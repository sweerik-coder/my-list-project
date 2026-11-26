# My first change
# My second change
# My third change good super help
def add_item(items, item):
    items.append(item)

def remove_item(items, item):
    if item in items:
        items.remove(item)

def show_items(items):
    print(items)


my_list = []

add_item(my_list, "Молоко")
add_item(my_list, "Хліб")
show_items(my_list)
remove_item(my_list, "Хліб")
show_items(my_list)
