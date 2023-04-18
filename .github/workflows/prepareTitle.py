import re
from modules import helpers
from functools import *
from pprint import pp

versions = helpers.getVersions()
latestVersion = helpers.getLatestVersion(versions)

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
    (r"(\{title:[a-zA-Z]+?,titleDelimiter:[a-zA-Z]+?\}=[a-zA-Z]+?;return\(null==[a-zA-Z]+?\?void 0:[a-zA-Z]+?\.trim\(\)\.length\)\?`\$\{[a-zA-Z]+?\.trim\(\)\} \$\{[a-zA-Z]+?\} \$\{[a-zA-Z]+?\})(`:[a-zA-Z]+?\})", r"\g<1> " + version + r"\g<2>"),
  ], [
    ".js",
  ], excludedFolders)