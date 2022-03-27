#insert the coordinates of the store into database

#manually doing is not vananging so script eluthi db la push pa poren


import mysql.connector as mc 
import matplotlib.pyplot as plt
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
        self.mycursor.execute("create table if not exists coordinates_table(location varchar(10))")
        self.mydb.commit()

    def insert_coordinates_of_store(self):
        column="abcdefghijklmnopqrstuvwxyz"
        row="123456"
        rack="123"

        for i in column:
            for j in row:
                for k in rack:
                    location=str(i)+'-'+str(j)+'-'+str(k)
                    self.mycursor.execute("insert into coordinates_table values('%s');"%(location))
                    self.mydb.commit()
    
    def generate_coordinates_location(self):
        column="abcdefghijklmnopqrstuvwxyz"
        row="123456"
        rack="123"
        location_list=[]
        

        for i in column:
            for j in row:
                for k in rack:
                    location_list.append(str(i)+'-'+str(j)+'-'+str(k))
        def onclick(event): 
            global counter
            print("location=%s, xdata=%f, ydata=%f" % (location_list[counter], event.xdata, event.ydata))
            self.mycursor.execute("update coordinates_table set x_cord='%f' where location='%s';"%(event.xdata,location_list[counter]))
            self.mycursor.execute("update coordinates_table set y_cord='%f' where location='%s';"%(event.ydata,location_list[counter]))
            self.mydb.commit()
            counter+=1

        def onrelease(event):
            pass
        img = mpimg.imread('E:/projects/smart trolley/image_mapping/imgs/floor_1.png')
        plt.figure(figsize = (12,12))
        ax = plt.imshow(img)
        fig = ax.get_figure()
        cid = fig.canvas.mpl_connect('button_press_event', onclick) 
        cid = fig.canvas.mpl_connect('button_press_event', onrelease)
        plt.show()

if __name__=="__main__":
    counter=0
    db_obj=Database()
    #db_obj.insert_coordinates_of_store()
    db_obj.generate_coordinates_location()