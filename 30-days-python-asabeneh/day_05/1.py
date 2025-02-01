# source -
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/day_5.py

empty_list = list()  # this is an empty list, no item in the list
print(len(empty_list))  # 0
print(len(empty_list) == 0)  # True

# Lists can have items of different data types
lst = [
    "Asabeneh",
    250,
    True,
    {"country": "Finland", "city": "Helsinki"},
]

# sq bracket syntax
fruits = ["banana", "orange", "mango", "lemon"]  # list of fruits
print(fruits)  #  ['banana', 'orange', 'mango', 'lemon']
print(len(fruits))  # 4
print(fruits[0])  # banana
print(fruits[1])  # orange
print(fruits[len(fruits) - 1])  # lemon
print(fruits[-2])  # mango (accessing second last item)
print("-----")

# --- Unpacking List Items - example 1  ---
lst = ["item1", "item2", "item3", "item4", "item5"]
first_item, second_item, third_item, *rest = lst
print(first_item)  # item1
print(second_item)  # item2
print(third_item)  # item3
print(rest)  # ['item4', 'item5']
print("-----")

# Unpacking List Items - example 2
first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)  # 1
print(second)  # 2
print(third)  # 3
print(rest)  # [4,5,6,7,8,9]
print(tenth)  # 10

# ---- Slicing items ----
# Positive Indexing: We can specify a range of positive
# indexes by specifying the start, end and step, the return value will be a new
# list. (DEFAULT VALUES for start = 0, end = len(lst) - 1 (last item), step = 1)
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits[0:4])  # returns all the fruits

#  If we don't set where to stop it takes all the rest
print(fruits[0:])  # returns all the fruits as above

# start items including item at index 1 and exclude item at index 3
print(fruits[1:3])  # ['orange', 'mango']
print(fruits[1:])  # ['orange', 'mango', 'lemon']
print("------")
print("------")

fruits = ["banana", "orange", "mango", "lemon"]
# negative indexes works like this:
#  "banana"   "orange"   "mango"   "lemon"
#      0          1          2         3
#     -4         -3         -2        -1

print(fruits[-4:])  # ["banana", "orange", "mango", "lemon"]
print(fruits[-3:-1])  # ['orange', 'mango']         # does not include the end index
print(fruits[-3:])  # ['orange', 'mango', 'lemon']


print("------ STEP EXAMPLE")
# here we used a 3rd argument, step. It will take every 2nd item - ['banana', 'mango']
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits[::2])  # ['banana', 'mango']


print("------ NEGATIVE STEP EXAMPLE")
# a negative step will take the list in reverse order
print(fruits[::-1])  # ['lemon', 'mango', 'orange', 'banana']


print("\n------ Modifying List")
fruits = ["banana", "orange", "mango", "lemon"]
fruits[0] = "Avocado"
print(fruits)  #  ['avocado', 'orange', 'mango', 'lemon']

fruits[1] = "apple"
print(fruits)  #  ['avocado', 'apple', 'mango', 'lemon']

fruits[len(fruits) - 1] = "lime"
print(fruits)  #  ['avocado', 'apple', 'mango', 'lime']
