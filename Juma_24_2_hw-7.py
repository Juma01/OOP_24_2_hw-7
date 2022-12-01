database = []


def binary_search(lst, el):  # range((1, 21), 3)
    a = lst[0]                    # 1
    b = lst[-1]                   # 20  # 10  # 5  # 3
    c = len(lst) // 2             # 10  # 5   # 3
    while True:
        if c < el:                # 10 < 3  # 5 < 3  # 3 < 3
            database.append(c)
            a = c
            c = (a + b) // 2
        elif c > el:              # 10 > 3  # 5 > 3  # 3 > 3
            database.append(c)
            b = c
            c = (a + c) // 2      # 10 + 1 // 2 = 5  # 5 + 1 // 2 = 3
        elif c == el:             # 3 == 3 True
            database.append(c)
            return f'Количество попыток - {len(database)}'


print(binary_search(range(1, 21), 3), f'{database},')


bubble_list = []


def bubble_sort(lst):
    while len(lst) != 0:
        i = lst.index(min(lst))
        bubble_list.append(lst.pop(i))
    return f'Список отсортирован {bubble_list}'


print(bubble_sort([231, 41, 4243, 234, 5, 65, 7]))