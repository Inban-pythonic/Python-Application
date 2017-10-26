#need a list to put all items
shopping_list = []

def print_help():
    #print help
    print("What do you want to add today?")
    print("""
Type 'DONE' to quit
Type 'HELP' to see help
Type 'SHOW' to see current shopping list
""")

def print_items():
    #print the list
    print("You've got in your shopping list: ")
    for item in shopping_list:
        print(item)

def add_item(new_item):
    shopping_list.append(new_item)
    print("Added {}, you got {} items in your list". format(new_item, len(shopping_list)))

print_help() 
while True:
    #need to put items into the list
    new_item = input("> ")

    #quit the program
    if new_item.upper()=="DONE":
        break
    elif new_item.upper() == "HELP":
        print_help()
        continue
    elif new_item.upper() == "SHOW":
        print_items()
        continue
    add_item(new_item)

print_items()
    
    



