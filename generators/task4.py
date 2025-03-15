class square:
    def __iter__(self):
        self.a = int(input())
        self.b = int(input())
        self.x = self.a
        return self

    def __next__(self):
        if self.x <= self.b:
            y = self.x 
            self.x += 1
            return y * y
        else:
            raise StopIteration
        
myclass = square()

for x in myclass:
    print(x)