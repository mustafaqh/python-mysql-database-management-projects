#the main program

import msvcrt
import mysql.connector
from creat_database import*

mydb = mysql.connector.connect(user = "root", password = "root", host = "127.0.0.1" )
my_cursor = mydb.cursor() #initialize courser object to connect ti db
DB_NAME = "habeb"





check_DB(my_cursor,DB_NAME)   # calling check funktion
print()
    # main_menu

while True:
    
    main_menu()  #print the main minue when the program starts
    choice = int(input("please choose a question...")) #asks the user to choose one of the alternative in the main menu
    
    if choice == 1 :
        my_cursor.execute("select name from planets")  #execute sql query to get planet's name.
        myresult = my_cursor.fetchall() #using fetches all  rows of a query result set and returns a list of tuples.
        for x in myresult: #loop for getting all planets names.
            print(x[0]) # print planets names.

        print() #printing an empty line.
        print("press any key to return to the main minue.")  #print a this statment to ask user if want to go back to main menu.
        msvcrt.getch()
        # continue

    elif choice == 2 :
        x = input("Enter the Planet Name:\t")      # ask user to enter planet's name.
        my_cursor.execute(f"select * from planets where name ='{x}'")        #execute sql query to Search for planet details
        myresult = my_cursor.fetchall()    #using fetches all  rows of a query result set and returns a list of tuples.
        for x in myresult: #loop to get a planets details
            print(f"Name: {x[0]}")
            print(f"Rotation Period: {x[1]}")
            print(f"Orbital_Period: {x[2]}")
            print(f"Diameter: {x[3]}")
            print(f"Climate: {x[4]}")
            print(f"Gravity: {x[5]}")
            print(f"Terrain: {x[6]}")
            print(f"Surface Water: {x[7]}")
            print(f"Population: {x[8]}")

        print() #printing an empty line.
        print("press any key to return to the main minue.")     #print a this statment to ask user if want to go back to main menu.
        msvcrt.getch()        #with this statment the user can go back to main minue by pressing any key.
        

    elif choice == 3 :
         # ask user to enter the minimum averageheight of  species.
        zy=int(input("enter the minimum averageheight :"))
        #execute sql query to select the species name wher the average_height is 
        #bigger than the average_height entered by the user.
        my_cursor.execute(f"SELECT name FROM species WHERE average_height > '{zy}'") 
        my_result = my_cursor.fetchall()          #using fetches all  rows of a query result set and returns a list of tuples.                            
        print(my_result)
        print()                                   
        print("press any key to return to the main minue.")  #print a this statment to ask user if want to go back to main menu.
        msvcrt.getch()
        
        

    elif choice == 4 :
        given_species = input("enter species's name : ") 
        #execute sql query to get the most likely desired climate of the given species
        my_cursor.execute(f"SELECT p.climate from species s LEFT JOIN planets p on s.homeworld = p.name where s.name = '{given_species}' ")
        climate = my_cursor.fetchall()
        print ("the most likely desired climate of given species is : ", end=" ")
        for n in climate :
            print(str(n[0]))
        print()
        print("press any key to return to the main minue.")
        msvcrt.getch()
        # continue

    elif choice == 5 :
        #execute sql query to get the average lifespan per species classification
        my_cursor.execute(f"SELECT classification, AVG(average_lifespan) from species GROUP BY classification ")
        myresult = my_cursor.fetchall()
        for x in myresult:
            print(x)
        print()
        print("press any key to return to the main minue.")
        msvcrt.getch()
        # continue

    elif choice == 6 :      # if  user press 6 the while loob will break and exit the main minue and stop the program.
        print("okey..!..bye bye..!")
        break

    else:  # in case the use pressed invaild numer that not shown in the main minue.
        print("invaild number..!")
        print()
        print("press any key to return to the main minue.")
        msvcrt.getch()
    print()

        


    