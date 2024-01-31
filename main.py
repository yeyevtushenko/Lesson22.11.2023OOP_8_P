class MyMeta(type):
    def __new__(cls, name, base, dct):
        dct['analytics'] = lambda self: dir(self)

        return super().__new__(cls, name, base, dct)


for i in range(1, 3):
    MyClass = MyMeta(f"MyClass{i}", (), {})
    my_class_instance = MyClass()
    print(my_class_instance.analytics())