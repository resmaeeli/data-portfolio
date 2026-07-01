

	--**********************************************************************
	-- Title: Monthly sales growth
	-- By: R.Esmaeeli
	-- Date: 2026-07-01
	-- Version : 1.0
	-- Description: 
	-- Returns sales growth by month
	-- 
	--**********************************************************************
	
	USE AdventureWorks2022
	GO


	--===========  BEGIN CTE PART ===========--

	WITH MonthlySalesInfo AS(
	SELECT 
			YEAR(OrderDate) AS SalesYear,
			MONTH(OrderDate) AS SalesMonth,
			SUM(TotalDue) AS TotalSales,
			LAG(SUM(TotalDue),1,0)
			OVER (PARTITION BY YEAR(OrderDate) ORDER BY MONTH(OrderDate)) AS PreviousMonthSales				
		FROM Sales.SalesOrderHeader osh
		GROUP BY 
				YEAR(OrderDate) , 
				MONTH(OrderDate)		
	)
	--===========  END CTE PART ===========--
	SELECT 
			SalesYear,
			SalesMonth, 
			TotalSales,
			PreviousMonthSales,
			(TotalSales - PreviousMonthSales) AS GrowthAmount

	FROM MonthlySalesInfo

	ORDER BY 
		SalesYear,
		SalesMonth