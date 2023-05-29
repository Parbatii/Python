''' Basic OOP concept in python
    Basic 'Class&Object'
'''

#Class Declaration
class person:
    name="Bob"
    address="Toronto"
    age=27
    email="bobby2@gmail.com"
    
#Object Declaration
bob=person()
print(f"Name        : {bob.name}")
print(f"address     : {bob.address}")
print(f"age         : {bob.age}")
print(f"email       : {bob.email}")