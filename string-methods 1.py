

# --------------------
# Strings Methods
# ----------------------------


#split()  rsplit()

a = " I Love Python and PHP and mySQL"
print(a.split()) # ['I', 'Love', 'Python', 'and', 'PHP', 'and', 'mySQL']

b = " I-Love-Python-and-PHP-and-mySQl"
print(b.split("-")) # [' I', 'Love', 'Python', 'and', 'PHP', 'and', 'mySQl']


c = " I-Love-Python-and-PHP-and-mySQL"
print(c.split("-" , 3)) # [' I', 'Love', 'Python', 'and-PHP-and-mySQL']

d = " I-Love-Python-and-PHP-and-mySQL"
print(d.rsplit("-" , 3)) # [' I-Love-Python-and', 'PHP', 'and', 'mySQL']

# Center()

s= "Salar"
print(s.center(9)) #   Salar 
print(s.center(9 , "#")) ###Salar##
print(s.center(15 , "!")) # !!!!!Salar!!!!!

#count()

f = " I Love Python and PHP because PHP is Easy"
print(f.count("PHP")) # 2
print(f.count("PHP" ,0 ,35)) # 2

# swapcase()
p = " I love python"
d = " i LOVE pYTHON"

print(p.swapcase()) #  i LOVE PYTHON
print(d.swapcase()) # I love Python

# Startswith
p = "I love Python"
print(p.startswith("I")) # True
print(p.startswith("s")) # False
print(p.startswith("p" , 6, 12)) # False


# Endwith
o = "I love Python"
print(o.endswith("n")) # True
print(o.endswith("s")) # False
print(o.endswith("e" , 2, 6)) # True




