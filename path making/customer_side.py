from dynamic_sorting import dyn_sorting
door_no= 1 #int(input("Enter door no : "))
user_list=['sakthi masala','happy happy', 'surf excel','50 50']


lines=[['A','B','K','L','M','N','X','W'],
            ['C','D','J','I','O','P','V','U'],
            ['E','F','G','H','Q','R','S','T']
            ]

layers=[['A','B','C','D','E','F'],
        ['G','H','I','J','K','L'],
        ['M','N','O','P','Q','R'],
        ['S','T','U','V','W','X'],
        ['Y','Z']]


if door_no==1:
    item_list,item_dic=dyn_sorting()
    #print(item_dic)
    racks_with_items = set()

    for item in user_list:
        racks_with_items.add(item_dic[item][0])
    #print("racks_with_items",racks_with_items,end=" ")
    

    poga_vendiya_lines=set()
    for column in racks_with_items:
        for line  in lines:      
            if column.upper() in line:
                poga_vendiya_lines.add(lines.index(line))
                break
    
    poga_vendiya_layers=set()
    for column in racks_with_items:
        for layer  in layers:      
            if column.upper() in layer:
                poga_vendiya_layers.add(layers.index(layer))
                break



    print(poga_vendiya_lines)
    print(poga_vendiya_layers)


elif door_no==2:
    pass

