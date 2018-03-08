import math

#圆周率π
pi = math.pi
print(pi)

#自然常数e
e = math.e
print(e)

#数值运算:

#向上取整
print(math.ceil(1.2))

#向下取整
print(math.floor(1.2))

#指数运算,得到x的y次方
print(math.pow(2,4))

#对数运算，默认底为e，使用第二个参数来改变默认底
print(math.log(10))

#平方根
print(math.sqrt(9))

#绝对值
print(math.fabs(-10))

#三角函数(弧度值)
print(math.sin(pi/2))
print(math.cos(pi/3))
print(math.tan(pi/4))
print(math.asin(pi/4))
print(math.acos(pi/4))
print(math.atan(pi/4))
#弧度转角度
#   math.degrees(x)
#角度转弧度
#   math.radians(x)
