# # Stirngs are immutable mean strings never chnage for example



# # a="faizan "
# # print(a.upper())
 



# #  rstrip use for remove unwanted charachters like for example just leading charchter not starting 

# Name="2676Fizan Ahmad2676"
# # print(Name.rstrip("2676"))

# # Name = "Faizan_Ahmad2676"
# # # Name = Name.removesuffix("2676")
# # print(Name)

# # Name = "Faizan_Ahmad2676"
# # print(len(Name))
# # Final_name= Name[0:-4]
# # print("this is the exact name",Final_name)



# print (Name.replace("2676","Shahzad Garments"))



# # Capitalie method use for first letter capital and rest small
# print(Name.split("2676"))
# print("**********************************************************************************************")

c="farhAN"
# print(c.capitalize())


# Center 

print(len(c))
print(c.center(50,"*"))


# count is to count the number of occurence in the string % and also this is K sensative 
  


d= c.lower()
e=c.upper()
f=c.capitalize()

print(d.count("a"))
print(e.count("A"))
print(f.count("F"))




# Endwih is use to check the string end with the specific charachter or not
print(c.endswith("N"))     #>>>So it return answer in boolean value true or false

# Find() is use to find the index of the specific charachter in the string and also this is K sensative
r="He,s name is give by yadav pandey which is the owner of this shop"
print(r.find("is"))     #>>>So it return the index of the charachter if




# Index() is also use to find the index of the specific charachter in the string but if the charachter is not found then it will give error
print(r.index("is"))     #>>>So it return the index of the charachter if


# isalnum() is use to check the string is alphanumeric or not if the string contain only charachter and number then it will return true otherwise false
print(c)
t="F@1zan"
print(c.isalnum())     #>>>So it return answer in boolean value true or false
print(t.isalnum())     #>>>So it return answer in boolean value true or false



# isalpha() is use to check the string is alphabetic or not if the string contain only charachter then it will return true otherwise false
print(c.isalpha())      #>>>So it return answer in boolean value true or false          
print(t.isalpha())      #>>>So it return answer in boolean value true or false


# islower() is use to check the string is in lower case or not if the string contain only small charachter then it will return true otherwise false
print(c)
y="faizan"
print(c.islower())      #>>>So it return answer in boolean value true or false
print(y.islower())      #>>>So it return answer in boolean value true or false



# printable() is use to check the string is printable or not if the string contain only charachter and number then it will return true otherwise false

w="faizan\n"
print(w)
print(w.isprintable())      #>>>So it return answer in boolean value true or false



# isspace() is use to check the string is space or not if the string contain only space then it will return true otherwise false    
s=" lio  "  
print(s.isspace())      #>>>So it return answer in boolean value true or false





# istitle() is use to check the string is in title case or not if the string contain only first letter capital and rest small then it will return true otherwise false
c="Faizan"
 
print(c.istitle())      #>>>So it return answer in boolean value true or false




# isupper() is use to check the string is in upper case or not if the string contain only capital charachter then it will return true otherwise false
c="FAIZAN"
print(c.isupper())      #>>>So it return answer in boolean value true or false


# startswith() is use to check the string start with the specific charachter or not
print(c.startswith("F"))     #>>>So it return answer in boolean value true or false 





# swapcase() is use to swap the case of the string if the string contain only small charachter then it will return capital charachter and if the string contain only capital charachter then it will return small charachter
c="fAizan"
print(c.swapcase())      #>>>So it return the string with swapped case



# title() is use to convert the string in title case if the string contain only first letter capital and rest small then it will return true otherwise false
c="faizan ahmad"
print(c.title())      #>>>So it return the string in title case make every letter first letter captial 