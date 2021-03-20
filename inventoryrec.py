grosdic={'rice':'A-3-II',
         'wheat':'A-4-I',
          'corn':'B-2-II'} 
print("Enter process")
x=int(input())
if x==1:
    print("enter product name ")
    a=str(input())
    print("enter its location ")
    loc=str(input())
    grosdic.__setitem__(a,loc)
    print(grosdic)
elif x==2:
    print(grosdic)
