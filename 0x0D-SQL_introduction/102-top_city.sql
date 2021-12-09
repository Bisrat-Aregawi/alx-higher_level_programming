-- Print top 3 cities with high temp during july and august
SELECT city, AVG(value) 'avg_temp'FROM temperatures WHERE month=7 OR month=8
GROUP BY city ORDER BY AVG(value) DESC LIMIT 3;
