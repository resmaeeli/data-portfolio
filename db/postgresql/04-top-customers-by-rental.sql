
    --*******************************************
    -- Title: Top Customers by Rental Count Report
    -- By: R.Esmaeeli
    -- Date: 2026-07-25
    -- Version : 1.0
    -- Description:
    -- Returns top 10 customers ranked by number of rented films.
    --
    --*******************************************


    SELECT
        c.customer_id,
        c.first_name,
        c.last_name,
        COUNT(r.rental_id) AS rental_count
    FROM customer c
    JOIN rental r
        ON c.customer_id = r.customer_id
    GROUP BY
        c.customer_id,
        c.first_name,
        c.last_name
    ORDER BY
        rental_count DESC
    LIMIT 10;