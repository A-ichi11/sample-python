# generater

l = ["a","b","c","d","e","f","g","h"]

for i in l:
    print(i)
    
print("#####")


def greet():
    yield "a"
    yield "b"
    yield "c"
    
# for g in greet():
#     print(g)
    
g = greet()
print(next(g))
print("###")
print(next(g))
print(next(g))