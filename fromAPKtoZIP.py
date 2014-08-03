import os
import glob

#os.chdir("C:\Users\Fadi\Dropbox\SharedWithMe\Android\AbeerAPKs")
#os.chdir("C:\Users\Fadi\Dropbox\SharedWithMe\Android\DropboxApps")
##os.chdir("C://Users//Fadi//Desktop//apktool//apktool-install-windows-r05-ibot//keyboards//unprocessed")
##print "Before hand...."
##for files in glob.glob("*.apk"):
##    print files

path =  "C://Users//Fadi//Desktop//DropboxAppsZIP//DropboxManifests"  
#for filename in os.listdir("C://Users//Fadi//Dropbox//SharedWithMe//Android//AbeerAPKs"):
#for filename in os.listdir("C:\Users\Fadi\Dropbox\SharedWithMe\Android\DropboxApps"):
for filename in os.listdir("C://Users//Fadi//Desktop//DropboxAppsZIP//DropboxManifests"):   
    print "before " , path + "//" + filename
##    print "after " , filename.replace(' ','')
    ##os.rename(filename, filename.replace(' ',''))
    #os.rename(filename, filename.replace(' - ',''))
    #if(filename.isspace()):
    print "after " , path + "//"+ filename.replace('.xmlp.txt','.xml')
    #print "after " , filename.replace(' ','')

#from APK to Zip
   # os.rename(path + "//" + filename, path + "//"+ filename.replace('.apk','.zip'))
    os.rename(path + "//" + filename, path + "//"+ filename.replace('.xmlp.txt','.xml'))
        #os.rename(filename, filename.replace(' - ',''))
 
##print "Afterwards!" 
##os.chdir("C://Users//Fadi//Desktop//apktool//apktool-install-windows-r05-ibot//keyboards//unprocessed")
##for files in glob.glob("*.apk"):
##    print files
