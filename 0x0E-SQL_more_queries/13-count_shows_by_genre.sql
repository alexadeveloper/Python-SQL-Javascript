-- number the show linked
SELECT g.name as 'genre', COUNT(s.genre_id) as 'number_shows'
FROM tv_genres g
INNER JOIN  tv_show_genres s
ON s.genre_id = g.id
GROUP BY g.id
ORDER BY COUNT(s.genre_id) DESC;
