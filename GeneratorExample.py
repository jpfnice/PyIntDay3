import random

random.seed(1)

def values(number):
    result=[]
    for e in range(number):
        result.append(random.randint(0,100))
    return result

def valuesAsGenerator(number):
    for e in range(number):
        yield random.randint(0,100)

# range() is implemented as a generator    
print("Use of a normal function")
for e in values(300):
    if e > 95:
        break
    print(e)
    
print("Use of a generator")

for e in valuesAsGenerator(300):
    if e > 95:
        break
    print(e)
    
result=values(30)
print(result, type(result))

result=set(valuesAsGenerator(30))
print(result, type(result))    
