#functions
#function is a collection of code that does a specific task

#when python sees "def" knows this is a function
#def always need a name
#good practices is to use a name with or without _


#sayhi(): means
#its going to tell python that what comes next it's what it is in the function 
#and it needs to be indented

def sayhi(name, age):
    print("Hello" " " + name + ", you are " + age)
#you need to execute the code, so you need to call the function

#FLOW
#funtion keeps the flow
# print("top")
# #calling the function
# # sayhi()
# print("bottom")

#we use () to tell the function to run when only has some parameters in it
#so, when we sayhi(name) when we call the function, we always have to say it's name

sayhi("Alex", "35")
sayhi("Adina", "32")