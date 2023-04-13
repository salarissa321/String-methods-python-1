

# --------------------
# Strings Methods
# ----------------------------


#split()  rsplit()

a = " I Love Python and PHP and mySQL"
print(a.split())

b = " I-Love-Python-and-PHP-and-mySQl"
print(b.split("-"))


c = " I-Love-Python-and-PHP-and-mySQL"
print(c.split("-" , 3))

d = " I-Love-Python-and-PHP-and-mySQL"
print(d.rsplit("-" , 3))

# Center()

s= "Salar"
print(s.center(9))
print(s.center(9 , "#"))
print(s.center(15 , "!"))

#count()

f = " I Love Python and PHP because PHP is Easy"
print(f.count("PHP"))
print(f.count("PHP" ,0 ,35))

# swapcase()
p = " I love python"
d = " i LOVE pYTHON"

print(p.swapcase())
print(d.swapcase())

# Startswith
p = "I love Python"
print(p.startswith("I"))
print(p.startswith("s"))
print(p.startswith("p" , 6, 12))


# Endwith
o = "I love Python"
print(o.endswith("n"))
print(o.endswith("s"))
print(o.endswith("e" , 2, 6))



