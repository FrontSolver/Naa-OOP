# class Calculator: 
#     def toplama(self):
#         print(a + b)
     
#     def cixma(self):
#         print(a - b)
        
#     def vurma(self):
#         print(a * b)
        
#     def bolme(self):
#         print(a / b)
        
# a = int(input('Ilk reqemini daxil et a kisi: '));
# b = int(input('Ikinci reqemini daxil et a kisi: '))

# obj = Calculator()
# choice = 1
# while choice != 0:
#     print("1. Toplama")
#     print("2. Cixma")
#     print("3. Vurma")
#     print("4. Bolme")
#     choice = int(input("Seciminizi daxil edin: "))
#     if choice == 1:
#         print(obj.toplama())
#     elif choice == 2:
#         print(obj.cixma())
#     elif choice == 3:
#         print(obj.vurma())
#     elif choice == 4:
#         print(obj.bolme())
#     else:
#         print('Zehmet olmasa kecerli reqem daxil edin')

# class Calculator:
#     def toplama(self):
#         print(a + b)
#     def cixma(self):
#         print(a - b)
#     def vurma(self):
#         print(a * b)
#     def bolme(self):
#         print(a / b)

# a = int(input('Ilk reqemini daxil et a kisi: '))
# b= int(input("Ikinci reqemini daxil et a kisi: "))

# obj = Calculator()
# choice = 1
# while choice != 0:
#     print('1. Toplama')
#     print('2. Cixma')
#     print('3. Vurma')
#     print('4. Bolme')
#     choice = int(input('Secimini daxil et: '))
#     if choice == 1:
#         print(obj.toplama())
#     if choice == 2:
#         print(obj.cixma())
#     if choice == 3:
#         print(obj.vurma())
#     if choice == 4:
#         print(obj.bolme())
#     else:
#         print('Duzgun secim daxil et')

class Calculator():
    def toplama(self):
        print(a + b)
    def cixma(self):
        print(a - b)
    def vurma(self):
        print(a * b)
    def vurma(self):
        print(a / b)

a = int(input('Ilk secimini daxil et: '))
b = int(input('Ikinci secminizi daxil et: '))

obj = Calculator()

choice = 1
while choice != 0:
    print('1. Toplama')
    print('2. Cixma')
    print('3. Vurma')
    print('4. Bolme')
    choice = int(input('Zehmet olmasa duzgun secim daxil edin: '))
    if choice == 1:
        print(obj.toplama())
    elif choice == 2:
        print(obj.cixma())
    elif choice == 3:
        print(obj.vurma())
    elif choice == 4:
        print(obj.bolme())
    else:
        print('Duzgun secim daxil et')