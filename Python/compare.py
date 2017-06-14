import sys
from bs4 import BeautifulSoup

  
reload(sys)
sys.setdefaultencoding('utf8')

a=open('actions.xml')
adata=a.read()
soupa=BeautifulSoup(adata,"lxml")

b=open('intentAll.xml')
bdata=b.read()
soupb=BeautifulSoup(bdata,"lxml")


docs  = soupa.root.doc.findAll('component') 
docs2 = soupb.root.findAll('doc') 
temp="2"

fo = open("result.txt", "wb")
for d in docs:
       for d2 in docs2:
        	intents2=d2.findAll('intent')
		for intent2 in intents2:
			if(intent2.action.string=='"'+d.action.string+'"'):
				print '{source: "'+d.packagename.string+'", target: "'+d.conponentname.string+'", type:"licensing"},\n'
				print '{source: "'+intent2.intentname.string+'", target: "'+intent2.sender.string+'", type:"licensing"},\n'
				print '{source: "'+intent2.intentname.string+'", target: "'+d.conponentname.string+'", act:"'+d.action.string+'"},\n'
 				fo.write( '{source: "'+d.packagename.string+'", target: "'+d.conponentname.string+'", type:"licensing", act:"component relationshp"},\n');
				fo.write( '{source: "'+intent2.intentname.string+'", target: "'+intent2.sender.string+'", type:"licensing", act:"component relationshp"},\n');
				fo.write( '{source: "'+intent2.intentname.string+'", target: "'+d.conponentname.string+'", act: "Intent</br>Action:</br>'+d.action.string+'"},\n');
					
		


# Close opend file
fo.close()
