# you can put anything in a list (strings, boolean, integers)
friends = ["Alex", "Adina", "Silvia", "oscar", "benji"]

#assign an index position to something
friends[0]="Silvia"

#print index positions
# print(friends[0])
# print(friends[1:3])


#
#list functionalities
# 
# 
lucky_numbers = ["4","7","8","12", "15"]
friends = ["Alex", "Adina", "Silvia", "oscar", "benji"]

#include another list to this list
friends.extend(lucky_numbers)

#append another item to the list
friends.append("Name")

#append another item to the list with a specific index position
friends.insert(1, "Nicu")

#remove an item from the list
friends.remove("Name")

#clear all the list
#friends.clear()

#removes the last elemnt from the list
#friends.pop()

#sort list alphabetically
friends.sort()
print(friends)

#sort list - reversed
friends.reverse()

#copy a list
friends2 = friends.copy()

print(friends2)


print("stringul Adina are index position - " + str(friends.index("Adina")))

print("De cate ori apare Alex - " + str(friends.count("Alex")))



