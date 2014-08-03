import csv
##import operator
import heapq
import pprint

from igraph import *
##tempList =[]
##fromList = []
##toList = []
##g = Graph.Famous("petersen")
##counterfrom = 0
##counterto = 0

dict={}
dict1 = {}
counter = 0
edgecount = 0
vertices = []


##this method is to check if the given edge belong to certain subject
def edgeSubject(src, des, subterm):
    sim1 = 0
    sim2 = 0
    sim3 = 0
    emailreader = csv.reader(open('EmailRec.csv', 'rb'))
    for rec in emailreader:
        if src == rec[2]:
            sim1+=1
            if des in rec[3].split(','):
                sim2+=1
                if subterm in rec[1].split(' '):
                    sim3+=1
                    print 'True : Break'
                    print 'sim1: ', sim1, 'sim2: ', sim2, 'sim3: ', sim3
                    return True
    return False
            
    
    
##parsing the subject into set of terms and counting their occurences
##the first element defines the email category
##we found three emails where subject is missed up (=?windows...
def readSubject(sub):
    subterms = sub.split(' ')
    for subter in subterms:
        if dict1.has_key(subter):
            dict1[subter] = dict1[subter] + 1
        else:
            dict1[subter] = 1

def findTopTerms(n):
    termlist = [(value,key) for key, value in dict1.items()]
    print 'top ', n, ' terms out of ', len(dict1)
    pprint.pprint(heapq.nlargest(n, termlist))
def findTopDegrees(n):
    degreelist = g.degree(type="in")
    nlargdegree = heapq.nlargest(n, degreelist)
    ##pprint.pprint(heapq.nlargest(n, degreelist))
    for elm in nlargdegree:
        print elm, ' maximum degree is for : ', vertices[degreelist.index(elm)]
    
# if the key already in, update its to list
def updateDictRec(key, newVal):
    oldVal = dict[key]
    ##print 'before',len(oldVal)
    for email in newVal:
        if  email not in oldVal and email != key and email !='':
            ##print email
            oldVal.append(email)
    dict[key] = oldVal
    
emailReader = csv.reader(open('EmailRec.csv', 'rb'))

for row in emailReader:
    readSubject(row[1])
    if dict.has_key(row[2]):
        updateDictRec(row[2],row[3].split(','))
        ##print 'after',len(dict[row[2]])
    else:
        dict[row[2]]= row[3].split(',')
findTopTerms(100)

##edgeSubject('emre.dogru@stratfor.com', 'bhalla@stratfor.com', 'Turkey')
for key in dict:
    if key in dict[key]:
        dict[key].remove(key)
        print key, ' removed'

## counting number of vertices required
## the vertices list will index every email once
for key in dict:
    if key not in vertices and key !='':
        vertices.append(key.strip())
        ##print key
        counter+=1
    for toemail in dict[key]:
        if toemail not in vertices:
            ##print toemail
            vertices.append(toemail.strip())
            counter+=1

##vertices.remove('')
g = Graph(len(vertices))
g.vs["name"] = vertices
g.to_directed(mutual=True)

term = r"INSIGHT"
print len(dict)
for key in dict:
    if key != '':
        for toemail in dict[key]:
            ##print 'the key related to ', key
            if edgeSubject(key, toemail, term):
                g.add_edges((vertices.index(key.strip()),vertices.index(toemail.strip())))
                edgecount+=1
                
        
print 'number of vertices: ',  len(vertices)
print 'number of edges: ', edgecount

findTopDegrees(20)
##layout = g.layout("kk")
##plot(g, layout= layout)

        



        
    
   
    
