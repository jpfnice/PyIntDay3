# mypy (conda install mypy or pip install mypy)

def f(a: str, b: int=2) -> str:
    if isinstance(a,str) and isinstance(b,int):
        return a * b
    else:
        raise Exception()

from typing import List

def mult(data: List[int]) -> int:
    total=data[0]
    for e in data[1:]:
        total *=e
    return total

result=f("xx",10)

print(result)

d=[4,3,2,1]

print(mult(d))
print(mult(3.4))