try:
    import mysql.connector 

    myDb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Allah786??',
        database = 'books_store' 
        ) 

    my_cursor = myDb.cursor() 

    my_cursor.execute('''update books_info set price = "76$" where book_name = "A little life" ''') 

    myDb.commit() 

except Exception as e :
    print(e) 

else:
    print("_____Process successful_____")