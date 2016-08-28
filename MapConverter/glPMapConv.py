variables= ["r=","b=","g=", "x=", "y=", "z=", "distance=","energy=","specular="]


def updateMap(filePath):
    """"updates old format to new one compatibble with xsd"""
    file= open(filePath, "r+")
    data= file.read()

    light =  data.find("<light ")

    while light!= -1:
        while data[light + 7] == "d":
            light = data.find("<light ", light+1)
            if light== -1:
                return

        value=[None]*9
        for i in range(9):
            Start= data.find(variables[i],
                        light,
                        data.find("/>",light))

            if  Start == -1:
                print("expression: "+ variables[i] + " not found")
                break;

            value[i]= data[ Start+len(variables[i])+1 : data.find("\"", Start+len(variables[i])+2) ]

        #to do rewrite it with %s
        insert= '\t<light distance="' + str(value[6]) + '" energy="'+ value[7] +'">\n' + \
                '\t\t<position x="'+ value[3] + '" y="'+ value[4] +'" z="'+ value[5] +'"/>\n' + \
		        '\t\t<color r="' + value[0] +'" g="'+ value[2]+ '" b="'+ value[1] + '"/>\n' + \
	            '\t</light>\n'

        data=data[:(light-1)] + insert + data[data.find("/>", light)+2:]

        light=data.find("<light ", light+1)

    mId = data.find("mid=")
    while mId != -1:
        data= data[:mId-1] + " material"+ data[mId+3:]
        mId = data.find("mid=")

    material = data.find("<mat material")
    while material != -1:
        data= data[:material + 3] + "terial id" + data[material+13:]
        material = data.find("<mat material")

    object = data.find("<object")
    while object != -1:
        data = data[:object] + "<model" + data[object + 7:]
        object = data.find("</object>")
        data= data[:object-1] + "</model>" + data[object+9:]
        object = data.find("<object")

    file.seek(0)
    file.truncate()
    file.write(data)
    file.close()
    return

