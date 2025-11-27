numbers1=[1,4,7,9,0,6,10]
numbers2=[20,13,8,9,3,5,6]
result=map(lambda x, y: x+y, numbers1, numbers2)
print("Addition of two lists")
print(list(result))
#using map
nums=[20,56,7,9,34,67,89,0]
def sq(n):
    return n*n
square=list(map(sq, nums))
print("Square of numbers in list")
print(square)