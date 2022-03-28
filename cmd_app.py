import mysql.connector as mc
import runpy
from prettytable import PrettyTable as pt


class Database:
    def __init__(self) -> None:  
        '''
        constructor of Database class creates smart_trolley database and checks for 
        table product_details, if not exist it will create one
        '''
        self.mydb=mc.connect(host="localhost",user="bot1",passwd="12345")
        self.mycursor=self.mydb.cursor()
        self.mycursor.execute("use smart_trolley")
        self.mycursor.execute("create table if not exists product_details(prod_name varchar(50),prod_id varchar(10),location varchar(8),category varchar(20))")
        self.mydb.commit()

    def add_items(self,prod_name,prod_id,prod_loc,prod_cate):
        '''
        add_items method takes 4 parameters(product_name,product_id,product_location,product_category)
        '''
        self.mycursor.execute("insert into product_details values('%s','%s','%s','%s');"%(prod_name,prod_id,prod_loc,prod_cate))
        self.mydb.commit()
        print("Item added")

    '''show_items method used to display list of available products
    '''        
    def show_items(self):
        self.mycursor.execute("select prod_name from product_details;")
        avail_items=self.mycursor.fetchall()
        c=1
        product_table=pt(["s.no","Product"])
        for item in avail_items:
            #print("{}. {}".format(c,item[0]),end="\n")
            product_table.add_row([c,item[0]])
            c+=1
        print(product_table)

    '''show_items_by_location method used to display list of available products with their location
    ''' 
    def show_items_by_location(self):
        self.mycursor.execute("select prod_name,location from product_details;")
        avail_items_with_location=self.mycursor.fetchall()
        c=1
        for item in avail_items_with_location:
            print("{}. {} {}".format(c,item[0],item[1]),end="\n")
            c+=1
    '''share_item_location method used to return a dictionary of available products with their location'''
    def share_item_location(self):
        self.mycursor.execute("select prod_name,location from product_details;")
        avail_items_with_location=self.mycursor.fetchall()
        item_dict={}
        for item in avail_items_with_location:
            item_dict[item[0]]=item[1] 
        return item_dict


def get_items(db_obj):
    """
    method to get items from user when add item command is given"""
    prod_name=input("Enter product name : ")
    prod_id=input("Enter product id : ")
    prod_loc=input("Enter product location : ")
    prod_cate=input("Enter product category : ")
    if prod_name!=" " and prod_id!=" " and prod_loc!=" " and prod_cate!=" ":
        db_obj.add_items(prod_name,prod_id,prod_loc,prod_cate)

def find_product(user_given_list,prod_name):
    '''
    method to find whether product is available'''
    if prod_name in user_given_list.keys():
        print("{} is available at {}".format(prod_name,user_given_list[prod_name]))

    else: 
        print("{} is not available".format(prod_name))

#driver code starts here
def welcome():
    print("Welcome to smart trolley")
    print("-------- Available commands -----")
    print("1. Add items \n2. Show items \n3.sort shop list \n4.Find product  \n5.Show items with location \n Exit")
    process = True
    while process:
        command = input("--->  Enter command :  ")
        db_obj=Database()
        print("-"*25)
        if command == "add" or command=='1':
            get_items(db_obj)
            print("-"*20)
        elif command == "show" or command=='2':
            db_obj.show_items()
            print("-"*20)
        elif command == "sort" or command=='3':
            runpy.run_path("sort_the_maliga_list.py")
            print("-"*20)
        elif command=="find" or command=='4':
            user_given_list=db_obj.share_item_location()
            find_product(user_given_list,input("Enter product name : "))
        elif command=="location" or command=='5':
            db_obj.show_items_by_location()
            print("-"*20)
        elif command == "exit" or command=='n':
            process=False
            print("Thank you for using smart trolley")

if __name__=="__main__":
    welcome()