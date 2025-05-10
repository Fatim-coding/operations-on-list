lst = ['Apple', 'Guava','mango', 'Banana', 'kiwi']

print("Length of list", len(lst))
print("First Element:", lst[0])
print("Last Element:", lst[-1])

lst.append('papaya')
print("Updated List :", lst)

lst.sort()
print("sorted List:", lst)

lst.pop(1)
print("updated List :", lst)

lst.reverse()
print("Reversed List :", lst)

print("Mulitplication on list :", lst*2)

lst = lst[:4]
print("sliced List :", lst*2)
      
lst.clear()
print("updated List :", lst)