list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
common_elements = []

for first in list1:
    for second in list2:
        if first == second and first not in common_elements:
            common_elements.append(first)

for element in common_elements:
    print(element)
