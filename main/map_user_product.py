'''
user maligai list get pannu
list oda items location get pannu
then get xy coordinates
map the locations on the image



keep client side seperately (getting the list from user
share item location can be moved to cmd file )
'''



import mysql.connector as mc
from matplotlib import image 
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

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
        self.mycursor.execute("drop table if exists cutomer_table;")
        self.mycursor.execute("create table if not exists customer_table(product_name varchar(20),location varchar(20))")
        self.mydb.commit()

    def get_user_shopping_list(self):
        item_counter=1
        print("Enter your shopping list : ")
        print("1) Manual Entry of list \n2) Scan QR code \n3) From file")
        option=int(input())
        if option==1:
            user_shopping_list=[]
            while True:
                item=input("Enter item %d :"%(item_counter))
                item_counter+=1
                if item!="end":
                    user_shopping_list.append(item)
                else:
                    break
        elif option==2:
            pass 
        elif option==3:
            with open("E:/projects/smart trolley/txt_and_readme/shopping_list.txt",'r') as f:
                user_shopping_list=f.read().splitlines()
            x_y_coord=self.share_item_location(user_shopping_list)
            img = mpimg.imread('E:/projects/smart trolley/image_mapping/imgs/floor_1.png')
            plt.figure(figsize = (12,12))
            plt.imshow(img)
            for i in range(len(x_y_coord)):
                plt.plot(x_y_coord[i][0],x_y_coord[i][1], marker='v', color="red")
            plt.show()
        
    def share_item_location(self,user_shopping_list):             
        item_list=[]
        item_list_loc=[]
        i=0
        self.mycursor.execute("select location from product_details;")
        avail_items_with_location=self.mycursor.fetchall()
        for item in avail_items_with_location:  
            item_list_loc.append(item[0])
            self.mycursor.execute("select c.x_cord,c.y_cord from coordinates_table c,customer_table cus where c.location=cus.location;")
            x_y_coord=self.mycursor.fetchall()
        return x_y_coord


    def make_entry_in_coordinates_table(self):  
        user_shopping_list=[]
        with open("../smart trolley/txt_and_readme/shopping_list.txt",'r') as f:
            user_shopping_list=f.read().splitlines()
        for item in user_shopping_list:
            self.mycursor.execute("select location from product_details where prod_name='%s';"%(item))
            location=self.mycursor.fetchone()
            if location!=None:
                self.mycursor.execute("insert into customer_table (product_name,location) values('%s','%s');"%(item,location[0]))
                self.mydb.commit()
                
    

        #print(item_list)    
if __name__=="__main__":
    db=Database()
    db.make_entry_in_coordinates_table()
    db.get_user_shopping_list()
    


                