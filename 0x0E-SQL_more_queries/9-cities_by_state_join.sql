-- List cities contained in database `hbtn_0d_usa`
-- Each record (row) should display: cities.id, cities.name, states.name
-- Results are sorted in ascending order by city id.
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states
ON states.id = cities.state_id;
