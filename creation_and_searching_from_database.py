import mysql.connector

try:
    myDb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Allah786??'
    )

    my_cursor = myDb.cursor()

    # creating the database
    sql_command_1 = ("create database if not exists books_store") 
    my_cursor.execute(sql_command_1)
    
    # using the created database :
    sql_command_2 = ('use books_store ') 
    my_cursor.execute(sql_command_2)

    # creating the tables of the database :
    sql_command_3 = ('''create table if not exists books_info(
                    book_name VARCHAR(100) NOT NULL,
                    author_name VARCHAR(50) NOT NULL,
                    price VARCHAR(20) NOT NULL DEFAULT "0",
                    published_at YEAR NOT NULL
                    ) ''') 

    my_cursor.execute(sql_command_3) 

    # getting the name of user :
    name = input(
        "Hello! Buddy \nI hope you will be alright \nPlease enter your name : \n")

    # printing the name of user :
    user_input = input(f'''Well {name}, 
              Type 's' for search any record of book from saved records. 
              Type 'e' for enter a new books records. 
              Type 'exit' for exit the program. 
              ''')
    # conditions for continuety of program :

    if user_input.lower() == 'exit':
        exit()

    elif user_input.lower() == 's' :
        b_name = input('Kindly enter the book name of which you want to check record :  ')

        sql_command = (f'''select * FROM books_info WHERE book_name like "%{b_name}%" ''')
        my_cursor.execute(sql_command)
        results = my_cursor.fetchall() 

        # loop for printing the searched record :

        for row in results :
            print(row) 


    elif user_input.lower() == 'e':
        
        # getting all info from the user :
        while True:
            try:
                print("_____Just type 'enter' to save the record_____")
                print("_____For enter new records_|just press enter|_____")

                cont_loop = input()
                if cont_loop.lower() == 'enter':
                    break

                # table columns inputs :
                bookName = input('Enter the name of book :  ')
                authorName = input("Enter the name of book's author : ")
                price = input("Enter the price of book : ")
                year = input("Enter the year of publish (like '1985') : ")

                # editing the data in tables :
                sql_command_4 = ('''INSERT INTO books_info(
                                    book_name,
                                    author_name,
                                    price,
                                    published_at)
                                    VALUES (%s,%s,%s,%s)
                ''')

                sql_command_5 = bookName, authorName, price, year

                my_cursor.execute(sql_command_4, sql_command_5) 

                myDb.commit()

            except Exception as f :
                print(f) 

    # printing the data from database : 
    u_input = input('''Now if you want to check the all record of books then 
                        type 'y' 
                        other-wise |just press enter| to continue program 
                        ''')
        
    # conditions for showing the data to user :
    if u_input.lower() == 'y' :
        my_cursor.execute("select * from books_info")

        result = my_cursor.fetchall()

        # loop for displaying :
        for data in result:
            print(data) 

    else :
        pass 

except Exception as e:
    print(e)

else:
    print("_____Process successful_____")
