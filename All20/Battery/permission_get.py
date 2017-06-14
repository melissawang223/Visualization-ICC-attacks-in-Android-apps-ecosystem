from bs4 import BeautifulSoup

f=open('BatteryHD.xml')
fdata=f.read()
soup=BeautifulSoup(fdata,"lxml")

print "START"
# Open a file
fo = open("permission_file.txt", "wb")


pertag = soup.application.usespermissions.findAll('permission') 
perS ="1"
for per in pertag:
	perS=perS+"</br>"+per.string


fo.write( '{source: "' )
fo.write(soup.application.packagename.string)
fo.write('", target: "')
fo.write(soup.application.packagename.string)
fo.write('", per: "')
fo.write(perS)
fo.write('"},\n');
	
print "END"




# Close opend file
fo.close()
