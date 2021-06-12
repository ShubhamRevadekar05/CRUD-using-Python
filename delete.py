import db_connection as dbConn

class Delete:
    def func_DeleteDataUsingRollNo(self):
        connection = dbConn.getConnection()
        roll_no = input("Enter Roll no.: ")
        try:
            query = "delete from students where roll_no=%(roll_no)s;"
            cursor = connection.cursor()
            cursor.execute(query, {'roll_no': roll_no})
            connection.commit()
            print("Successfully deleted data!")
        except:
            print("Error! Something went wrong.")
        finally:
            connection.close()

    def func_DeleteDataUsingRegistrationNo(self):
        connection = dbConn.getConnection()
        registration_no = input("Enter Registration no.: ")
        try:
            query = "delete from students where registration_no=%(registration_no)s;"
            cursor = connection.cursor()
            cursor.execute(query, {'registration_no': registration_no})
            connection.commit()
            print("Successfully deleted data!")
        except:
            print("Error! Something went wrong.")
        finally:
            connection.close()