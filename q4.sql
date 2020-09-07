DROP TABLE IF EXISTS  bugs;
CREATE TABLE bugs(id INT(10), open_date TIMESTAMP, close_date TIMESTAMP, severity VARCHAR(10));
TRUNCATE TABLE bugs;
INSERT INTO bugs VALUES
(1,'2019-09-11','2019-10-02', '1'),
(2,'2019-09-12','2019-10-03', '3'),
(3,'2019-09-05','2019-10-03', '2'),
(4,'2019-08-20','2019-09-17', '3'),
(5,'2019-09-12',null, '1');

DELIMITER $$
DROP PROCEDURE IF EXISTS openBugs $$

CREATE 
	PROCEDURE openBugs(dateStart DATE, dateEnd DATE) 
	BEGIN
	DECLARE cnt INT DEFAULT 0;
	DROP TABLE IF EXISTS MisFechas;
	WHILE dateStart <= dateEnd DO
	SET cnt = (SELECT COUNT(*) AS COUNT FROM bugs WHERE DATE(open_date) <= dateStart AND DATE(close_date) >= dateStart);
	CREATE TEMPORARY TABLE IF NOT EXISTS MisFechas (
	myDate DATE,
	COUNT INT
	);
	INSERT INTO MisFechas (mydate, COUNT) VALUES (dateStart, cnt);
	SET dateStart = DATE_ADD(dateStart, INTERVAL 1 DAY);
	END WHILE;
	SELECT * FROM MisFechas;
	END $$

DELIMITER ;

call openBugs('2019-08-20','2019-09-17');