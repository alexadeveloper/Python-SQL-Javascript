-- number the show linked
SELECT g.name as genre, COUNT(s.show_id) as number_of_shows
FROM tv_genres g INNER JOIN  tv_show_genres s
    ON g.id = s.genre_id
    GROUP BY genre
    ORDER BY number_of_shows DESC;
