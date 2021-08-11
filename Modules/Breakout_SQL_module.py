import sqlite3

def create_connection(database_name):
    '''returns objects with active connection to the database file'''
    conn = sqlite3.connect(database_name)
    return conn



def create_table(conn: sqlite3.Connection):
    table_name = input("Enter name of table\n")
    no_of_table_fields = int(input("Enter number of fields in the table\n")) 
    #Note:assembling queries using python variables like below makes the program vulnerable to SQL injection
    table_query = f'''CREATE TABLE IF NOT EXISTS {table_name} ('''
    for i in range(no_of_table_fields):
        field_name = input("Enter field name")
        n = int(input("Enter data type of this field:\n1 - smallint\n2 - varchar\n"))
        if n == 1:
            table_query += f'''{field_name} smallint'''
        else:
            table_query += f'''{field_name} varchar'''
        if i < no_of_table_fields-1:
            table_query += ', '
    table_query += ''');''' 
    cur = conn.cursor()
    cur.execute(table_query)
    conn.commit()
    conn.close() #ends connection with the database




def insert_values(table_name: str, conn: sqlite3.Connection):
    
    #block to find the number of columns in the table 
    cur = conn.cursor()
    cur.execute(f'''SELECT * FROM {table_name};''')
    columns = len(cur.fetchone()) 
    #block for making the query. Main code of function actually starts here 
    insert_query = f'''INSERT INTO {table_name} VALUES ('''
    for i in range(columns):
        value = input(f"Enter value for column {i+1}\n")  
        #later insert a block here to check if the data type of values entered by the user match the respective column data types 
        if type(cur.fetchone()[i]) == str:
            insert_query += f'''\'{value}\''''
        else:
            insert_query += f'''{value}'''
        if i < columns-1:
            insert_query += ''', '''
    insert_query += ''');'''  
    cur.execute(insert_query)
    conn.commit()
    conn.close()

def show_rows(table_name: str, conn: sqlite3.Connection):
    cur = conn.cursor()
    cur.execute(f'''SELECT * FROM {table_name};''')
    print(cur.fetchall())
    

if __name__ == '__main__':
    create_table(create_database('abcd.db')) #pass objects with ongoing connection to the database to the function create_table



