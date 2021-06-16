import random

def swap(items, first_index, second_index):
    first = items[first_index]
    second = items[second_index]

    items[first_index] = second
    items[second_index] = first

    return items

def bubble_sort(items: list) -> list:
    for i in range(len(items) - 1):
        left = items[i]
        right = items[i+1]

        if right < left:
            swap(items, i, i+1)

    return items

def bogo_sort(items: list) -> list:
    random.shuffle(items)
    return items

def gnome_sort(items: list) -> list:
    for i in range(len(items) - 1):
        item_index = i+1
        if items[item_index] < items[i]:
            item = items[item_index]
            for n in range(1, len(items)):
                new_index = item_index - n
                if items[new_index+1] > item and items[new_index-1] < item:
                    print(items.pop(item_index))
                    items.insert(new_index, item)
                    return items

    return items

ALGORITHMS = {
    "bubble": bubble_sort,
    "bogo": bogo_sort,
    "gnome": gnome_sort
}