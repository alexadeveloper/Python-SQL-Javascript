-- cities from a state
SELECT c.id, c.name
FROM states s, cities c
WHERE c.state_id = s.id
AND s.name = 'California'
ORDER BY c.id;
