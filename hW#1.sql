#1 How many airplanes have listed speeds?  Whats the 
minimum listed speed & the maximum listed speed? 

SELECT COUNT(*) FROM planes
	WHERE speed IS NOT NULL;
SELECT COUNT(speed) FROM planes;

SELECT MAX(speed) FROM planes;
SELECT MIN(speed) FROM planes; 

#2. Whats the total distance flown #by all of the planes #in January #2013? 
# Whats the total distance flown b#y all of the planes #in January 2#013 #where the tailnum #is missing?
SELECT COUNT(*) AS 'Number of Flights', SUM(distance) AS 'Total Distance' FROM flights;
SELECT COUNT(*) AS 'Number of Flights', SUM(distance) AS 'Total Distance' FROM flights
	WHERE (year = 2013 AND month = 1);

SELECT COUNT(tailnum) FROM flights;		
SELECT COUNT(*) FROM flights
	WHERE tailnum IS NOT NULL;			
SELECT COUNT(*) FROM flights
	WHERE tailnum IS NULL;				

SELECT COUNT(*) AS 'Number of Flights', SUM(distance) AS 'Total Distance' FROM flights
	WHERE (year = 2013 AND month = 1)
    AND tailnum IS NULL;
    
    #3
    sELECT COUNT(*) AS 'Number of Flights', SUM(distance) AS 'Total Distance', manufacturer AS 'Manufacturer'
FROM flights
INNER JOIN planes
ON flights.tailnum = planes.tailnum
WHERE (flights.year = 2013 AND flights.month = 7 AND flights.day = 5)
GROUP BY manufacturer;

SELECT COUNT(*) AS 'Number of Flights', SUM(distance) AS 'Total Distance', manufacturer AS 'Manufacturer'
FROM flights
LEFT JOIN planes
ON flights.tailnum = planes.tailnum
WHERE (flights.year = 2013 AND flights.month = 7 AND flights.day = 5)
GROUP BY manufacturer;
