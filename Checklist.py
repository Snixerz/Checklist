checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item
    return

# DESTROY
def destroy(index):
    checklist.pop(index)

# READ ALL
def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1

def mark_completed(index):
    update(index, "√" + checklist[index])
    list_all_items()   

def select(function_code):

    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)

    elif function_code == "R":
        item_index = user_input("Index Number?")
        print(checklist[int(item_index)])
        
    elif function_code == "U":
        update(user_input("Input an index you'd like to change"),  user_input("Input what you'd like to update"))
        
    elif function_code == "D":
        destroy(int(user_input("Please input an index for an element you would like to delete")))
        
    elif function_code == "P":
        list_all_items()
        
    elif function_code == "Q":
        return False

    else:
        print("Unknown Option")
        
def test():
    print("Testing function")
    select("C")
    list_all_items()
    print("Testing function")
    select("R")
    list_all_items()
    print("Testing function")
    select("M")
    list_all_items()
    print("Testing function")
    select("U")
    list_all_items()
    print("Testing function")
    select("D")
    list_all_items()
    print("Testing function")
    select("P")
    print("Tesing function")
test()

def user_input(prompt):

    user_input = input(prompt)
    return user_input

def colors():
    create("Purple")
    create("Green")
    create("Yellow")
    create("Red")
    create("Blue")

colors()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list")
    select(selection)
