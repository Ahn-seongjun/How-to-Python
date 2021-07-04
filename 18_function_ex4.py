# 18_function_ex4.py

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

x=9
y=3
print("%d+%d=%d"%(x,y,add(x,y)))
print("%d-%d=%d"%(x,y,sub(x,y)))
print("%d*%d=%d"%(x,y,mul(x,y)))
print("%d/%d=%d"%(x,y,div(x,y)))