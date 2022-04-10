from cmd_app import Database
from prettytable import PrettyTable as pt
"""
creates obj for databse class
access share item location method and obtain the dictionary
sort the dictionary by:
    creating temp list for value to eliminates "-"
    sort that list and add to ordered dictionary
    using show dic method to display the sorted dictionary
"""
def sorting_list(user_given_list):
    temp_list = []
    ordered_dic={}
    for location in user_given_list.values():
        temp_list.append(location)

    for location in range(len(temp_list)):
        temp_list[location]=temp_list[location].replace("-","")
    c=0
    for ke in user_given_list.keys():
        ordered_dic[ke]=temp_list[c]
        c+=1
    ordered_dic=sorted(ordered_dic.items(),key=lambda x:x[1])
    return ordered_dic

def show_dic(sorted_dic):
    c=1
    product_table=pt(["s.no","Product","Location"])
    for item in sorted_dic:
        #print("{}. {} {}".format(c,item[0],item[1]))
        product_table.add_row([c,item[0],item[1]])
        c+=1
    print(product_table)



obj=Database()
user_given_list = obj.share_item_location()
sorted_list = sorting_list(user_given_list)
show_dic(sorted_list)