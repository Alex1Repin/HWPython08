def get_da(part, all):
    li = []
    for i in all:
        li.append(i.split()[part])
    return li

def sort(part, all):
    li =[]
    for i in all:
        if part in i:
            li.append(i)
    return li