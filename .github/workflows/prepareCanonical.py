import re
from modules import helpers
from functools import *
from pprint import pp

versions = helpers.getVersions()

excludedFolders = [
  ".git",
]

print("Fixing canonical")
for version in versions:
  helpers.findReplaceRegex(f"./{version}", [
    (r"(<link[^>]*? rel=\"canonical\" href=\"https:\/\/support\.touchgfx\.com).+?(\/docs)", r"\g<1>\g<2>"),
  ], [
    ".html",
    ".htm",
  ], excludedFolders)

  helpers.findReplaceRegex(f"./{version}", [
    (r"(\.createElement\(\"link\",\{rel:\"canonical\",href:.+?)(\})", r"\g<1>" + f'.replace("/{version}/docs", "/docs")' + r"\g<2>"),
  ], [
    ".js",
  ], excludedFolders)