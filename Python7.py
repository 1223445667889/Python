f=open('G:\haha.txt')
content = f.read(12)
print(content)
print("-"*30)
content = f.read()
print(content)
f.close()
