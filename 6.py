mylist = []
print("Enter 5 elements for the list: ")
for i in range(5):
    value = int(input())
    mylist.append(value)
print("Enter an element to be search: ")
element = int(input())
for i in range(5):
    if element == mylist[i]:
        print("Element found at Index:", i)
        print("Element found at Position:", i+1)
