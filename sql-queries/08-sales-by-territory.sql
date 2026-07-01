

	--**********************************************************************
	-- Title: Sales by terriroy
	-- By: R.Esmaeeli
	-- Date: 2026-07-01
	-- Version : 1.0
	-- Description: 
	-- Returns the count of orders and total sales amount per by territory
	-- 
	--**********************************************************************
	
	USE AdventureWorks2022
	GO

	SELECT 
		st.Name AS TerritoryName,
		Count(*) AS OrderCount,
		SUM(soh.TotalDue) AS TotalSalesAmount
		
	FROM Sales.SalesOrderHeader soh
		INNER JOIN Sales.SalesTerritory st on soh.TerritoryID = st.TerritoryID
	
	GROUP BY 
		soh.TerritoryID , 
		st.Name
	
	ORDER BY 
		OrderCount DESC, 
		TotalSalesAmount DESC