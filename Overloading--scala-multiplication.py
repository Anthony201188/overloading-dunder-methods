""" Exercise( Overloading * for Scalar Multiplication):
You can multiplay a number to a vector: (x,y) * c = (x*c, y*c)
use the dunder method __ add__ to add a scalar (number) to an instance of Vector2d (see notes) """
 
 # Task-1

class Vector2d:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Vector2d {(self.x, self.y)}"
    
    def __mul__(self, number):
        return (self.x * number, self.y* number)
    
    def __rmul__(self, number):
        return (self.y * number, self.x * number)
    
    def __neg__(self,):
        return (-self.x, -self.y)
    
    def __add__(self):
        return (self.x +self.x2)


        


    
    
        



""" vec2d = Vector2d(1,1)
new_vec2d = vec2d * 10
new_vec2d2 = vec2d * 100
new_vec2d = 10 * vec2d
new_vec2d2 = 100 * vec2d
print(new_vec2d) # --> Vector2d (10, 10)
print(new_vec2d2) # --> Vector2d (10, 10)
print("========")

# Task-2

new_vec2d = vec2d * 10
new_vec2d2 = vec2d * 100
new_vec2d = 10 * vec2d
new_vec2d2 = 100 * vec2d
print(new_vec2d) # --> Vector2d (10, 10)
print(new_vec2d2) # --> Vector2d (10, 10)
print("========")


# Task-3
neg_vec = -vec2d
print(neg_vec)
print("========") """


# Task-4

class Vector2d2:
    def __init__(self, lst):
        self.lst = lst
        
    
    def __str__(self) -> str:
        return f"Vector2d2,{self.lst}"

    def __add__(self, other):
       return [x + y for x, y in zip(self.lst, other.lst)] # zip both lists together and add pairs of elemtents together in a new list
    
   



v1 = Vector2d2([3,4,5])
v2 = Vector2d2([6,7,8])
v3 = v1 + v2
print(v1)
print(v2)
print(v3)