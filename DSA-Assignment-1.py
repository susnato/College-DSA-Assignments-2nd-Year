### List ###
'''Reverse a List'''

print("Enter the values of the list : ")
list_ = [*map(int, input().split(" "))]
# list_ = [5, 1, 0, 80, 10]
print("The list is : ", list_)
revsresed_list = []
for i in range(1, len(list_)+1):
    revsresed_list.append(list_[-i])
print("The reversed list is : ", revsresed_list)


'''Concat 2 lists index-wise'''
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

print('The 1st list : ', list1)
print('The 2nd list : ', list2)

for i in list2:
    list1.append(i)

print("The concatenated list : ", list1)

'''Turn every item of a list into it's square'''

print("Enter the values of the list : ")
list_ = [*map(int, input().split(" "))]
# list_ = [1, 2, 3, 4, 5]
print("The input list is : ", list_)
for i in range(len(list_)):
    list_[i] = list_[i]**2

print("The output list is : ", list_)

'''Add a item after a specified item'''
print("Enter the values of the list : ")
list_ = [*map(int, input().split(" "))]

print("Enter the item to be added")
item_tba = int(input())

print("Enter the item after which it needed to be added")
item = int(input())
new_lst = []
for i in list_:
    if i == item:
        new_lst.append(i)
        new_lst.append(item_tba)
    else:
        new_lst.append(i)
print("New List : ", new_lst)


'''remove all occurrences of a specific item from a list'''

print("Enter the values of the list : ")
list_ = [*map(int, input().split(" "))]
# list_ = [1, 2, 3, 3, 5, 3]
print("Enter the element to be removed : ")
# item = 3
item = int(input())

print("Main list : ", list_)
try:
    while True:
        list_.remove(item)
except:
    pass
print(f"Value : {item} has been removed from the list !, the new list is : ", list_)

### List ###




### Tuple ###
'''Access value 20 from the tuple'''



'''Unpack the tuple into 4 variables'''
my_tuple = (10, 20, 30, 40)
print("Tuple : ", my_tuple)

var1, var2, var3, var4 = my_tuple[0], my_tuple[1], my_tuple[2], my_tuple[3]
print("The 4 variables are : ", var1, var2, var3, var4)


'''Copy Specific element from one tuple to another'''
tuple1 = (10, 20, 30, 40)
print("Main tuple : ", tuple1)
print("Enter the indexes you want to copy from this tuple")
idxs = [*map(int, input().split(" "))]

tuple2 = []
for idx in idxs:
    tuple2.append(tuple1[idx])
tuple2 = tuple(tuple2)
print("New tuple : ", tuple2)

''' Count the number of occurances of item "x" from a tuple '''
tuple1 = (1, 2, 2, 3)
print("The tuple is : ", tuple1)

print("Enter the item : ")
item = int(input())

count=0
for i in tuple1:
    if i==item:
        count += 1
print(count)

'''Check if all the items are same'''
tuple1 = tuple([*map(int, input().split(" "))])
print("The tuple : ", tuple1)
item_, c = tuple1[0], 0
for i in tuple1:
    if item_!=i:
        print("The Items are not same !")
        c = c+1
if c == 0:
    print("The Items are same !")

### Tuple ###



### Set ###

'''Add a list of elements to a set'''
set_ = {1, 2, 3, 4, 5}
elements = [10, 20, 30]
print("Set : ", set_, "elements to be added : ", elements)

set_ = set_.union(set(elements))
print('New Set : ', set_)

'''get only unique items from two sets'''
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Set 1 : ", set1, "Set 2 : ", set2)
print("Unique items of set 1 :", set1-set2)
print("Unique items of set 2 :", set2-set1)

'''Remove all elements at once'''
set_ = {1, 2, 3, 4, 5}
print("Set : ", set_)
set_.clear()
print("Set After removing all elmenets at once : ", set_)

'''Return a set of elements present in Set A or Set B, but not both'''
setA = {1, 2, 3}
setB = {3, 4, 5}

print("Set A : ", setA, "Set B : ", setB)
print("Set of elements present in Set A or Set B, but not in both : ", (setA-setB).union(setB-setA))

'''Elements in common'''
setA = {1, 2, 3}
setB = {3, 4, 5}

print("Set A : ", setA, "Set B : ", setB)
print('Elements in common : ', setA.intersection(setB))

### Set ###


### Dictionary ###

'''Convert two lists into a dict'''
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print("List 1 : ", l1, "List 2 : ", l2)
dict__ = [(k, v) for k, v in zip(l1, l2)]
print("The dictionary is : ", dict__)

'''Merge two dictionaries into one'''
dict1 = {"A":10, "B":20}
dict2 = {"C":30, "D":40}
print(f"The 1st disctionary : {dict1} The 2nd dictionaty : {dict2}")

dict1.update(dict2)
print(f"Concatenated dictionary : {dict1}")

'''Create a dictionary from extracting keys from a given dictionary'''
dict1 = {"key1":1, "key2":2, "key3":3}
dict2 = {}
print(f"Dictionary 1 : {dict1}, Dictionary 2 : {dict2}")

for k in dict1.keys():
    dict2[k] = dict1[k]
print(f"Dictionary 2 : {dict2}")

'''Delete a list of keys from a dictionary'''
dict1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
keys_del = ['a', 'c']
print(f"The dictionary : {dict1}, keys to be deleted : {keys_del}")

for key_del in keys_del:
    dict1.pop(key_del)

print(f"The dictionary after deletion : {dict1}")


'''Check if a value exists in dictionary'''
dict1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
value = 5
print(f"Dictionary : {dict1}, Value we are finding : {value}")
if value in dict1.values():
    print("The value is in dictionary !")
else:
    print("The value is not in dictionary !")


### Dictionary ###

