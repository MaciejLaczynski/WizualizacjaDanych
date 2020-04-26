class Point:
    counter = [64]
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def update(self, n):
        self.counter.append(n)

p1 = Point(0,0)
print('p1.counter:', p1.counter)
p2 = Point(2,2)
print('p2.counter:', p2.counter)
p3 = Point(4,4)
print('p3.counter:', p3.counter)

p1.update('p1')
p2.update('p2')
p3.update('p3')
p1.update('p4')

print('punkt1:', p1.counter)
print('punkt2:', p2.counter)
print('punkt3:', p3.counter)
p1.counter.append('Joint')
print('punkt1:', p1.counter)
print('punkt2:', p2.counter)
print('punkt3:', p3.counter)