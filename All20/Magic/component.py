from bs4 import BeautifulSoup


f=open('MagicFluidsFree.xml')
fdata=f.read()
soup=BeautifulSoup(fdata,"lxml")



print "START!!"
# Open a file
fo = open("python_for_xml.py", "wb")



pertag = soup.application.components.findAll('component') 

fo.write("import lxml.etree\n")
fo.write("import lxml.builder\n")  

fo.write("E = lxml.builder.ElementMaker()\n")
fo.write("ROOT = E.root\n")
fo.write("DOC = E.doc\n")

fo.write("component = E.component\n")
fo.write("packagename = E.packagename\n")
fo.write("conponentname = E.conponentname\n")
fo.write("action = E.action\n")

fo.write("the_doc = ROOT( \n")
fo.write("DOC(")


i=1
for per in pertag:
	
	pertag2= per.intentfilter.findAll('filter')
	
	for per2 in pertag2:
		pertag3= per2.findAll('actions') 
		for per3 in pertag3:
			if per3.string is not None:
				if per3.string[:7] == 'android':
					fo.write("component(\n") 
					fo.write("packagename('"+soup.application.packagename.string+"'),\n")
					fo.write("conponentname('"+per.find('name').string+"'),\n")
					fo.write("action('"+per3.string+"'),\n")
					fo.write("),\n")
				if per3.string[:11] == 'com.android':
					fo.write("component(\n") 
					fo.write("packagename('"+soup.application.packagename.string+"'),\n")
					fo.write("conponentname('"+per.find('name').string+"'),\n")
					fo.write("action('"+per3.string+"'),\n")
					fo.write("),\n")


fo.write(")\n")
fo.write(")\n")
fo.write("print lxml.etree.tostring(the_doc, pretty_print=True)\n")

fo.write("# Open a file\n")
fo.write("fo = open('actions.txt', 'wb')\n")
fo.write("fo.write( lxml.etree.tostring(the_doc, pretty_print=True));\n")

fo.write("# Close opend file\n")
fo.write("fo.close()\n")
print "END"


# Close opend file
fo.close()

