'''class with methods'''

class person:
    name="peter"
    address="tokyo"
    age=46
    
    #method initialization
    '''by default:self'''
    def printobj(self):
        print(f"The name is {self.name}")
    
boy=person()
print(f"name        : {boy.name}")
print(f"address     : {boy.address}")
print(f"age         : {boy.age}")
boy.printobj()