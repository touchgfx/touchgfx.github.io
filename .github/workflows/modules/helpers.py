import os, re
from functools import *

def findReplace(directory: str, replacementMap: list[tuple[str, str]], excludedFiles: list[str], excludedFolders: list[str]):
  for path, dirs, files in os.walk(directory):
    if any(map(lambda exclude : exclude in path.lower(), excludedFolders)):
      continue

    for filename in filter(lambda name : not any(map(lambda exclude : name.lower().endswith(exclude), excludedFiles)), files):
      filepath = os.path.join(path, filename)
      
      with open(filepath, encoding="utf-8") as f:
        s = f.read()
      
      for entry in replacementMap:
        s = s.replace(entry[0], entry[1])

      with open(filepath, "w", encoding="utf-8") as f:
        f.write(s)

def findReplaceRegex(directory: str, replacementMap: list[tuple[re.Pattern, str]], includedFiles: list[str], excludedFolders: list[str]):
  for path, dirs, files in os.walk(directory):
    if any(map(lambda exclude : exclude in path.lower(), excludedFolders)):
      continue

    for filename in filter(lambda name : any(map(lambda include : name.lower().endswith(include), includedFiles)), files):
      filepath = os.path.join(path, filename)
      
      with open(filepath, encoding="utf-8") as f:
        s = f.read()
      
      for entry in replacementMap:
        s = re.sub(entry[0], entry[1], s)

      with open(filepath, "w", encoding="utf-8") as f:
        f.write(s)

def hideTagById(directory: str, id: str, excludedFolders: list[str]):
  for path, dirs, files in os.walk(directory):
    if any(map(lambda exclude : exclude in path.lower(), excludedFolders)):
      continue

    for filename in filter(lambda name : name.lower().endswith(".html") or name.lower().endswith(".htm"), files):
      filepath = os.path.join(path, filename)
      
      with open(filepath, encoding="utf-8") as f:
        s = f.read()

      s = s.replace(f"id=\"{id}\"", f"id=\"{id}\" data-nosnippet hidden")

      with open(filepath, "w", encoding="utf-8") as f:
        f.write(s)

def getVersions():
  versionPattern = re.compile(r"^(\d+\.\d+)$")

  return [x for x in filter(versionPattern.search, next(os.walk("./"))[1])]

def getLatestVersion(versions):
  return reduce(lambda prev, now : now if float(now) > float(prev) else prev, versions, "0.0")
