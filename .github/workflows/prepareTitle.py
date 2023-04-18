import re
from modules import helpers
from functools import *
from pprint import pp

# versions = helpers.getVersions()
versions = ["4.13"]
# latestVersion = helpers.getLatestVersion(versions)
latestVersion = "4.21"

excludedFolders = [
  ".git",
  latestVersion,
]

print("Adding version in the titles of archived versions")
for version in filter(lambda version : version != latestVersion, versions):
  helpers.findReplaceRegex(f"./{version}", [
    (r"(<title.*?>*)(<\/title>)", r"\g<1> " + version + r"\g<2>"),
    (r"(<meta[^>]*?property=\"og:title\"[^>]*?content=\"[^\">]*?)(\">)", r"\g<1> " + version + r"\g<2>"),
  ], [
    ".html",
    ".htm",
  ], excludedFolders)

  helpers.findReplaceRegex(f"./{version}", [
    (r"/({title:\"TouchGFX Documentation)(\")/g", r"\g<1> " + version + r"\g<2>"),
  ], [
    ".js",
  ], excludedFolders)