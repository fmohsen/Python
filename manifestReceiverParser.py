import xml.etree.ElementTree as ET
from xml.dom import minidom

#from lxml import etree

import glob
import ntpath
cntPer = 0
cntNonPer = 0
hasPermission = False
cnt = 0
numOfPerm = 0
typeA = 0
typeB = 0
typeAB = 0
typeBNo = 0
typeANo = 0
typeABNo = 0
intNoWriteCnt = 0
intNWSNoWriteCnt = 0
permFreq = []
permDict = {}
appPerm = []
writeper = "android.permission.WRITE_EXTERNAL_STORAGE"
interperm = "android.permission.INTERNET"
nwsperm = "android.permission.ACCESS_NETWORK_STATE"
hasReciever = 0
noReceiver = 0

def isKeyboardApp(approot):
    iskb = False
    for child in approot.getchildren():
        if child.tag == "application":
            for subchild in child.getchildren():
                if subchild.tag == "service":
                    attrs = subchild.attrib
                    keys =  attrs.keys()
                    for key in keys:
                        if ( attrs[key] == "android.permission.BIND_INPUT_METHOD"):
                            iskb = True
                            #print ntpath.basename(files), " is a keyboard app"
                            break                        
    return iskb

def hasReceiverComp(approot):
    hasReceiver = False
    for child in approot.getchildren():
        if child.tag == "application":
            for subchild in child.getchildren():
                if subchild.tag == "receiver":
                    hasReceiver = True
                    break
                    
##                    attrs = subchild.attrib
##                    keys =  attrs.keys()
##                    for key in keys:
##                        if ( attrs[key] == "android.permission.BIND_INPUT_METHOD"):
##                            iskb = True
##                            #print ntpath.basename(files), " is a keyboard app"
##                            break                        
    return hasReceiver

###########################################
def printIntentFilters(approot):
    hasReceiver = False
    for child in approot.getchildren():
        if child.tag == "application":
            for subchild in child.getchildren():
                if subchild.tag == "receiver":
                    hasReceiver = True
                    for subsubchild in subchild.getchildren():
                        if subsubchild.tag == "intent-filter":
                            print "found intent filter"
                            for subsubsubchild in subsubchild.getchildren():
                                print subsubsubchild
                                attrs = subsubsubchild.attrib
                                keys = attrs.keys()
                                for key in keys:
                                    print key

                                
#########################################################
##    typeB = False
##    if writeper in permlist and interperm in permlist and nwsperm in permlist:
##        typeB = True
##    print typeB
##    return typeB
def attackBNoType(permlist):
    typeB = False
    if writeper in permlist and interperm in permlist:
        typeB = True
    print typeB
    return typeB

def attackAType(permlist):
    typeA = False
    if interperm in permlist and nwsperm in permlist:
        typeA = True
    print typeB
    return typeA
def attackANoType(permlist):
    typeA = False
    if interperm in permlist:
        typeA = True
    print typeB
    return typeA
def intNoWrite(permlist):
    intNoW = False
    if interperm in permlist and not(writeper in permlist):
        intNoW = True
    return intNoW
def intNWSNoWrite(permlist):
    intNWSNoW = False
    if interperm in permlist and nwsperm in permlist and not(writeper in permlist):
        intNWSNoW = True
    return intNWSNoW

def findReceiverAction(f):
    for manifest_tag in f.findall('application'):
        for app_item in manifest_tag.findall('receiver'):
            for activity_item in app_item.findall('intent-filter'):
                    for intent_filter in activity_item.findall('action'):                              
                         print intent_filter.get('android:name')

    
#dropbox    
#for files in glob.glob("C:\\Users\\Fadi\\Desktop\\DropboxAppsZIP\\DropboxManifests\\*.xml"):
#Keyboards
for files in glob.glob("C:\\Users\\Fadi\\Desktop\\Top\\Games\\Adventure\\Manifests\\*.xml"):
    
    
##    perm = ET.parse(files).findall('uses-permissions')
##    print perm
    print "****************************"
    #print "*",ntpath.basename(files),"*"
    #print "****************************"
    #print files
    
    path = files.split('\\')
    print path[len(path)-1]
    

    #parser = ET.XMLParser(encoding="utf-8")
    #tree = ET.fromstring(files, parser=parser)
    tree = ET.parse(files)
    root = tree.getroot()
    
    if hasReceiverComp(root):
        findReceiverAction(root)
        hasReciever = hasReciever + 1
        #printIntentFilters(root)
        print "has receiver component"
    else:
        noReceiver = noReceiver + 1
        print "doesn't have a receiver component"
##for perm in root.findall('uses-permission'):
####    print perm.items()
####    print perm.getchildren()
##    print perm.tag
##    print perm.tail
##    print perm.text
    ##for child in root:
        
        
##        if child.tag == "uses-permission":
##            numOfPerm = numOfPerm + 1
##            hasPermission = True
##            attrs = child.attrib
##            keys =  attrs.keys()
##        print "keys: ", keys
##        print "keys[0]: ", keys[0]
##        print "length: ", len(attrs)
##        print "attrs: ", attrs
##            if isKeyboardApp(root):
##                print ntpath.basename(files), " is a keyboard app"
##                appPerm.append(attrs[keys[0]])
##                if attrs[keys[0]] in permDict:
##                    permDict[attrs[keys[0]]] +=1
##                else:
##                    permDict[attrs[keys[0]]] = 1
##                
##                print attrs[keys[0]]
##            
##    if(hasPermission):
##        cntPer = cntPer + 1
##    else:
##        cntNonPer = cntNonPer + 1
##    hasPermission = False
##    cnt = cnt + 1
##    print "Number of Permissions: " , numOfPerm
##    if(isKeyboardApp(root)):
##       permFreq.append(numOfPerm)
##       if (attackBType(appPerm)):
##           typeB = typeB + 1
##       if(attackAType(appPerm)):
##           typeA = typeA + 1
##       if(attackAType(appPerm) or attackBType(appPerm)):
##           typeAB = typeAB + 1
##       if(attackANoType(appPerm)):
##           typeANo = typeANo + 1
##       if(attackBNoType(appPerm)):
##           typeBNo = typeBNo + 1
##       if(attackANoType(appPerm) or attackBNoType(appPerm)):
##           typeABNo = typeABNo + 1
##       if(intNoWrite(appPerm)):
##           print "internet no write"
##           intNoWriteCnt = intNoWriteCnt + 1
##       if(intNWSNoWrite(appPerm)):
##           print "internet and nws no write"
##           intNWSNoWriteCnt = intNWSNoWriteCnt + 1
##
##           
##    numOfPerm = 0
##    appPerm = []
##    
##print "number of apps processed: ", cnt
##print "number of apps with zero permission: ", cntNonPer
##print "number of apps with one or more permission: ", cntPer
##print "number of apps with typeA attacks : " , typeA
##print "number of apps with typeB attacks : " , typeB
##print "number of apps with typeAB attacks : " , typeAB
##print "number of apps with typeA- attacks : " , typeANo
##print "number of apps with typeB- attacks : " , typeBNo
##print "number of apps with typeAB- attacks : " , typeABNo
##print "number of apps with internet but no write : " , intNoWriteCnt
##print "number of apps with internet, nw state but no write : " , intNWSNoWriteCnt
    
##    print cnt
##    cnt = cnt + 1
##    print files
##    tree = ET.parse(files)
##    tree.parse(
##    root = tree.getroot()
##    for perm in root.findall('uses-permissions'):
##        print perm.get('android:name')
##  
