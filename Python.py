import  pythonpackagetest1
print("hello,这是主函数")
print(pythonpackagetest.printTest2)

def Mysun(l):
  if not l:
    return 0
  else:
    return l[0]+Mysun(l[1:])
  
def sun(L):
	tot = 0
	for x in L:
		if not isinstance(x, list):
			tot += x
		else:
			tot += sumtree(x)
	return tot
