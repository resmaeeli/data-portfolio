

	--**********************************************************************
	-- Title: Average order value by year
	-- By: R.Esmaeeli
	-- Date: 2026-07-01
	-- Version : 1.0
	-- Description: 
	-- Returns the average value of the orders by year
	-- 
	--**********************************************************************
	
	USE AdventureWorks2022
	GO

	SELECT 
		YEAR(OrderDate) AS OrderYear,
		COUNT(*) AS OrderCount,
		AVG(TotalDue) AS AverageOrderValue
	
	FROM Sales.SalesOrderHeader
	GROUP BY YEAR(OrderDate)
	ORDER BY OrderYear DESC
		