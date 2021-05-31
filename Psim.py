#"On my honor, I have neither given nor received unauthorized aid on this assignment”
INM = []
INB = []
AIB = []
LIB = []
ADB = []
REB = []
RGF = {}
DAM = {}
c = 1
d = True
for element in open("instructions.txt","r").readlines():
    INM.append(element.strip('<>\n').split(','))
for element in open("registers.txt","r").readlines():
    (key,val) = element.strip("'<>\n'").split(',')
    RGF[(key)]=int(val)
for element in open("datamemory.txt","r").readlines():
    (key,val) = element.strip("'<>\n'").split(',')
    DAM[(key)] = int(val)
def write_to_file(step):
    if d is True:
        f = open("simulation.txt", "w")
        f.write("STEP "+str(step)+":\n")
    if d is False:
        f= open("simulation.txt","a")
        f.write("\n\nSTEP "+str(step)+":\n")
    if INM:
        line1="INM:"
        for i in INM:
            p = ('<'+','.join(i)+'>')
            line1=line1+p+','
        line1=line1[:-1]
        f.write(line1)
    if not INM:
        f.write("INM:")
    if INB:
        line2=""
        for item in INB:
            line2=line2+"%s"%item+','
        line2="\nINB:<"+line2[:-1]+">"
        f.writelines(line2)
    if not INB:
        f.write("\nINB:")
    if AIB:
        line3=""
        for item in AIB:
            line3=line3+"%s"%item+','
        line3="\nAIB:<"+line3[:-1]+">"
        f.writelines(line3)
    if not AIB:
        f.write("\nAIB:")
    if LIB:
        line4=""
        for item in LIB:
            line4=line4+"%s"%item+','
        line4="\nLIB:<"+line4[:-1]+">"
        f.writelines(line4)
    if not LIB:
        f.write("\nLIB:")
    if ADB:
        line5=""
        for item in ADB:
            line5=line5+"%s"%item+','
        line5="\nADB:<"+line5[:-1]+">"
        f.writelines(line5)
    if not ADB:
        f.write("\nADB:")
    if REB:
        line6=""
        if len(REB) == 2:
            for item in REB:
                line6=line6+"%s"%item+','
            line6="\nREB:<"+line6[:-1]+">"
            f.writelines(line6)
        else:
            ls1=''
            ls2=''
            h=[REB[0],REB[1]]
            j=[REB[2],REB[3]]
            for item in h:
                ls1=ls1+"%s"%item+','
            ls1 = "<" + ls1[:-1] + ">"
            for item in j:
                ls2=ls2+"%s"%item+','
            ls2 = "<" + ls2[:-1] + ">"
            line6 ="\nREB:"+ls1+','+ls2
            f.writelines(line6)
    if not REB:
        f.write("\nREB:")
    if RGF:
        line7=""
        for key, value in RGF.items():
            line7=line7+"<"+str(key)+","+str(value)+">,"
        line7="\nRGF:"+line7[:-1]
        f.writelines(line7)
    if not RGF:
        f.write("\nRGF:")
    if DAM:
        line8=""
        for key, value in DAM.items():
            line8=line8+"<"+str(key)+","+str(value)+">,"
        line8="\nDAM:"+line8[:-1]
        f.writelines(line8)
        f.close()
    if not DAM:
        f.write("\nDAM:")
        f.close()
write_to_file(0)
d = False
while INM or INB or AIB or LIB or ADB or REB:
    if REB:
        RGF[REB[0]]=REB[1]
        REB=REB[2:]
    if ADB:
        REB=REB+[ADB[0],DAM[str(ADB[1])]]
        ADB=ADB[2:]
    if LIB:
        ADB=ADB+[LIB[1],LIB[2]+LIB[3]]
        LIB=LIB[4:]
    if AIB:
        if AIB[0] == 'ADD':
            REB=REB+[AIB[1],AIB[2]+AIB[3]]
            AIB=AIB[4:]
        elif AIB[0] == 'SUB':
            REB = REB + [AIB[1], abs(AIB[2] - AIB[3])]
            AIB = AIB[4:]
        elif AIB[0] == 'OR':
            REB=REB+[AIB[1],AIB[2]|AIB[3]]
            AIB=AIB[4:]
        elif AIB[0] == 'AND':
            REB = REB + [AIB[1], AIB[2] & AIB[3]]
            AIB = AIB[4:]
    if INB:
        if INB[0] == "LD":
            LIB=LIB+INB
            INB=INB[4:]
        elif INB[0] == "ADD"or"SUB"or"OR"or"AND":
            AIB = AIB + INB
            INB = INB[4:]
    if INM:
        INB=INB+[INM[0][0],INM[0][1],RGF[INM[0][2]],RGF[INM[0][3]]]
        INM=INM[1:]
    write_to_file(c)
    c += 1