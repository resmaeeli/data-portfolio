
    --*******************************************
    -- Title: Customer Activity Analysis Report
    -- By: R.Esmaeeli
    -- Date: 2026-07-25
    -- Version : 1.0
    -- Description:
    -- Returns customer rental activity and last rental date information.
    --
    --*******************************************


    SELECT
        c.customer_id,
        c.first_name,
        c.last_name,
        COUNT(r.rental_id) AS rental_count,
        MAX(r.rental_date) AS last_rental_date
    FROM customer c
    JOIN rental r
        ON c.customer_id = r.customer_id
    GROUP BY
        c.customer_id,
        c.first_name,
        c.last_name
    ORDER BY
        last_rental_date DESC;