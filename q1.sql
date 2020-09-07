SELECT 
name, 
votes,  
rank()  OVER ( order by votes desc )  AS 'rank'  
FROM votes;