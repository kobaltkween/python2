import glob
import os
import sys

def count(path):
    "Get the list of files in the directory"
    fileCount = {}
    files = glob.glob(os.path.join(path, "*"))
    if  os.path.exists(path):
        if files:     
            for file in files:
                if not os.path.isdir(file):
                    ext = os.path.splitext(file)[1]
                    if ext in fileCount.keys():
                        fileCount[ext] += 1
                    else:
                        fileCount[ext] = 1
        else: 
            fileCount = "There are no files in the directory."
    else: 
        fileCount = "The directory does not exist."
    return fileCount

def buildCountList(res):
    if type(res) is str:
        s = res
    elif type(res) is dict: 
        s = "Ext | Files\n"
        s += "-----------\n"
        for ext, num in res.items():
            s += '{0:>3} : {1:<5}\n'.format(ext[1:], str(num))
    else:
        s = "Wrong type of input"
    return s
    
if __name__ == "__main__":
    try:
        fileCount = count(sys.argv[1])
    except Exception as error:
        fileCount = ('Problem: {0}'.format(error))
    print (buildCountList(fileCount))