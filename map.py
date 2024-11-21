nums = [1 , 2 , 3 , 4 , 5]
def add(n):
    return n+1
def double(n):
    return n*2

square = list(map(add, nums))
print("square of numbers in list")
print(square)