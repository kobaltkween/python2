import zipfile
import os
import glob

def zipDir(myPath):
    # Make sure the path doesn't end in a trailing slash
    myPath = os.path.normpath(myPath)
    # Get all the files in the directory
    files = glob.glob(os.path.join(myPath, '*'))
    # Make a zip file in the directory
    fn = os.path.join(myPath, 'fileArchive.zip')
    zf = zipfile.ZipFile(fn, 'w', zipfile.ZIP_DEFLATED)
    # If it isn't a directory
    for f in files:
        if os.path.isfile(f) and f != fn:
            zf.write(f, os.path.relpath(f, os.path.dirname(myPath)))      
    zf.close()
    # Close up the zip
    return fn