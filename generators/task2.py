class nums:
    def __init__(self,n):
        self.n = n
    def __iter__(self):
        self.a = 0
        return self
    
    def __next__(self):
        if(self.a % 2 == 0):
            if(self.a > self.n):
                raise StopIteration
            else:
                x = self.a
                self.a += 2
                return x

n = int(input())        
myclass = nums(n)

cnt = 0
cnt1 = 0
for x in myclass:
    cnt += 1

for x in myclass:
    cnt1 += 1
    if cnt1 == cnt:
        print(x)
    else:
        print(x, end=", ")