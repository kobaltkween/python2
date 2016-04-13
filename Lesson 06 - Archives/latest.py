import glob
import os
import zipfile

def latest(num = 1, path = "."):
    files = glob.glob(os.path.join(path, '*'))
    datedFiles = [(os.path.getmtime(fn), os.path.abspath(fn)) for fn in files]
    datedFiles.sort()
    latestFiles = [f for (d, f)in datedFiles[-num:]]
    latestFiles.reverse()
    return latestFiles

def zipLatest(fn, num, path):
    filesToArchive = latest(num, path)
    zf = zipfile.ZipFile(fn, 'w', zipfile.ZIP_DEFLATED)
    for fnToArchive in filesToArchive:
        zf.write(fnToArchive)
    zf.close()