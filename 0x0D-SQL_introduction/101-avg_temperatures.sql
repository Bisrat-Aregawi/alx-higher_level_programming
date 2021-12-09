-- Print average temperatures by city ordered descending
SELECT city, AVG(value) 'avg_temp' From temperatures GROUP BY city ORDER BY AVG(value) DESC;
