class ClassRegistry:
    _registry = {}

    @classmethod
    def register(cls, class_name, class_obj):
        cls._registry[class_name] = class_obj

class AutoRegisterMeta(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        ClassRegistry.register(name, cls)

class MyClassA(metaclass=AutoRegisterMeta):
    pass

class MyClassB(metaclass=AutoRegisterMeta):
    pass


print(ClassRegistry._registry)
