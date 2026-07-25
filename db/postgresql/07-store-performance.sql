
    --*******************************************
    -- Title: Store Performance Analysis Report
    -- By: R.Esmaeeli
    -- Date: 2026-07-25
    -- Version : 1.0
    -- Description:
    -- Returns rental count and revenue performance by store.
    --
    --*******************************************


    SELECT
        s.store_id,
        c.city,
        co.country,
        COUNT(r.rental_id) AS rental_count,
        ROUND(SUM(p.amount), 2) AS total_revenue
    FROM store s
    JOIN address a
        ON s.address_id = a.address_id
    JOIN city c
        ON a.city_id = c.city_id
    JOIN country co
        ON c.country_id = co.country_id
    JOIN inventory i
        ON s.store_id = i.store_id
    JOIN rental r
        ON i.inventory_id = r.inventory_id
    JOIN payment p
        ON r.rental_id = p.rental_id
    GROUP BY
        s.store_id,
        c.city,
        co.country
    ORDER BY
        total_revenue DESC;