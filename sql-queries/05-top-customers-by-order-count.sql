

	--***************************************************************
	-- Title: Top 10 Customers by Number of Orders
	-- By: R.Esmaeeli
	-- Date: 2026-06-30
	-- Version : 1.0
	-- Description: 
	-- Returns the top 10 customers ranked by number of sales orders
	-- 
	--***************************************************************
	
	USE AdventureWorks2022
	GO

	SELECT TOP 10 
		COALESCE(
				Store.Name,
				p.FirstName + ' ' + p.LastName
			) AS CustomerName,
		soh.CustomerID, 		
		COUNT(*) AS OrderCount
	FROM Sales.SalesOrderHeader soh
		INNER JOIN Sales.Customer c ON soh.CustomerID = c.CustomerID
		LEFT JOIN Sales.Store on c.StoreID = Store.BusinessEntityID 
		LEFT JOIN Person.Person p ON c.PersonID = p.BusinessEntityID
	GROUP BY soh.CustomerID , Sales.Store.Name , p.FirstName , p.LastName
	ORDER BY OrderCount DESC


	