

#---------------------------------------------------
#------- Built in Function 7---------
#--------------------------------------------------
# enumerate()
# help()
# reversed()
#--------------------------------------------------



# enumerate(iterable , start=0)

mySkills = ["Html" , "Css" , "Js" , "PHP"]

mySkillsWithCounter = enumerate(mySkills , 20) # (20, 'Html') , (21, 'Css') , (22, 'Js') , (23, 'PHP')
print(type(mySkillsWithCounter )) # <class 'enumerate'>

for counter, skill  in mySkillsWithCounter :
    print(f"{counter} - {skill}") 

# 20 - Html
# 21 - Css
# 22 - Js
# 23 - PHP



print("-" * 50) # --------------------------------------------------


# help()

print(help(print))



print("-" * 50) # --------------------------------------------------

# reversed(iterable)


myString = "Salar"

for letter in reversed(myString) :
    print(letter) 
# r
# a
# l
# a
# S



print("-" * 50) # --------------------------------------------------



mySkills = ["Html" , "Css" , "Js" , "PHP"]

for skill in reversed(mySkills) :
    print(skill) 

# PHP
# Js
# Css
# Html




