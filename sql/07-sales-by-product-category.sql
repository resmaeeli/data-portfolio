

	--*******************************************************************************
	-- Title: Sales by product category
	-- By: R.Esmaeeli
	-- Date: 2026-07-01
	-- Version : 1.0
	-- Description: 
	-- Returns the count of purchase and total amount of sales by product category
	-- 
	--*******************************************************************************
	
	SELECT 
		pc.Name AS CategoryName,
		SUM(sod.OrderQty) AS TotalQuantitySold,		
		SUM(sod.LineTotal) AS TotalSalesAmount
		
	FROM Sales.SalesOrderDetail sod
		INNER JOIN Production.Product p on sod.ProductID = p.ProductID
		INNER JOIN Production.ProductSubcategory psc on p.ProductSubcategoryID = psc.ProductSubcategoryID
		INNER JOIN Production.ProductCategory pc on pc.ProductCategoryID = psc.ProductCategoryID

	GROUP BY pc.ProductCategoryID , pc.Name