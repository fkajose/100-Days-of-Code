import time


def f1(list_of_list):
    result = []  # O(1)
    for inner_list in list_of_list:  # O(1)
        for x in inner_list:  # O(1)
            if x not in result:
                result.append(x)
    return result


def f2(list_of_list):
    flat_list = []
    for inner_list in list_of_list:
        flat_list.extend(inner_list)
    return [
        x for i, x in enumerate(flat_list)
        if flat_list.index(x) == i]


def f3(list_of_list):
    result = []
    seen = set()
    for inner_list in list_of_list:
        for x in inner_list:
            if x not in seen:
                result.append(x)
                seen.add(x)
    return result


list = [[1, 1, 2], [1, 1, 3], [4, 2], [5, 2, 3]] * 19000000

start = time.time()
print(f3(list))
end = time.time()
print(end - start)
