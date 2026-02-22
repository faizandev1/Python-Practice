# Anything that close in single or double quotes is a string. You can use either single or double quotes to create a string, but you must use the same type of quotes at the beginning and end of the string.


name="Faizan"
anothername="Chaudhry"
anothername2='Mahmood'




# for example if we wan to show the double quotes also that why we use single quote 


print('My name is "Faizan"')


# Also if u wanna show someone chat like each and every message than u use tripe stting '''


print('''Faizan:Hi
      
      Mah:HEY
      Faizan:How are you?
        Mah:I'm good, how about you?
      
      
      
      
      
      ''')


# Index


st="Faizan"
print(st[0:3]) #>>For index find out 
print(len(st)) #>>for sting lenght find out 



print ("if we are using a for loop to print string name ")
for character in st:
    print(character)