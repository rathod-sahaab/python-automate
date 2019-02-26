f = open("names.txt")
for namePos in f.readlines() :
    namePos = namePos.strip('\n')
    pos,name = namePos.split(' - ')
    print(namePos,name,pos)


