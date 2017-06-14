from bs4 import BeautifulSoup


f=open('PhotoEditor.xml')
fdata=f.read()
soup=BeautifulSoup(fdata,"lxml")



print "START"
# Open a file
fo = open("intent_xml_generator.py", "wb")




pertag = soup.application.newintents.findAll('intent') 

fo.write("import lxml.etree\n")
fo.write("import lxml.builder\n")  

fo.write("E = lxml.builder.ElementMaker()\n")
fo.write("ROOT = E.root\n")
fo.write("DOC = E.doc\n")

fo.write("intent = E.intent\n")
fo.write("sender = E.sender\n")
fo.write("action = E.action\n")
fo.write("intentname = E.intentname\n")

fo.write("the_doc = ROOT( \n")
fo.write("DOC(")


for per in pertag:
	pertag2= per.findAll('action')
	for per2 in pertag2:
		if per2.string is not None:
			if per2.string[:8] == '"android':
				fo.write("intent(\n") 
				fo.write("intentname('"+soup.application.packagename.string+"'),\n")
				fo.write("sender('" + per.sender.string + "'),\n") 
				fo.write("action('" + per2.string + "'),\n")
				fo.write("),\n")
			if per2.string[:12] == '"com.android':
				fo.write("intent(\n") 
				fo.write("intentname('"+soup.application.packagename.string+"'),\n")
				fo.write("sender('" + per.sender.string + "'),\n") 
				fo.write("action('" + per2.string + "'),\n")
				fo.write("),\n")
fo.write(")\n")
fo.write(")\n")



fo.write("print lxml.etree.tostring(the_doc, pretty_print=True)\n")

fo.write("# Open a file\n")
fo.write("fo = open('intent.txt', 'wb')\n")
fo.write("fo.write( lxml.etree.tostring(the_doc, pretty_print=True));\n")

fo.write("# Close opend file\n")
fo.write("fo.close()\n")
print "END"


# Close opend file
fo.close()

