import db_connection as dbConn

class Create:
    def func_CreateData(self):
        connection = dbConn.getConnection()
        context = {
            'registration_no': input("Enter the Registration Number: "),
            'name': input("Enter the Name: "),
            'email': input("Enter the Email: "),
            'phone_no': input("Enter the Phone no.: "),
            'attendance': input("Enter the Attendance: "),
            'class_id': input("Enter the Class ID: "),
            'section': input("Enter the Section ID: ")
        }
        try:
            query = "Insert into students(registration_no, name, email, phone_no, attendance, class_id, section) values(%(registration_no)s,%(name)s,%(email)s,%(phone_no)s,%(attendance)s,%(class_id)s,%(section)s);"
            cursor = connection.cursor()
            cursor.execute(query, context)
            connection.commit()
            print("Successfully created data!")
        except:
            print("Error! Something went wrong.")
        finally:
            connection.close()