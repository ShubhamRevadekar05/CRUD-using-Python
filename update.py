import db_connection as dbConn

class Update:
    def func_UpdateAttendace(self):
        connection = dbConn.getConnection()
        roll_no = input("Enter Roll no.: ")
        try:
            query = "Select * from students where roll_no=%(roll_no)s;"
            cursor = connection.cursor()
            cursor.execute(query, {'roll_no': roll_no})
            item = cursor.fetchone()
            if item:
                new_attendance = input("Enter New Attendance: ")
                query = "Update students set attendance=%(new)s where roll_no=%(roll_no)s;"
                context = {
                    'new': new_attendance,
                    'roll_no': roll_no
                }
                cursor.execute(query, context)
                connection.commit()
                print("Successfully updated data!")
            else:
                print("Item not found!")
        except:
            print("Error! Something went wrong.")
        finally:
            connection.close()

    def func_UpdateEmailPhone(self):
        connection = dbConn.getConnection()
        roll_no = input("Enter Roll no.: ")
        try:
            query = "select * from students where roll_no=%(roll_no)s;"
            cursor = connection.cursor()
            cursor.execute(query, {'roll_no': roll_no})
            item = cursor.fetchone()
            if item:
                new_Email = input("Enter New Email: ")
                new_Phone = input("Enter New Phone: ")
                query = "Update students set email=%(email)s, phone_no=%(phone)s where roll_no=%(roll_no)s;"
                context = {
                    'email': new_Email,
                    'phone': new_Phone,
                    'roll_no': roll_no
                }
                cursor.execute(query, context)
                connection.commit()
                print("Successfully updated data!")
            else:
                print("Item not found!")
        except:
             print("Error! Something went wrong.")
        finally:
            connection.close()