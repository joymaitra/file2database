import xlrd
import sqlite3

def f2db(file,table_name):
    # variable list with initializations
    line_count = 0
    col_cnt = 0
    ins_str = ''

    # DB connection
    con = sqlite3.connect("database/sqlite_database.db")
    cur = con.cursor()

    create_str = "create table if not exists "+table_name+"("

    # count the number of columns and prepare the string with ?
    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)
    col_cnt=sheet.ncols
    row_count= sheet.nrows
    print(col_cnt)

    for i in range(col_cnt):
        if i == col_cnt-1:
            ins_str = ins_str+ '?)'
            create_str=create_str+sheet.cell_value(0, i)+" text)"
        elif  i == 0 :
            ins_str = ins_str + '(?,'
            create_str=create_str+sheet.cell_value(0, i)+' text,'
        else:
            ins_str=ins_str+"?,"
            create_str=create_str+sheet.cell_value(0, i)+' text,'
    print(ins_str)


    # create table 
    print(create_str)
    con.execute(create_str)


    # insert data into the table
    ins_str = "insert into "+ table_name+ " values"+ins_str
    for i in range(row_count):
        if i==0:
            pass
        else:
            cur.execute(ins_str,sheet.row_values(i))

    # commit and close the connection
    con.commit()
    con.close()
    return "completed"
