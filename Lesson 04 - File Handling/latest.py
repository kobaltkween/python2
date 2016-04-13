import glob
import os

def latest(num = 1, path = "."):
    filesWithDates = []
    files = glob.glob(os.path.join(path, "*"))
    latestFiles = []
    for fn in files:
        filesWithDates.append((os.path.getmtime(fn), os.path.abspath(fn)))
    filesWithDates.sort()
    for fileInfo in filesWithDates[-num:]:
        latestFiles.append(fileInfo[1])
    latestFiles.reverse()
    return latestFiles                                