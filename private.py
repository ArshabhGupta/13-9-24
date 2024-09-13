class MyClass:
    __privatevar = 27
    def __privatemeth(self):
        print("This is in the private variable")
    def hello(self):
        print(MyClass.__privatevar)

obj = MyClass()
obj.hello()
obj.__privatemeth