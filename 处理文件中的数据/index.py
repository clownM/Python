f = open("score.txt")
lines = f.readlines()
# print(lines)
f.close()

results = []
for line in lines:
    data = line.split()
    #print(data)
    sum = 0
    for score in data[1:]:
        sum += int(score)
    result = '%s\t:%d\n'%(data[0],sum)
    results.append(result)
print(results)

output = open('index.txt','w')
output.writelines(results)
output.close()


