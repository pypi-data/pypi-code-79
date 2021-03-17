import logging
import os
import re
from os import mkdir, path
from pathlib import Path
from github import Github
from kolibri.utils.dict import Dict

DATA_PATH = os.path.join(str(Path.home()), '.kolibri')

GITHUB_TOKEN="b24a0ab736f38891bdee41664c7d539176790148"
GITHUB_REPO_NAME="mbenhaddou/kolibri"

Path(DATA_PATH).mkdir(exist_ok=True, parents=True)

data = Dict({
    'MIN_EXAMPLES_PER_CLASS': 15,
    'MIN_EXAMPLES_PER_ENTITY': 2
})

# [entity_text](entity_type(:entity_synonym)?)
ent_regex = re.compile(r'\[(?P<entity_text>[^\]]+)'
                       r'\]\((?P<entity>[^:)]*?)'
                       r'(?:\:(?P<text>[^)]+))?\)')

DEFAULT_SERVER_PORT = 5005

EMBEDDING_SIZE = 100
WORD2VEC_WORKERS = 4
MIN_WORD_COUNT = 5
WORD2VEC_CONTEXT = 5

LOGS_DIR = path.join(DATA_PATH, 'logs')
LOG_NAME = 'kolibri'
LOG_FILE = path.join(LOGS_DIR, LOG_NAME + '.log')
LOG_LEVEL = logging.DEBUG

MINIMUM_COMPATIBLE_VERSION = "0.0.1"

DEFAULT_NLU_FALLBACK_THRESHOLD = 0.0

DEFAULT_CORE_FALLBACK_THRESHOLD = 0.0

DEFAULT_REQUEST_TIMEOUT = 60 * 5  # 5 minutes

DEFAULT_SERVER_FORMAT = "http://localhost:{}"

DEFAULT_SERVER_URL = DEFAULT_SERVER_FORMAT.format(DEFAULT_SERVER_PORT)

corenlp = Dict({
    'LIBRARY_PATH': '/Users/mbenhaddou/Stanford/stanford-corenlp-full-2018-02-27/',
    'PORT': 9000,
    'D2V_MODEL_PATH': "/Users/mbenhaddou/Documents/Mentis/Developement/Python/Kolibri/kolibri/features/doc2vec/model"
})

modeling = Dict({
    # How many classes are at max put into the output class ranking, everything else will be cut off
    'TARGET_RANKING_LENGTH': 10
})

dialog = Dict({
    'INTENT_MESSAGE_PREFIX': "/",
    'DEFAULT_FALLBACK_ACTION': "action_default_fallback",
    'USER_INTENT_RESTART': "/restart",  # dINTENT_MESSAGE_PREFIX +
    'DOCS_BASE_URL': '.',
    'FALLBACK_SCORE': 1.1
})

DOCUMENT_TEXT_MAX_LENGTH = 255

DOCUMENT_LABEL_MAX_LENGTH = 32

# The maximum length_train of characters that the name of a tag can contain
TAG_NAME_MAX_LENGTH = 50

DIRS = [DATA_PATH, LOGS_DIR]

for d in DIRS:
    if not path.exists(d):
        mkdir(d)



try:
    Resources_sha
except NameError:
    Resources_sha={}
path_i=Path(".")
path=path_i
__repo=Github(GITHUB_TOKEN).get_repo(GITHUB_REPO_NAME)
__branch=__repo.get_branch("main").commit





def traverse(node, path = [], paths = []):

    if hasattr(node, "path"):
        path.append(node.path)
    if hasattr(node, "type") and node.type == "blob":
        data=dict(node.raw_data)
        data['path']='/'.join(path)
        data['url']="https://raw.githubusercontent.com/mbenhaddou/kolibri/main/{}".format(data['path'])
        Resources_sha['/'.join(path[1:])]=data

        path.pop()
    else:
        for child in __repo.get_git_tree(node.sha).tree:
            traverse(child, path, paths)
        if path:
            path.pop()

p=[]
for child in __repo.get_git_tree(__branch.sha).tree:
    if child.path=="data":
        traverse(child, p, Resources_sha)
