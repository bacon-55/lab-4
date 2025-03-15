class square:
    def __iter__(self):
        self.a = 1
        self.n = int(input())
        return self
    
    def __next__(self):
        if(self.a*self.a <= self.n):
            x = self.a
            self.a += 1
            return x * x
        else:
            raise StopIteration
        
myclass = square()

for x in myclass:
    print(x)