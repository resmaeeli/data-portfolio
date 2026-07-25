"""
Transform "01-top-actors-by-film-count.sql" query results into structured records.
"""


def transform_top_actors_by_film_count(rows):
    result = []

    for actor_id, first_name, last_name , film_count in rows:
        result.append({
            "ActorId": actor_id,
            "First Name": first_name,
            "Last Name":last_name, 
            "Film Count":film_count
            })

    return result
