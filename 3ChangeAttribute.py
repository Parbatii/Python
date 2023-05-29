'''change attribute'''

class employee:
    name="Peter"

peter=employee()
print(f"Employee1               : {peter.name}")
bob=employee() #declaration of new object
bob.name="Bob" #change name of the new object
print(f"Employee2 (after rename): {bob.name}")