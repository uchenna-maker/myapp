import sqlite3 

# create a connection to the database
con = sqlite3.connect('students.db') 

# create an instance of the cursor based on the connected database 
cursor = con.cursor() 

# cursor.execute("""CREATE TABLE IF NOT EXISTS student (
# firstname text, 
# surname text, 
# email text 
# ); 
# """) 

# test command to enter data 
# cursor.execute("INSERT INTO student VALUES ('Uchenna','Melford','uee1bolton.ac.uk');") 
# con.commit() 

# accepts args from calling function and inserts data using qry
def insertStudentQry (forename:str, surname:str, email:str): 

    # use parameterised qrys to mitigate sql injection 
    cursor.execute("INSERT INTO student VALUES (?,?,?)", (forename, surname, email)) 
    con.commit() 
    return 


# accepts input for students
def getStudentData(): 
    # pre-check loop to allow an unknown number of iterations 
    while True: 
        resp = input("Would you like to enter a student name? (Y/N)").upper() 
        if resp == "N": 
            break 
        else: 
            forename = input("Enter the student's forename: ").capitalize() 
            surname = input("Enter the student's surname: ").capitalize() 
            email = input("Enter the student's email: ").lower() 

            # call function to insert data and send values as args 
            insertStudentQry (forename, surname, email) 
            return 
        
# display all students
def viewStudentsQry(): 
    for row in cursor.execute("SELECT * FROM student"): 
        print(row) 
        
# test case 
getStudentData() 
viewStudentsQry()