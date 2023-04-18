from modules import helpers
from functools import *
from pprint import pp

versions = helpers.getVersions()
latestVersion = helpers.getLatestVersion(versions)

excludedFolders = [
  ".git",
]

print("Removing version banner from latest version")
helpers.hideTagById(f"./{latestVersion}/", "doc-version-banner-identifier", excludedFolders)

helpers.findReplaceRegex(f"./{latestVersion}", [
  (r"(\.createElement\(\"div\",\{id:\"doc-version-banner-identifier\",)", r'\g<1>"data-nosnippet":true,hidden:true,'),
], [
  ".js",
], excludedFolders)