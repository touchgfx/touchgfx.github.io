from modules import helpers
import os, shutil, glob
from pathlib import Path
from functools import *

def copyFolder(source, destination, excluded=[]):
  path = ""
  for file in glob.glob(f"{source}/**/*", recursive=True):
    if any(map(lambda exclude : file.lower().endswith(exclude), excluded)):
      continue

    path = destination + file[len(source):]
    if Path(file).is_file():
      Path(path).parent.mkdir(parents=True, exist_ok=True)
      shutil.copy2(file, path)
    else:
      Path(path).mkdir(parents=True, exist_ok=True)

versions = helpers.getVersions()
latestVersion = helpers.getLatestVersion(versions)

files = os.listdir(f"./{latestVersion}/")

replacementMap = [(f"/{latestVersion}/{os.path.splitext(entry)[0] if entry.lower().endswith('.html') else entry}", f"/{os.path.splitext(entry)[0] if entry.lower().endswith('.html') else entry}") for entry in files] + [
  (f"/{latestVersion}/<", f"/<"),
  (f"/{latestVersion}/\"", f"/\""),
]

excludedFiles = [
  ".png",
  ".webp",
  ".jpeg",
  ".jpg",
  ".bmp",
  ".svg",
  ".mp4",
  ".pdf",
  ".zip",
  ".git",
]

excludedFolders = [
  ".git",
]

print("Copying files to temporary folder")
source = f"./{latestVersion}"
destination = "./tmp"
copyFolder(source, destination, [".git"])

print("Updating file locations")
helpers.findReplace(f"{destination}/", replacementMap, excludedFiles, excludedFolders)

print("Copying updated files to root")
source = f"./tmp"
destination = "."
copyFolder(source, destination, [".git"])

print("Removing temporary folder")
shutil.rmtree(source)
