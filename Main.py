import db_connection as dbConn
from create import Create
from read import Read
from update import Update
from delete import Delete

def main():
    print("C=Create, R=Read, UA=Update Attendance, UEP=Update Email and Phone no., DRO=Delete using Roll no., DRE=Delete using Regidstration no.")
    operation = input("Enter operation: ")    
    if operation == 'C' or operation == 'c':
        createObj = Create()
        createObj.func_CreateData()
    elif operation == 'R' or operation == 'r':
        readObj = Read()
        readObj.func_ReadData()
    elif operation == 'UA':
        updateObj = Update()
        updateObj.func_UpdateAttendace()
    elif operation == 'UEP':
        updateObj = Update()
        updateObj.func_UpdateEmailPhone()
    elif operation == 'DRO':
        deleteObj = Delete()
        deleteObj.func_DeleteDataUsingRollNo()
    elif operation == 'DRE':
        deleteObj = Delete()
        deleteObj.func_DeleteDataUsingRegistrationNo()
    else:
        print("Invalid Operation!")
    
main()