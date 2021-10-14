try:
    import mysql.connector 

    myDb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Allah786??',
        database = 'books_store' 
        ) 

    my_cursor = myDb.cursor() 

    u_input = input('Please enter the name of book of which you want to delete record : ')

    my_cursor.execute(f'''delete from books_info where book_name = "{u_input}" ''') 

    myDb.commit() 

except Exception as e :
    print(e) 

else:
    print("_____Process successful_____")