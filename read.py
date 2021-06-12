import db_connection as dbConn

class Read:
    def func_ReadData(self):
        connection = dbConn.getConnection()
        try:
            query = "select * from students where attendance <= (select avg(d.attendance) as median from (select @rowindex:=@rowindex+1 as rowindex, students.attendance as attendance from students order by students.attendance) as d where d.rowindex in (floor(@rowindex/2), ceil(@rowindex/2)));"
            cursor = connection.cursor()
            cursor.execute("set @rowindex:=1;")
            cursor.execute(query)
            print("Defaulters List:")
            for row in cursor:
                print('%r' %(row,))
        except:
            print("Error! Something went wrong.")
        finally:
            connection.close()