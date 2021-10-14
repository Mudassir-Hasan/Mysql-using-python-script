try:
    import mysql.connector 

    myDb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Allah786??',
        database = 'books_store' 
        ) 

    my_cursor = myDb.cursor() 

    book_name = input('Hello! dear please enter the name of book of which you want to update : ') 

    att = input('''Now Type 
                            '1' for update book's name :
                            '2' for update author's name :
                            '3' for update price of book
                            '4' for update published date of book \n''')

    if att == '1' :
        name = input('Enter the updated name : ') 
        
        my_cursor.execute(f'''update books_info set book_name = "{name}" 
        where book_name = "{book_name}" ''') 
        
        myDb.commit() 

    elif att == '2' :
        Name = input('Enter the updated name : ') 
        
        my_cursor.execute(f'''update books_info set author_name = "{Name}" 
        where book_name = "{book_name}" ''') 
        
        myDb.commit()

    elif att == '3' :
        price = input('Enter the updated price : ') 
        
        my_cursor.execute(f'''update books_info set price = "{price}" 
        where book_name = "{book_name}" ''') 
        
        myDb.commit()

    elif att == '4' :
        year = input(f'Enter the updated year of publishing {book_name}  like (1985) : ') 
        
        my_cursor.execute(f'''update books_info set author_name = "{year}" 
        where book_name = "{book_name}" ''') 
        
        myDb.commit()


except Exception as e :
    print(e) 

else:
    print("_____Process successful_____")