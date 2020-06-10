#!usr/bin/python3.6

#Run this script to get dictionnaries of a given length

f = open("english.txt")
dico = f.read()
words = dico.split()
f.close()


for i in range(3,8):
    new = open("eng{}.txt".format(str(i)), "w+")
    for word in words:
        if len(word) == i:
            new.write(word+"\n")
    new.close()