class MyClass:
    def __init__(self,language) -> None:
        self._language=language
    @property
    def get_language(self):
        return self._language
    @set_language.setter
    def set_language(self,value):
        self._language=value
    #property is a  class(type)
    ##constractor has a few parameters:
        #  fget specifies  the function to use to get instance property value
    # x=property()
    # x.setter(set_language)
    # x.getter)get_language
    # language=property(fget=get_language,fset=set_language)


obj=MyClass('java-5')
obj.language="python"
print(obj.language)