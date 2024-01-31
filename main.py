class ForbiddenBase:
    pass

class MyMeta(type):
    def __init_subclass__(cls, **kwargs):
        forbidden_bases = getattr(cls, 'forbidden_bases', [])
        for base in forbidden_bases:
            if issubclass(cls, base):
                raise TypeError(f"Class {cls.__name__} cannot inherit from {base.__name__}.")

class MyClassA(ForbiddenBase, metaclass=MyMeta):
    pass

class MyClassB(metaclass=MyMeta):
    pass

class MyClassC(MyClassB):
    pass

class MyClassD(MyClassA):
    pass