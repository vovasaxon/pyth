class Employee():
    __age=int()
    __company=str()

    def __init__(self):
        print('Конструктор базового класса без параметров')

    def __init__(self,age='',company=''):
        self.__age=age
        self.__company=company
        print('Конструктор базового класса')

    def __del__ (self):
        print("Сработал базовый деструктор")

    def set_age(self,age):
        self.__age=age

    def set_company(self,company):
        self.__company=company

    def get_age(self):
        return self.__age

    def get_company(self):
        return self.__company

    def show (self):
        print('Возраст: ', self.__age,'Компания: ', self.__company, end =' ')

    def write(self):
        self.__age= input ('Введите возраст: ')
        self.__company = input('Введите компанию: ')

class Musician(Employee):
    __label=str()

    def __init__(self):
        print('Конструктор класса Musician без параметров')

    def __del__(self):
        print ('Деструктор Musician')

    def __init__(self,age='',company='',label=''):
        print ("Конструктор класса Musician")
        super(Musician, self).__init__(age,company)
        self.__label=label

    def set_label(self,label):
        self.__label=label

    def get_label(self):
        return self.__label

    def show (self):
        super(Musician, self).show()
        print ('Лейбл: ',self.__label, end=' ')

    def write(self):
        super(Musician, self).write()
        self.__label = input('Введите лейбл: ')

class Guitarist (Musician):
    __strings=str()

    def __init__(self):
        print('Конструктор класса Guitarist без параметров')

    def __init__(self,age='',company='',label='',strings=''):
        print('Конструктор класса Guitarist')
        super(Guitarist, self).__init__(age,company,label)
        self.__strings=strings

    def __del__(self):
        print ('Деструктор Guitarist')

    def set_strings(self,strings):
        self.__strings=strings

    def get_strings (self):
        return self.__strings

    def show (self):
        super(Guitarist, self).show()
        print ('Струны: ',self.__strings)

    def write(self):
        super(Guitarist, self).write()
        self.__strings = input('Введите тип струн: ')


a=Employee(24,'Apple')
print(a.get_age())
a.set_age(28)
print(a.get_age())

b=Musician(28,'GladProd', 'Republic')
b.show()
b.set_company('TayRec')
b.show()
b.set_label('RCA')
b.show()

c=Guitarist(56,'BrookRec', 'Motown', 'Nickel')
c.show()
c.set_strings('Nylon')
c.show()
c.set_age(67)
c.show()

#m=Guitarist()
#m.write()
#m.show()

k=Musician()
k.write()
k.show()
