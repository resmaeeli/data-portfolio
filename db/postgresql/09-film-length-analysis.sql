
    --*******************************************
    -- Title: Film Length Analysis Report
    -- By: R.Esmaeeli
    -- Date: 2026-07-25
    -- Version : 1.0
    -- Description:
    -- Returns film duration statistics grouped by length category.
    --
    --*******************************************


    SELECT
        CASE
            WHEN length < 60 THEN 'Short'
            WHEN length BETWEEN 60 AND 120 THEN 'Medium'
            ELSE 'Long'
        END AS length_category,
        COUNT(film_id) AS film_count,
        ROUND(AVG(length), 2) AS average_length
    FROM film
    GROUP BY
        CASE
            WHEN length < 60 THEN 'Short'
            WHEN length BETWEEN 60 AND 120 THEN 'Medium'
            ELSE 'Long'
        END
    ORDER BY
        film_count DESC;