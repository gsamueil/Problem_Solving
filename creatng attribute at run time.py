


from types import MethodType
class person:
    def __init__(self,name):
        self.name=name
    
    def regisrer_do_work(self,func):
        setattr(self,'_do_work',MethodType(func,self))
    
    def do_work(self):
        do_work_method=getattr(self,'_do_work',None)
        if do_work_method:
            return do_work_method()
        else:
            raise AttributeError("you must first register a do_work method.")


math_teacher =person('Eric')
english_teacher=person('john')
# print(math_teacher,english_teacher)
# print(math_teacher.name,english_teacher.name)
# print(math_teacher.do_work(),english_teacher.do_work())
def work_math(self):
    return f'{self.name} will teach differentials today.'
print(math_teacher.regisrer_do_work(work_math))
print(math_teacher.__dict__)
print(math_teacher.do_work())
