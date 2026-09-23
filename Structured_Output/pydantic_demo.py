from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'Default' #default value
    age: Optional[int] = None  #setting optional values, require default value
    email: EmailStr  #built-in validation in pydantic
    cgpa: float = Field(gt=0, lt=10, default=5, description='represents cgpa')  #Field Function -> default values, constraints, descriptions, regex

#it performs data validation as well, try to change 'Ishan' to 7 and see
new_student1 = {'name': 'Ishan', 'email':'ishan9411@gmail.com'}
new_student2 = {'age': '32'} #pydantic is smart enough to understand and explicitly convert this to integer -> type coercing

student1 = Student(**new_student1)

print(student1)

student1_dict = dict(student1)  #can create dict object using pydantic object

print(student1_dict['age'])

student1_json = student1.model_dump_json()  #can create json object through pydantic

print(student1_json)