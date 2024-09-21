-- printing a full description of the first_table in the database
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'first_table'
AND TABLE_SCHEMA = 'hbtn_0c_0';


