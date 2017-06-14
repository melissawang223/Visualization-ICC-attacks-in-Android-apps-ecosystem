# Open a file
fo = open("short.txt", "wb")
arrays = ["1"]
with open("dataAll.txt", "r") as ins:
    for line in ins:
	temp=0
	for array in arrays:
		
		
    		if( array == line ):
			temp=1
			break
		if( "android.intent.action.MAIN" == line[-30:-4] ):
			temp=1
			break
		if( "android.intent.action.VIEW" == line[-30:-4] ):
			temp=1
			break
		
        if(temp==0):
		arrays.append(line)
			



for a in arrays:
    fo.write(a);

fo.close()
