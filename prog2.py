def mdc(a,b):
    if b == 0:
        return a
    return mdc(b,a%b)

x = int(input())
y = int(input())
print(mdc(x,y))
