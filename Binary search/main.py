def BinarySearch(list, key):
    top = 0
    last = len(list) - 1
    mid = (top + last) // 2
    found = False
    while top <= last and not found:
        mid = (top + last) // 2
        if list[mid] == key:
            found = True
        else:
            if key < list[mid]:
                last = mid - 1
            else:
                top = mid + 1
    return found


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 65, 66, 69, 70, 77, 88, 99]
if BinarySearch(list, 65):
    print("The item is in the lise")
else:
    print("The item is not in the list")
