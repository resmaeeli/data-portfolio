
    --*******************************************
    -- Title: Top Films by Rental Frequency Report
    -- By: R.Esmaeeli
    -- Date: 2026-07-25
    -- Version : 1.0
    -- Description:
    -- Returns top 10 films ranked by number of rentals.
    --
    --*******************************************


    SELECT
        f.film_id,
        f.title,
        COUNT(r.rental_id) AS rental_count,
        ROUND(SUM(p.amount), 2) AS total_revenue
    FROM film f
    JOIN inventory i
        ON f.film_id = i.film_id
    JOIN rental r
        ON i.inventory_id = r.inventory_id
    JOIN payment p
        ON r.rental_id = p.rental_id
    GROUP BY
        f.film_id,
        f.title
    ORDER BY
        rental_count DESC
    LIMIT 10;