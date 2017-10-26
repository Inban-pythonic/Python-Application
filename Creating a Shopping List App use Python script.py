#NEED A LIST TO PUT ALL ITEMS:

shopping_list = []

def print_help():
    #PRINT HELP
    print("What do you want to add today?")
    print("""
Type "DONE" to quit
Type "HELP" to see help
Type "SHOW" to see current shopping list
""")

def print_items():
    #PRINT THE LIST
    print("You've got in your shopping list: ")
    for item in shopping_list:
        print(item)

def add_item(new_item):
    shopping_list.append(new_item)
    print("Added {}, you got {} items in your list". format (new_item, len(shopping_list)))

print_help()
while True:
    #NEED TO PUT ITEMS INTO THE LIST
    new_item = input("> ")

    #QUIT THE PLROGRAM
    if new_item.upper() == "DONE":
        break
    elif new_item.upper() == "HELP":
        print_help()
        continue
    elif new_item.upper() == "SHOW":
        print_items()
        continue
    add_item(new_item)

print_items()







#OUTPUT EXAMPLES::::

Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python36-32/Creating a Shopping List App use Python script.py 
What do you want to add today?

Type "DONE" to quit
Type "HELP" to see help
Type "SHOW" to see current shopping list

> banana
Added banana, you got 1 items in your list
> mangO
Added mangO, you got 2 items in your list
> apple
Added apple, you got 3 items in your list
> Grape
Added Grape, you got 4 items in your list
> help
What do you want to add today?

Type "DONE" to quit
Type "HELP" to see help
Type "SHOW" to see current shopping list

> show
You've got in your shopping list: 
banana
mangO
apple
Grape
> done
You've got in your shopping list: 
banana
mangO
apple
Grape
>>> 
                                                             
