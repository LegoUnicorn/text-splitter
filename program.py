from distutils.log import error
while True:
    try:
        fileName = input("File name without file extension (txt): ")
        split = input("Split by how much (int): ")
        newFile = fileName + "_splitby_" + split
        fileName = fileName + ".txt"

        f = open(fileName, 'r')
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

        break
            
    except:
        print("Error. Check your typing.")
