-- includes the null
SELECT s.title, g.genre_id
FROM tv_shows s
LEFT OUTER JOIN tv_show_genres g
ON s.id = g.show_id
ORDER BY s.title, g.genre_id ASC;
