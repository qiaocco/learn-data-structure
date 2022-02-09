def binary_search(lst, data):
    n = len(lst)
    if n == 0:
        return False

    mid = n // 2
    if lst[mid] > data:
        return binary_search(lst[:mid], data)
    elif lst[mid] < data:
        return binary_search(lst[mid + 1:], data)
    else:
        return True


def binary_chop(lst, data):
    n = len(lst)
    first = 0
    last = n - 1
    while first < last:
        mid = (first + last) // 2
        if lst[mid] > data:
            last = mid - 1
        elif lst[mid] < data:
            first = mid + 1
        else:
            return True
    return False


if __name__ == '__main__':
    print(binary_search(list(range(100)), 24))
