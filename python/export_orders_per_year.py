import pyodbc


connection_string = """
    DRIVER={ODBC Driver 17 for SQL Server};
    SERVER=localhost;
    DATABASE=AdventureWorks2022;
    UID=sa;
    PWD=sa;
    TrustServerCertificate=yes;
    """


query = """
	SELECT 
		YEAR(OrderDate) AS OrderYear,
		COUNT(*) AS OrderCount
	FROM Sales.SalesOrderHeader
	GROUP BY YEAR(OrderDate)
	ORDER BY OrderYear
    """


connection = pyodbc.connect(connection_string)
cursor  = connection.cursor()

cursor.execute(query)
rows = cursor.fetchall()

for year, count in rows:
    print(f"{year}: {count}")


cursor.close()
connection.close()