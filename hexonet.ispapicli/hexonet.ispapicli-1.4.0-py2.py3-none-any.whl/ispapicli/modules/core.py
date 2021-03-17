from hexonet.apiconnector.apiclient import APIClient as AC
from hexonet.apiconnector.response import Response
import re
import argparse
import textwrap
import sys
from pathlib import Path
from datetime import datetime, timedelta
import json
import time
import os
from tabulate import tabulate
from textwrap import TextWrapper
from .db import DB

__version__ = "1.4.0"


class Core:
    def __init__(self):
        # create API client
        self.cl = AC()
        # Send statistics
        self.cl.setUserAgent("ISPAPICLI", __version__)
        # init db
        self.dbObj = DB()

    def initParser(self, args=None):
        """
        Initialize the parser using the python standard library 'argparse'
        This step adds all commands to be executed by the end-user

        Returns:
        --------
        ArgumentParser: parser
        """
        parser = argparse.ArgumentParser(add_help=False)
        parser.prog = "ispapi"
        parser.formatter_class = argparse.RawDescriptionHelpFormatter
        parser.epilog = textwrap.dedent(
            """
                ------------------------------------------------------------
                - You must login first to start requesting commands
                - You can use the command '--help <command>' to know everything about a specific command,
                - Or visit our documentation on: https://github.com/hexonet/hexonet-api-documentation
                ------------------------------------------------------------
            """
        )
        # args: will be the positional args
        parser.add_argument(
            "args", nargs=argparse.REMAINDER, help="All additional args, e.g. limit=5"
        )
        # command: is the user command to be executed e.g. QueryDomainList
        parser.add_argument(
            "--command",
            "-c",
            metavar="<command>",
            help="Enter a command e.g. -c=CheckDomain or -c CheckDomain",
        )
        # userid: used in login
        parser.add_argument(
            "--userid", "-u", metavar="<user id>", help="Your login user ID"
        )
        # password: used in login
        parser.add_argument(
            "--password", "-p", metavar="<your password>", help="Your login password"
        )
        # entitiy: either live or ote, used in login
        parser.add_argument(
            "--entity",
            "-e",
            choices={"live", "ote"},
            help="Set entity to either live or ote system e.g. -e=ote",
        )
        # gui: used to start the gui from the terminal
        parser.add_argument(
            "--gui",
            "-g",
            const="gui",
            nargs="?",
            metavar="<>",
            help="Start graphical application",
        )
        # help: used to show help about how to use the tool, generated by argparse dynamically
        parser.add_argument(
            "--help",
            "-h",
            const="all",
            nargs="?",
            metavar="<command>,<>",
            help="Show detailed use of a 'command' OR use --help to show help",
        )
        # list: used to list all the commands avaiable
        parser.add_argument(
            "--list",
            "-li",
            const="list",
            nargs="?",
            metavar="<>",
            help="List all commands' names",
        )
        # logout: used to kill the user session (locally and remotely)
        parser.add_argument(
            "--logout",
            "-l",
            const="logout",
            nargs="?",
            metavar="<>",
            help="Destroy your current session",
        )
        # update the local user commands. This will call scraper
        parser.add_argument(
            "--update",
            "-up",
            const="update",
            nargs="?",
            metavar="<>",
            help="Update local command list",
        )
        # version: show the tool version

        parser.add_argument(
            "--version", "-v", action="version", version="%(prog)s %(__version__)s"
        )

        return parser

    def parseArgs(self, args):
        """
        This function will check which command is triggered by the user and call a function accordingly

        Returns
        -------
        Tuple: (string, string)
        """
        # case logout
        if args["logout"] is not None:
            result = self.logout()
            return "logout", result
        # case gui
        if args["gui"] is not None:
            return "gui", ""
        # case help
        if args["help"] is not None:
            if args["help"] == "all":
                return "help", ""
            else:
                command_help = args["help"]
                help_info = self.getCommandHelp(command_help)
                return "help_command", help_info
        # case list of all commands
        if args["list"] is not None:
            commands_list = self.getCommandList()
            return "list", commands_list
        # case update commands triggered
        if args["update"]:
            return "update", ""

        # case login
        # check if login credentials provided
        if None not in (args["userid"], args["password"], args["entity"]):
            result, msg = self.login(args)
            return "msg", msg

        # otherwise it is a command requested
        # if logged in, and there is a session, then execute a command
        session_status = self.checkSession(args)
        if session_status == "valid":
            if args["command"] is not None:
                cmd_struct = {}
                cmd_struct["command"] = args["command"]
                return "cmd", cmd_struct
            if args["COMMAND"] is not None:
                cmd_struct = {}
                cmd_struct["command"] = args["COMMAND"]
                return "cmd", cmd_struct
            # case user trying to log in while his session is valid
            elif None not in (args["userid"], args["password"], args["entity"]):
                msg = "You are already logged in, your session is valid."
                return "msg", msg
            else:
                msg = "Command is not recognized!"
                return "cmd_unknown", msg
        # initial running
        elif session_status == "init":
            msg = "Login first, you can run the command: -u = <your user id> -p = <your password> -e = {ote,live}"
            return "msg", msg
        # case sessin expired
        elif session_status == "expired":
            msg = """
                Session expired. Please login again.
                Use the command: -u = <your user id> -p = <your password> -e = {ote,live}
                """
            return "msg", msg
        # case unknown command requested
        else:
            msg = "No command found!"
            return "cmd_unknown", msg

    def login(self, args, session_status=""):
        """
        This function perform remote login on the server

        Returns
        -------
        Tuple: ((True | False), msg:string)

        """
        user = args["userid"]
        password = args["password"]
        entity = args["entity"]
        # check which system to use, live of test
        if entity == "ote":
            # case ote is set, otherwise by default the system is live
            self.cl.useOTESystem()
        self.cl.setCredentials(user, password)
        r = self.cl.login()
        if r.isSuccess():
            # save login session
            loginSession = self.cl.getSession()
            # save session
            self.__saveLocalSession(loginSession, entity)
            msg = "Login success. Your session valid for one hour max of idle time"
            return True, msg
        else:
            desc = r.getDescription()
            code = r.getCode()
            msg = "Server response: " + str(code) + " " + desc
            return False, msg

    def checkSession(self, args=""):
        """
        Check local session.

        Returns
        -------
        String: 'valid' | 'init' | 'expired'
        """
        # check if there is a session already exist
        try:
            # query for login data
            data = self.dbObj.getLoginInfo()
            if not data:
                raise Exception
            # get login data
            entity = data[0]["entity"]
            t_old = data[0]["ts"]
            session = data[0]["session"]
            time_format = "%Y-%m-%d %H:%M:%S"
            t_now = datetime.now().strftime(time_format)
            t_now_object = datetime.strptime(t_now, time_format)
            t_old_object = datetime.strptime(t_old, time_format)
            t_new = t_now_object - timedelta(hours=1)
            if t_new < t_old_object:
                result = self.cl.setSession(session)
                if entity == "ote":
                    self.cl.useOTESystem()
                return "valid"
            else:
                return "expired"
            # Do something with the session file
        except Exception:
            return "init"

    def logout(self):
        """
        Delete user session.

        Returns:
        --------
        String: msg
        """
        try:
            msg = ""
            # query for login data
            data = self.dbObj.getLoginInfo()
            if not data:
                raise Exception
            # get login data
            entity = data[0]["entity"]
            session = data[0]["session"]
            if entity == "ote":
                self.cl.useOTESystem()
            # delete remote session
            self.cl.setSession(str(session))
            r = self.cl.logout()
            if r.isSuccess():
                flag = True
            else:
                flag = False

            # delete local session
            self.dbObj.deleteLoginInfo()

            # return message
            if flag:
                msg = "Successfully logged out!"
                return msg
            else:
                msg = "Local session deleted but couldn't delete remote session!"
                return msg

        except Exception as e:
            return "Couldn't delete remote session due to: " + str(e)

    def request(self, commands):
        """
        Request command from remote server.

        Returns:
        -------
        Response: response
        """
        response = self.cl.request(commands)
        return response

    def getResponse(self, response, mode=""):
        """
        Parse response based on user preference.

        Returns:
        --------
        List | String
        """
        if mode == "properties":
            return response.getListHash()
        elif mode == "list":
            return response.getListHash()
        elif mode == "plain":
            return response.getPlain()
        else:
            code = response.getCode()
            description = response.getDescription()
            message = "Server response: " + str(code) + " " + description
            return message

    def getCommandHelp(self, command_name):
        """
        Get help for a specific command: command_name.

        Returns:
        -------
        String: <>
        """
        data = self.dbObj.getCommand(command_name)
        for item in data:
            try:
                command_name_lower_case = (item["command"]).lower()
                if command_name_lower_case == command_name.lower():
                    command = item["command"]
                    description = item["description"]
                    availability = item["availability"]
                    paramaters = item["paramaters"]
                    basic_info = f"""
                                Command: {command}
                                Description: {description}
                                Availability: {availability}
                                Parameters:"""
                    # dedent, remove spaces
                    basic_info = textwrap.dedent(basic_info).strip()
                    headers = ["Parameter", "Min", "Definition", "Type"]
                    table = []
                    t = TextWrapper(width=30)
                    for row in paramaters:
                        row_data = []
                        for key in row:
                            if key == "Definition":
                                row_data.append(t.fill(row[key]))
                            else:
                                row_data.append(row[key])
                        table.append(row_data)

                    paramaters_table = tabulate(table, headers, tablefmt="fancy_grid")
                    return basic_info + "\n" + paramaters_table
            except Exception:
                continue
        else:
            return f"Command '{command_name}' not found!"

    def __saveLocalSession(self, loginSession, entity):
        """
        Saves users session in local file.

        Returns:
        --------
        Bool: True | False
        """
        try:
            time_format = "%Y-%m-%d %H:%M:%S"
            ts = datetime.now().strftime(time_format)
            data = {}
            data["session"] = loginSession
            data["ts"] = ts
            data["entity"] = entity
            # insert login
            if self.dbObj.setLoginInfo(data):
                return True
            else:
                raise Exception
        except Exception:
            return False

    def parseParameters(self, parameters):
        """
        Parse positional arguments, e.g. limit = 5.

        Returns:
        --------
        Set: params
        """
        params_len = len(parameters)
        params = {}
        i = 0
        while i < (params_len):
            if "=" in parameters[i]:
                key, value = parameters[i].split("=")
                params[key] = value
            else:
                key = parameters[i]
                i += 1
                value = parameters[i]
                params[key] = value
            i += 1
        # return result
        return params

    def getCommandList(self):
        """
        Get all commands from local commands' files

        Returns:
        --------
        String: return_list
        """
        return_list = ""
        data = self.dbObj.getAllCommands()
        for item in data:
            try:
                return_list += item["command"] + "\n"
            except Exception:
                continue
        return return_list

    def getSubUserList(self):
        """
        Get all subusers from local commands' files

        Returns:
        --------
        String: return_list
        """
        return_list = ""
        data = self.dbObj.getAllSubusers()
        for item in data:
            try:
                return_list += item["subuser"] + "\n"
            except Exception:
                continue
        return return_list

    def getMinParameters(self, command_name):
        """
        Get minimum required parameters of the command: command_name

        Returns:
        --------
        List: returnData
        """
        returnData = []
        data = self.dbObj.getCommand(command_name)
        if data:
            for item in data:
                try:
                    command_name_lower_case = (item["command"]).lower()
                    if command_name_lower_case == command_name.lower():
                        paramaters = item["paramaters"]
                        for row in paramaters:
                            paramater = row["Parameter"]
                            minValue = row["Min"]
                            if minValue == "1" and paramater != "COMMAND":
                                returnData.append(paramater.lower())
                except Exception:
                    continue
        return list(dict.fromkeys(returnData))

    def getSubUsers(self):
        cmd = {
            "command": "finduser",
            "pattern": "%",
            "userdepth": "all",
            "orderby": "userid",
        }
        response = self.request(cmd)
        listResult = response.getListHash()["LIST"]
        for item in listResult:
            subusers = {}
            subusers["subuser"] = item["USER"]
            self.dbObj.insertSubuser(item["USER"], subusers)
        pass
