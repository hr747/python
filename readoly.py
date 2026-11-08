class user:
    def __init__(self, name, age, money):
        self._name = name
        self._age = age
        self._money = money
# gretter without any setter in readonly attribute 
    @property
    def age(self):
        return self._age

    # setter

    @salary.setter
    def  salary (self,vali):
        if vali<0:
            return 'emty'
        self._money+=vali
        


samsu = user('kopa', 21, 500)
# print(samsu.age())

print(samsu.age)
print(samsu.salary)
samsu.salary=500
print(samsu.salary)