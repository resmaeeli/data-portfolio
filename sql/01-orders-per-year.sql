

	--*******************************************
	-- Title: Orders Per Year Report
	-- By: R.Esmaeeli
	-- Date: 2026-06-29
	-- Version : 1.0
	-- Description: 
	-- Returns number of sales orders per year.
	--
	--*******************************************

	SELECT 
		YEAR(OrderDate) AS OrderYear,
		COUNT(*) AS OrderCount
	FROM Sales.SalesOrderHeader
	GROUP BY YEAR(OrderDate)
	ORDER BY OrderYear