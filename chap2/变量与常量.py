#变量名=value
luck_num=7
print(type(luck_num))
#可以赋不同的值 修改变量的类型
luck_num='11'
#在python中允许多个变量指向同一个值
no=num=1024
print(id(no),id(num))#id函数可以查看对象的内存地址  2704899351152 2704899351152
#常量 可以改 但不要改
PI=3.14