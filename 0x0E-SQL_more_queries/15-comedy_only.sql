-- list all comedy shows
SELECT s.title
FROM tv_genres g, tv_show_genres sg, tv_shows s
WHERE g.name = 'Comedy'
AND sg.genre_id = g.id
AND s.id = sg.show_id
ORDER BY s.title ASC;
