variables= ["r=","b=","g=", "x=", "y=", "z=", "distance=","energy=","specular="]


def updateMap(filePath):
    """"updates old format to new one compatibble with xsd"""
    file= open(filePath, "r+")
    data= file.read()

    light =  data.find("<light b")
    while light!= -1:
        value=[None]*9
        for i in range(9):
            Start= data.find(variables[i],
                        light,
                        data.find("/>",light))

            if  Start == -1:
                print("expression: "+ variables[i] + " not found")
                break;

            value[i]= data[ Start+len(variables[i])+1 : data.find("\"", Start+len(variables[i])+2) ]

        #yeah i couldve used %s things, happens
        insert= '\t<light distance="' + str(value[6]) + '" energy="'+ value[7] +'">\n' + \
                '\t\t<position x="'+ value[3] + '" y="'+ value[4] +'" z="'+ value[5] +'"/>\n' + \
		        '\t\t<color r="' + value[0] +'" g="'+ value[2]+ '" b="'+ value[1] + '"/>\n' + \
	            '\t</light>\n'

        data=data[:(light-1)] + insert + data[data.find("/>", light)+2:]

        print("finished replacing ")
        light=data.find("<light b")

    mId = data.find("mid=")
    while mId != -1:
        data= data[:mId - 1] + data[:mId+1]
        material = data.find("mid=")

    material = data.find("<material ")
    while material != -1:
        data= data[:material + 3] + "terial id" + data[material+12:]
        material = data.find("<mat")


    file.seek(0)
    file.truncate()
    file.write(data)
    file.close()
    return

