
    --*******************************************
    -- Title: Film Rating Analysis Report
    -- By: R.Esmaeeli
    -- Date: 2026-07-25
    -- Version : 1.0
    -- Description:
    -- Returns film count and average duration grouped by film rating.
    --
    --*******************************************


    SELECT
        rating,
        COUNT(film_id) AS film_count,
        ROUND(AVG(length), 2) AS average_length
    FROM film
    GROUP BY
        rating
    ORDER BY
        film_count DESC;