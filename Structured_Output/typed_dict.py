#Only provides type hint
from typing import TypedDict

class Person(TypedDict):

    name : str
    age : int

new_person: Person = {'name': 'Ishan', 'age': 22}
#new_person: Person = {'name': 'Ishan', 'age': '22'} -> no type validation even "THIS WORKS"

print(new_person)