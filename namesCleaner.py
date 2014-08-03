import os
import glob

###os.chdir("C:\Users\Fadi\Dropbox\SharedWithMe\Android\AbeerAPKs")
##os.chdir("C:\Users\Fadi\Dropbox\SharedWithMe\Android\DropboxApps")
##for files in glob.glob("*.apk"):
##    print files
##    
###for filename in os.listdir("C://Users//Fadi//Dropbox//SharedWithMe//Android//AbeerAPKs"):
##for filename in os.listdir("C:\Users\Fadi\Dropbox\SharedWithMe\Android\DropboxApps"):
##    if(filename.isspace()):
##        print filename
##        os.rename(filename, filename.replace(' ',''))
## 
## 
##os.chdir("C:\Users\Fadi\Dropbox\SharedWithMe\Android\DropboxApps")
##for files in glob.glob("*.apk"):
##    print files


startingDir = os.getcwd() # save our current directory
#testDir = "C:\\Users\\Fadi\\Dropbox\\Android\\dex2jar-0.0.9.12" # note that \ is windows specific, and we have to escape it
#testDir = "C:\\Users\\Fadi\\Dropbox\\Android\\dex2jar-0.0.9.12"
testDir = "C:\\Users\\Fadi\\Dropbox\\Fadi Mohsen\\Mobile WebViews References\\Example\\dex2jar-0.0.9.12"
os.chdir(testDir) # change to our test directory


#path = "C:\\Users\\Fadi\\Dropbox\\SharedWithMe\\Android\\DropboxApps"

path = "C:\\Users\\Fadi\\Desktop\\DropboxApps"

#os.chdir("C:\Users\Fadi\Dropbox\SharedWithMe\Android\OldInput")
#for files in glob.glob("C:\Users\Fadi\Dropbox\SharedWithMe\Android\DropboxApps\*.apk"):
for files in glob.glob("C:\Users\Fadi\Desktop\DropboxApps\*.apk"):
    print 'processing ' ,  files
    os.system("dex2jar " + files)


os.chdir(startingDir) # change back to where we started
