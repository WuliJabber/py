#用于去掉字符串最外侧的引号，并按照python的语句方式执行该字符串
#eval函数经常和input函数一起使用
s='3.14+3'
x=eval(s)
print(x)

age=eval(input('请输入你的年龄：'))
print(age)