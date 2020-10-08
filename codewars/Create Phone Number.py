#Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
#Example:
#create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
#The returned format must be correct in order to complete this challenge.
#Don't forget the space after the closing parentheses!


#Minu lahendus
def create_phone_number(n):
    str1 = "" #loon tühja stringi
    for i in n[:3]: #võtan listist väärtused kuni teatud kohani
        str1 += str(i) #lisan väärtused tühja stringi ja pärast prindin välja
    str2 = ""
    for i in n[3:6]:
        str2 += str(i)
    str3 = ""
    for i in n[6:10]:
        str3 += str(i)
    print( '(' + str1 +')' + ' ' + str2 + '-' + str3 ) #prindin tulemused välja

#Codewars lahendus
def create_phone_number1(n):
    print( "({}{}{}) {}{}{}-{}{}{}{}".format(*n) )

#Codewars lahendus 2, mille tegin natuke oma käe järgi ümber
def create_phone_number2(n):
    a = ""
    for i in n:
        a += str(i)
    return '({}) {}-{}'.format(a[:3], a[3:6], a[6:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
create_phone_number(nums)
create_phone_number1(nums)
create_phone_number2(nums)
