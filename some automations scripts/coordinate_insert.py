#insert the coordinates of the store into database

#manually doing is not vananging so script eluthi db la push pa poren


import mysql.connector as mc 


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

if __name__=="__main__":
    db_obj=Database()
    db_obj.insert_coordinates_of_store()