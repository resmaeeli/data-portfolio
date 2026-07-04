"""
Export yearly order statistics from AdventureWorks to CSV.
"""

import pyodbc
import csv

## define connection string
connection_string = """
    DRIVER={ODBC Driver 17 for SQL Server};
    SERVER=localhost;
    DATABASE=AdventureWorks2022;
    UID=sa;
    PWD=sa;
    TrustServerCertificate=yes;
    """


## Defining query
query = """
	SELECT 
		YEAR(OrderDate) AS OrderYear,
		COUNT(*) AS OrderCount
	FROM Sales.SalesOrderHeader
	GROUP BY YEAR(OrderDate)
	ORDER BY OrderYear
    """

## Connect to odbc , using cursor and fetch data
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

cursor.execute(query)
rows = cursor.fetchall()

## Export query results to CSV
output_file_path =  "data/orders_per_year.csv"
with open(output_file_path, "w" , newline="" , encoding="utf-8") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Year" , "Count"])
    # csv_writer.writerows(rows)
    for year, count in rows:
        csv_writer.writerow([year, count])


# ## Print results to console
# for year, count in rows:
#     print(f"{year}, {count}")

## closing objects
cursor.close()
connection.close()