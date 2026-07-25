
    --*******************************************
    -- Title: Film Category Analysis Report
    -- By: R.Esmaeeli
    -- Date: 2026-07-25
    -- Version : 1.0
    -- Description:
    -- Returns film count and average duration grouped by film category.
    --
    --*******************************************


    SELECT
        c.category_id,
        c.name AS category_name,
        COUNT(f.film_id) AS film_count,
        ROUND(AVG(f.length), 2) AS average_length
    FROM category c
    JOIN film_category fc
        ON c.category_id = fc.category_id
    JOIN film f
        ON fc.film_id = f.film_id
    GROUP BY
        c.category_id,
        c.name
    ORDER BY
        film_count DESC;