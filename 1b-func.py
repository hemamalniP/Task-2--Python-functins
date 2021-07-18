class str1():
    def _init_(self):
        self.string=""
    def get(self):
        self.string=input()
    def put(self):
        print(self.string.upper())

obj=str1()
obj.get()
obj.put() 
