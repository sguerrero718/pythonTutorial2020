# pyodbc does not come by default and we must install it with pip
import pyodbc as pyodbc

# conn string for mssql
connStr = 'DRIVER={ODBC Driver 17 for SQL Server};Server=localhost\\SQLEXPRESS;Database=LOYALTY;Trusted_Connection=yes'


def getCustomers():
    list = []
    select = "SELECT * FROM [dbo].[CUSTOMER];"

    conn = pyodbc.connect(connStr)
    cursor = conn.cursor()
    cursor.execute(select)
    
    for row in cursor:
        list.append(row)

    return list 