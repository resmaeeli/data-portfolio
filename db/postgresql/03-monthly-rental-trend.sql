
    --*******************************************
    -- Title: Monthly Rental Trend Report
    -- By: R.Esmaeeli
    -- Date: 2026-07-25
    -- Version : 1.0
    -- Description:
    -- Returns monthly rental count and revenue trend based on rental activity.
    --
    --*******************************************


    SELECT
        DATE_TRUNC('month', r.rental_date) AS rental_month,
        COUNT(r.rental_id) AS rental_count,
        ROUND(SUM(p.amount), 2) AS total_revenue
    FROM rental r
    JOIN payment p
        ON r.rental_id = p.rental_id
    GROUP BY
        DATE_TRUNC('month', r.rental_date)
    ORDER BY
        rental_month;