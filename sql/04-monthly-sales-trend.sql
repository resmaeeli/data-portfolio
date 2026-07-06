

	--**********************************************************
	-- Title: Monthly Sales Trend
	-- By: R.Esmaeeli
	-- Date: 2026-06-30
	-- Version : 1.0
	-- Description: 
	-- Returns monthly sales totals and order counts 
	-- grouped by year and month.	
	--**********************************************************
	
	SELECT
		YEAR(OrderDate) AS SalesYear , 
		MONTH(OrderDate) AS SalesMonth,
		COUNT(*) AS OrderCount,
		SUM(TotalDue) AS TotalSales
	FROM Sales.SalesOrderHeader	
	GROUP BY YEAR(OrderDate) , MONTH(OrderDate) 
	ORDER BY SalesYear , SalesMonth