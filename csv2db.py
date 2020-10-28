import csv
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
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if line_count == 0:
                col_cnt = len(row)
                line_count +=1
                for col in row:
                    if col == row[col_cnt-1]:
                        create_str = create_str + col + " text)"
                    else:
                        create_str = create_str + col + " text,"
            else:
                line_count +=1
    print(line_count-1)
    for i in range(col_cnt):
        if i == col_cnt-1:
            ins_str = ins_str+ '?)'
        elif  i == 0 :
            ins_str = ins_str + '(?,'
        else:
            ins_str=ins_str+"?,"
    print(ins_str)

    # create table 
    print(create_str)
    con.execute(create_str)

    # insert data into the table
    data = open(file)
    rows = csv.reader(data)
    next(rows)
    ins_str = "insert into "+ table_name+ " values"+ins_str
    cur.executemany(ins_str,rows)

    # commit and close the connection
    con.commit()
    con.close()
    return "completed"