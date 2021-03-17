#
# exceptions.py
#
# the cati project
# Copyright 2020-2021 parsa shahmaleki <parsampsh@gmail.com>
#
# This file is part of cati.
#
# cati is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cati is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with cati.  If not, see <https://www.gnu.org/licenses/>.
##################################################

""" Dotcati section exceptions """

class InvalidPackageDirException(Exception):
    pass

class InvalidPackageFileException(Exception):
    pass

class DependencyError(Exception):
    pass

class ConflictError(Exception):
    pass

class PackageScriptError(Exception):
    pass

class PackageIsInSecurityBlacklist(Exception):
    pass

class FileConflictError(Exception):
    pass

class CannotReadFileException(Exception):
    pass
