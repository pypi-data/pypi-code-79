
# This file was generated by 'versioneer.py' (0.18) from
# revision-control system data, or from the parent directory name of an
# unpacked source archive. Distribution tarballs contain a pre-generated copy
# of this file.

import json

version_json = '''
{
 "date": "2021-03-17T07:00:19+0000",
 "dirty": false,
 "error": null,
 "full-revisionid": "b27ec4e21daea580ffe2a1a416591da4446e05f5",
 "version": "1.15.0.post.dev91"
}
'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)
