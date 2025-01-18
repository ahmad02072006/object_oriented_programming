x=10
print(type(x))

def say_hello(name):
    print('Hello',name)
say_hello("Ahmad")
print(type(say_hello))

class Talaba:
    def __init__(self,ism,familya,tyil):#bular xususiyat emas,balki argumentlar
        self.name=ism # name bu xususiyat , ism esa argument va ikkalasini bog'layabmiz
        self.surname=familya# surname xususiyat , familya argument
        self.byear=tyil# byear xususiyat , tyil argument

talaba1=Talaba('Ahmad','Ochilov',2006)

print(talaba1.name)
print(f"{talaba1.surname} {talaba1.name}.{talaba1.byear} yilda tug'ilgan")

talaba2=Talaba('Abbos',"Xidirov",2007)
talaba3=Talaba('Jahon','Bozorboyev',2005)

print(talaba2.surname)
print(talaba3.byear)

class Talaba:
    def __init__(self, ism, familya, tyil):
        self.name = ism
        self.surname = familya
        self.byear = tyil

    def introduce(self):
        print(f'{self.surname} {self.name}.Born in {self.byear}')
    def get_name(self):
        print(f"{self.name} {self.surname}")
    def get_age(self,year):
        print(f'{year-self.byear} years old')
    def describe(self):
        pass
    def get_email(self):
        pass
talaba1=Talaba('Ahmad','Ochilov',2006)
talaba2=Talaba('Abbos',"Xidirov",2007)
talaba3=Talaba('Jahon','Bozorboyev',2005)

talaba1.introduce()
talaba3.introduce()

talaba4=Talaba('Jasur','Olimov',2002)

talaba4.introduce()
talaba1.get_name()
talaba3.get_age(2024)
talaba2.get_name()
talaba1.get_age(2020)

class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.name= ism
        self.surname = familiya
        self.byear = tyil
        self.bosqich=1

    def get_info(self):
        print(f"{self.surname} {self.name}.{self.bosqich}-bosqich talabasi")
    def set_bosqich(self,bosqich):
        self.bosqich=bosqich
    def get_bosqich(self):
        print(self.bosqich)
    def update_bosqich(self):
        self.bosqich+=1

talaba1=Talaba('Ahmad','Ochilov',2006)
talaba2=Talaba('Abbos',"Xidirov",2007)
talaba3=Talaba('Jahon','Bozorboyev',2005)
talaba1.get_info()

talaba1.set_bosqich(3)
talaba1.get_bosqich()
talaba2.get_bosqich()
talaba1.get_info()

talaba2.get_bosqich()
talaba2.update_bosqich()
talaba2.get_info()

class Fan:
    def __init__(self,nomi):
        self.nom=nomi
        self.talabalar_soni=0 #talabar_soni yam xususiyatga kiradi
        self.talabalar=[]

    def add_students(self,talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni+=1
    def get_talabalar_soni(self):
        print(self.talabalar_soni)
    def get_students(self):
        return [talaba.get_info() for talaba in self.talabalar]
# get_info boshqa klassdan yaratilgan obyek uchun ya'ni talaba1 va talaba2 uchun
matematika=Fan('Oliy Matematika')

talaba1 = Talaba("Alijon","Valiyev",2000)
talaba2 = Talaba("Hasan","Alimov",2001)

matematika.add_students(talaba1)
matematika.add_students(talaba2)

matematika.get_talabalar_soni()
mat_talabalar=matematika.get_students()
mat_talabalar

z=dir(Talaba)
print(z)
dir(talaba1)

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(Talaba))
print(see_methods(talaba2))

print(talaba1.__dict__)
print(talaba3.__dict__)

print(talaba2.__dict__.keys())


class Car:
    def __init__(self, make="Toyota", model="Corolla", year=2020):
        self.make=make
        self.model=model
        self.year=year

    def get_make(self):
        print(self.make)
    def get_model(self):
        print(f"it's {self.model} model")
    def get_year(self):
        print(f"It was made in {self.year}")
    def set_year(self,nyear):
        self.year=nyear
car=Car()
car.get_model()
car.get_year()
car.get_make()

car.set_year(2019)
car.get_year()

car2=Car('GM','Malibu',2022)
car2.get_make()
car2.get_model()
car.get_year()

print(car.__dict__)
print(car.__dict__.values())
print(car2.__dict__.keys())
































