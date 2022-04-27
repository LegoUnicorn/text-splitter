from distutils.log import error

def openFile():
    global fileName
    global fullFileName
    global f
    fileName = input("File name without file extension (txt): ")
    fullFileName = fileName + ".txt"
    f = open(fullFileName, 'r')

def splitFunc():
    openFile()
    split = input("Split by how much (int): ")

    newFile = fileName + "_splitby_" + split
    wr = open(newFile, 'x')

    nl = f.readline()
    c = 1
    c2 = 0

    while nl != '':  
        if c == int(split):
            wr.write(nl)
            c = 1
        if c2 % 1000 == 0:
            print("Scanned " + str(c2) + "lines.")
        c += 1
        c2 += 1
        nl = f.readline()
    print("Scanned " + str(c2) + "lines.")
    print("New file created called " + newFile + ".")

    f.close()
    wr.close()

def dedupFunc():
    openFile()

    newFile = fileName + "_dedupped"
    wr = open(newFile, 'x')
    tempList = []

    nl = f.readline()
    while nl != "":
        tempList.append(nl)
        nl = f.readline()
    tempList = list(dict.fromkeys(tempList))

    f.close()
    wr.close()


while True:
    try:
        run = input("Select Function (split, dedup): ")
        if run == "split":
            splitFunc()
        elif run == "dedup":
            dedupFunc()
        break
            
    except:
        print("Error. Check your typing.")
