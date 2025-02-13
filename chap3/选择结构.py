#if else
name='hgd'
#用于去掉字符串最外侧的引号
if name=='hgd':
    print('hgd')
number=eval(input('请输入中将号码：'))
if number==123:
    print('中将了')

x=input('输入字符串')
if x:
    print('非空字符串')
if not x:
    print('空字符串')
#如果if语句只有一句 可以写在冒号后面
if x:print('1122')
else:print('3344')

num=eval(input('输入一个数字'))
if num>0:
    print('1123')
elif num<0:
    print('gf')