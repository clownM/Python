f = open('readFile.txt')
data = f.read()
print(data)
f.close()
f_write = open("writeFile.txt","w")
f_write.write(data)
f_write.close()

