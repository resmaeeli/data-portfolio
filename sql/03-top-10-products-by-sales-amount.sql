

	--****************************************************
	-- Title: Top 10 Products by Sales Amount
	-- By: R.Esmaeeli
	-- Date: 2026-06-30
	-- Version : 1.0
	-- Description: 
	-- Returns top 10 products by total purchase amount
	--
	--****************************************************


	SELECT TOP 10 
		sod.ProductID, 
		pr.Name AS ProductName,
		SUM(sod.LineTotal) AS TotalSalesAmount
	FROM Sales.SalesOrderDetail AS sod
		INNER JOIN Production.Product AS pr on sod.ProductID = pr.ProductID
	GROUP BY sod.ProductID , pr.Name
	ORDER BY TotalSalesAmount DESC
