def BinarySearch(list, key, top, last):
    if top <= last:
        mid = (top + last) // 2
        if key == list[mid]:
            print("The number is in the list")
        else:
            if key < list[mid]:
                last = mid - 1
                BinarySearch(list, key, top, last)
            else:
                top = mid + 1
                BinarySearch(list, key, top, last)
    else:
        print("The number is not in the list")


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 65, 66, 69, 70, 77, 88, 99]
top = 0
last = len(list) - 1
BinarySearch(list, 99, top, last)
