#this code initialize function to create connection, create database, create tables and isert data into the tables


import mysql.connector
import csv 

mydb = mysql.connector.connect(user = "root", password = "root", host = "127.0.0.1" )
DB_NAME = "habeb"


# creating function to cennect the mysql server,creat data base if it is not created, create tables, and isert data into.
def create_database():  
    # creat connection with mysql.
    # mydb = mysql.connector.connect(user = "root", password = "root", host = "127.0.0.1" )
    DB_NAME = "habeb"
    csv_data1 = csv.reader(open('planets.csv'))
    headr = next(csv_data1)
    #initialize courser object to comunicate wiyh my sql
    my_cursor= mydb.cursor() 
    #check and creat database if it is not exist.
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS habeb") 
    mydb.commit() #save


    mydb = mysql.connector.connect(user = "root", password = "root", host = "127.0.0.1",database ="habeb")#newe conect to data base habeb
    #initialize courser object to comunicate wiyh my sql
    my_cursor= mydb.cursor()
    #creat species tabel
    my_cursor.execute("CREATE TABLE species(name varchar(225),\
        classification varchar(225),\
        designation varchar(225) ,\
        average_height INT ,skin_colors varchar(225),\
        hair_colors varchar(225), eye_colors  varchar(225), average_lifespan int,language varchar(225), homeworld varchar(225))")

    #insert data from csv dile into spacies tabel
    with open ("species.csv","r") as csvfile:   # I had saved csv files in the same folder with programs.
        csv_data1= csv.reader(open('species.csv'))
        count = 0
        for row in csv_data1:
            if count == 0 :
                count +=1
            else:   
                for i in range(9):   #replace NA with NOne
                    if row[i]=='NA' or row[i] == 'indefinite':
                        row[i]=None
                        
                tb1 = "INSERT INTO species VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                value1 = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
                my_cursor.execute(tb1,value1)
                count =+1
                mydb.commit()   #save changes
    show1= "select * from species"
    my_cursor.execute(show1)
    myresult = my_cursor.fetchall()
    print("species table:")
    for x in myresult:    #print out the tabel in termenal.
        print(x)
    print()

    #creat table planets
    my_cursor.execute("CREATE TABLE planets (name VARCHAR(255),\
    rotation_period VARCHAR(225),\
    orbital_period VARCHAR(255),\
    diameter VARCHAR(225),\
    climate VARCHAR(255),\
    gravity VARCHAR(255),\
    terrain VARCHAR(255),\
    surface_water VARCHAR(225),\
    population VARCHAR(255))")

    with open ("planets.csv","r") as csvfile:  # i had saved the scv files in the same folder with python program
        csv_data2 = csv.reader(csvfile) #reading the csv file
        count = 0
        for row in csv_data2:
            if count == 0 :
                count +=1
            else:
                for i in range(9):   #replace NA with NOne
                    if row[i]=='NA':
                        row[i]=None
                        
                tb = "INSERT INTO planets VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"   #inserting data
                value = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                my_cursor.execute(tb,value)
                count =+1
                mydb.commit()
                
    show2 = "select * from planets" #printing the tabel
    my_cursor.execute(show2)
    myresult = my_cursor.fetchall()
    print("planets table:")
    for y in myresult:
        print(y)

def main_menu():      #creating function to print the main minue..
    print("1.List all planets.")
    print("2.Search for planet name.")
    print("3.Search for species with height higher than given number.")
    print("4.what is the most likely desired climate of given species ?. ")
    print("5.what is the average lifespan per species clasiification ?.")
    print("6. to close.")
    print("------------")



def check_DB(my_cursor,DB_NAME):  # function to check if there is a data base called habeb 
                                  # else creat data base and tables and insert data into tables

    try:
        my_cursor.execute(f"use {DB_NAME}")
        print()
        print(f"the program use data base {DB_NAME} ")
        mydb.commit()

    except Exception as e:
        # if there is no database with the given name, create new one
        if str(e) == (f"1049 (42000): Unknown database '{DB_NAME}'"):
            print(f"There is no database with name {DB_NAME} ")
            create_database()
            my_cursor.execute(f"use {DB_NAME}")

        else :
            print(str(e))




