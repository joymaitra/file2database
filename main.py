import csv2db
import xlsx2db

# user inputs
file = input("file name ( *full path required): ")
table_name = input("target table name : ")

if '.csv' in file:
    response=csv2db.f2db(file,table_name)
    print(response)
elif '.xlsx' in file:
    response=xlsx2db.f2db(file,table_name)
    print(response)
else:
    print("not a valid format")