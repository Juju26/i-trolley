from inventoryrec import grosdic

#print("enter product location as:               ex: A-3-II") 
'''grosdic={'rice':'A-3-II',
         'wheat':'A-4-I',
          'corn':'B-2-II'} '''
print("Enter item")
a=input().split(" ")
a=[i.lower() for i in a]

#a=str(a) 
#print(grosdic[a])


#product availability gives the location if product available 
def productavailability(grosdic,user_item): #grosdic is the dictonary & user_item is item to be searched
    c=0
    #b=[val for key,val in grosdic.items() if user_item==key] 
    for key,val in grosdic.items():
        if user_item==key:
            b=val
            c+=1
    if c>0:
        print(str(b)) 
    else:
        print("Item not available")
for i in a:   
    productavailability(grosdic,i)
