fp=open('note.txt','w')#打开文件 w--> write
print('hello world', file=fp)
fp.close()#关闭文件