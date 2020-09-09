class agenda:
    def __init__(self):
        self.lista = []
    def insert_name(self,nom):
        self.name = nom
    def insert_num(self,num):
        self.num = num
    def insert_email(self,email):
        self.email = email
    def get_name(self):
        return self.name
    def get_num(self):
        return self.num
    def insert_lista(self,ele):
        self.lista.append(ele)

obj = agenda()
obj.insert_name('teste')
obj.insert_num(123)
obj.insert_email('baodemaisdaconta@gmail.com')
print(obj.get_name(),obj.get_num(),obj.email)
obj.insert_lista(1)
print(obj.lista)
obj.insert_lista(2)
print(obj.lista)
obj.insert_lista(3)
print(obj.lista)

