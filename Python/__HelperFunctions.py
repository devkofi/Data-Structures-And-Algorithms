def flatten(items, maintain_order=True):
    """
    This is a function to flatten deeply nested list. \n
    Set maintain_order to False if you do not care about the 
    order the list is presented
    """
    counter = 0
    
    while counter < len(items):
        
        if type(items[counter]) == list:
            length = 0
            for i in items[counter]:
                items.append(i)
                length += 1
            
            if maintain_order:
                #use this to maintain order
                items = items[:counter] + items[-length:] + items[counter + 1: len(items) - length]
            else:
                #or use this if order is not relevant
                del items[counter]
          
        counter += 1
    
    return items

initial_list = [1, [2, 3, [79, 29, [16, 44, [12, 20, [64,[-10]]]]]], 4, [5, [6, 7, [22, 30, [81, 40, [300, 200, [100, 400]]]]]], 8, [9, 10]]
print(initial_list)

flat_list = flatten(initial_list, True)
print(flat_list)