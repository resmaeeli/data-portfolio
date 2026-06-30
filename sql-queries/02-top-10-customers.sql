

	--****************************************************
	-- Title: Top 10 Customers by Total Purchase Amount
	-- By: R.Esmaeeli
	-- Date: 2026-06-29
	-- Version : 1.0
	-- Description: 
	-- Returns top 10 customers by total purchase amount
	--
	--****************************************************
	
	SELECT TOP 10 
	Store.Name AS StoreName, 
	(Person.FirstName + ' ' + Person.LastName) AS PersonName ,
	SUM(SalesOrderHeader.TotalDue) AS TotalPurchasedAmount 
		FROM Sales.SalesOrderHeader
		JOIN Sales.Customer on SalesOrderHeader.CustomerID = Customer.CustomerID
		LEFT JOIN Sales.Store on Customer.StoreID = Store.BusinessEntityID 
		LEFT JOIN Person.Person ON Customer.PersonID = Person.Person.BusinessEntityID
	GROUP BY  Customer.CustomerID , Store.Name , Person.FirstName, Person.LastName
	ORDER BY SUM(SalesOrderHeader.TotalDue) DESC