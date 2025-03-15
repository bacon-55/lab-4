class square:
    def __iter__(self):
        self.n = int(input())
        self.a = self.n
        return self

    def __next__(self):
        if self.a == 0:
            raise StopIteration
        else:
            x = self.a
            self.a -= 1
            return x
        
myclass = square()

for x in myclass:
    print(x)