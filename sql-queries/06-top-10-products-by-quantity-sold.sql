

	--***************************************************************
	-- Title: Top 10 Products by Quantity Sold
	-- By: R.Esmaeeli
	-- Date: 2026-06-30
	-- Version : 1.0
	-- Description: 
	-- Returns the top 10 products ranked by total quantity sold
	-- 
	--***************************************************************
	
	USE AdventureWorks2022
	GO

	SELECT TOP 10 
		p.Name AS ProductName ,
		SUM(sod.OrderQty) AS TotalQuantitySold	
	FROM Sales.SalesOrderDetail sod
		INNER JOIN Production.Product p on sod.ProductID = p.ProductID
	GROUP BY sod.ProductID , p.Name
	ORDER BY TotalQuantitySold DESC