from random import randint

name = input("请输入你的名字：")

f = open("game.txt")
lines = f.readlines()
f.close()

scores = {}
for line in lines:
    s = line.split()
    scores[s[0]] = s[1:]
score = scores.get(name)
if score is None:
    score = [0,0,0]

game_times = int(score[0])  #游戏次数
min_times = int(score[1])   #最快猜中答案轮数
total_times = int(score[2]) #总共游戏轮数

if(game_times > 0):
    avg_times = float(total_times) /game_times #平均游戏轮数
else:
    avg_times = 0

print("%s,你已经玩了%d次，最快%d轮猜中答案，平均%.2f轮猜中答案" %
      (name,game_times,min_times,avg_times))

#游戏内容
print("Guess a num between 0 and 99?")
current_times = 0
_total_times = total_times
random_num = randint(0,100)
flag = False
while(flag == False):
    current_times += 1      #当前游戏轮数+1
    _total_times += 1    #总共游戏轮数+1
    input_num = int(input())
    if(input_num > random_num):
        print("The num you guess is too big!")
    elif(input_num < random_num):
        print("The num you guess is too small!")
    else:
        flag = True
        print("Bingo!")

#记录游戏

_game_times = game_times + 1
if(min_times == 0 or min_times > current_times):
    _min_times = current_times
else:
    _min_times = min_times

scores[name] = [str(_game_times),str(_min_times),str(_total_times)]
result = ''
for n in scores:
    line = n + " " + " ".join(scores[n]) + "\n"
    result += line
    
save_game = open("game.txt","w")
save_game.write(result)
save_game.close()
