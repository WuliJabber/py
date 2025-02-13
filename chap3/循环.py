for i in 'hello':
    print(i)

#range函数用于生成一个【m,n)的整数序列，包含m不包含n
for i in range(0,9):
    # print(i)
    if i%2==0:
        print(i,'是偶数')
sum=0
for i in range(0,11):
    sum+=i
print(sum)

# while
ans=input('上课嘛？')
while ans=='y':
    print('好好上课')
    ans=input('还上嘛？')