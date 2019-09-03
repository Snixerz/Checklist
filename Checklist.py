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
    update(index, "√" + checklist[item])
    list_all_items()

def select(function_code):

    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    elif function_code == "R":
        item_index = user_input("Index Number?")

        print(read(int(item_index)))

    elif function_code == "P":
        list_all_items()

    else:
        print("Unknown Option")

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
