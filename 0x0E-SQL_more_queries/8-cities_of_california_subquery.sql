-- cities of california
SELECT cities.name
FROM cities,states
WHERE states.name ="California"
AND cities.state_id = state_id
ORDER BY cities.id ASC;

