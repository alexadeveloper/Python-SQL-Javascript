-- genres of the show dexter
SELECT g.name
FROM tv_genres g, tv_show_genres sg, tv_shows s
WHERE s.title = 'Dexter'
AND sg.show_id = s.id
AND g.id = sg.genre_id
ORDER BY g.name;
