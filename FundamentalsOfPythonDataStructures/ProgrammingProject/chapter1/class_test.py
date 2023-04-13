class class_name:
    class_var = 'I am class variable'

    @classmethod
    def func1(cls):
        print(cls.class_var)

    
if __name__ == "__main__":

    class_inst = class_name()
    class_inst.func1()