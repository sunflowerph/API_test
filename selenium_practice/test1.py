'''a=[2,1,4,5,6,3,1,8,9,0,0,6]
b=len(a)-1
while b>=0:
    for i in range(b):
        if a[i]<a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    b=b-1


print(a)'''


'''class A(n):
    def __init__(self):
        self.n = n

    def f(self,n):
        if n == 1:
            return 1
        else:
            return(f(n-1)*n)'''


class A(object):
    def __init__(self,n):
        self.n=n

    def f(self):
        if self.n == 1:
            return 1
        else:
            return f(self.n-1)+self.n
a=A(8)
print(a.f())

