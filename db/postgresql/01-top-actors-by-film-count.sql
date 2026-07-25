
    --*******************************************
    -- Title: Top Actors by Film Count Report
    -- By: R.Esmaeeli
    -- Date: 2026-07-25
    -- Version : 1.0
    -- Description:
    -- Returns top 10 actors ranked by the number of films they participated in.
    --
    --*******************************************


    SELECT
        a.actor_id,
        a.first_name,
        a.last_name,
        COUNT(f.film_id) AS film_count
    FROM actor a
    JOIN film_actor fa
        ON a.actor_id = fa.actor_id
    JOIN film f
        ON fa.film_id = f.film_id
    GROUP BY
        a.actor_id,
        a.first_name,
        a.last_name
    ORDER BY
        film_count DESC
    LIMIT 10;