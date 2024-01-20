class person():
    def __init__(self,name):
        self.setname(name)
    def setname(self,value):
        if isinstance(value,str) and len(value.strip())>0:
            self._name=value.strip()
        else:
            raise ValueError('name must be non empty string')
    def getname(self):
        return self._name
p=person('alex')
# print(p.getname())
try:
    person('george')
except ValueError as ex:
    print(ex)
# p=person('')
print(p.getname())


