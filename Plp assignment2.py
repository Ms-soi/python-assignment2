my_list = []
my_list.append([10, 20, 30, 40])
print(my_list)

my_list.insert(1, [15])
your_list = [50, 60, 70]
my_list.extend(your_list)

# To remove 40 from the first inner list
my_list[0].remove(40)

# To flatten the list before sorting
flat_list = [item for sublist in my_list if isinstance(sublist, list) for item in sublist] + [item for item in my_list if not isinstance(item, list)]
flat_list.sort()
print(flat_list)

# To find the index of 30
print(flat_list.index(30))