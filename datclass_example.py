from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p1 = Person("Patrick", 42)

print (p1)