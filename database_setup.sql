-- Database: spotify_playlist_db
-- Description: This script creates a MySQL database and a table to store Spotify playlist data.
-- It also includes a procedure to load data from a CSV file into the table.
-- Author: [Aswin Kumar R]

create database if not exists `spotify_playlist_db';
use `spotify_playlist_db';

-- Create the Function (MYSQL)
-- CREATE TABLE
DELIMITER //

CREATE PROCEDURE spotify_table()
BEGIN

DROP TABLE IF EXISTS `spotify_playlist_data`;
CREATE TABLE IF NOT EXISTS spotify_playlist (
    id INT AUTO_INCREMENT PRIMARY KEY,
    track_name VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    popularity INT,
    duration_minutes FLOAT
)

END//
DELIMITER ;

-- Call the Function (MYSQL)
CALL spotify_table();


-- Create the Table (MYSQL)
-- INSERT DATA (Bulk Insert csv to database)

DELIMITER //

CREATE PROCEDURE Load_Table1()
BEGIN
    -- Declare variables for dynamic SQL
    DECLARE sql_query VARCHAR(1000);
    
    -- Truncate tables before loading
    SET @sql_query = 'TRUNCATE TABLE spotify_playlist;';
    PREPARE stmt FROM @sql_query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;


    -- Load Data using dynamic SQL
    SET @sql_query = "LOAD DATA LOCAL INFILE 'E:/Python_Projects/spotify_projects/spotify_playlist_data.csv'
                      INTO TABLE spotify_playlist
                      FIELDS TERMINATED BY ','  
                      ENCLOSED BY '\"'  
                      LINES TERMINATED BY '\n'  
                      IGNORE 1 ROWS;";
    PREPARE stmt FROM @sql_query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

END //

DELIMITER ;