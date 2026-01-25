class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Vector(new_x, new_y)
        else:
            raise TypeError("Unsupported type for '+'")
        
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __del__(self):
        print(f"Deleted: Vector({self.x}, {self.y})")
        

# vector_a = Vector(4, 5)
# vector_b = Vector(-14, -15)
# new_vec = vector_a + vector_b
# print(new_vec)
# del new_vec

total_dunder = []

for m in dir(object):
    if m.startswith("__") and m.endswith("__"):
        total_dunder.append(m)
        print(m)

print(len(total_dunder))
