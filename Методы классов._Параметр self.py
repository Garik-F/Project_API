class Point:
    color = "red"
    circle = 3
    def set_coords(self, x, y):
        self.x = x
        self.y = y
    def get_coords(self):
        return (self.x, self.y)
pt = Point()
pt2 = Point()
pt.set_coords(4, 5)
pt2.set_coords(10, 20)
f = getattr(pt, 'get_coords')
print(pt.__dict__)
print(pt2.__dict__)
print(pt.get_coords())
print(f)