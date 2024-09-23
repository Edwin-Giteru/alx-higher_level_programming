CREATE USER if not exists 'user_0d_1'@'localhost' IDENTIFIED BY 'Proot@01';
CREATE USER if not exists 'user_0d_2'@'localhost' IDENTIFIED BY 'Proot@01';


-- list privileges of user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';
-- list privileges of user_0d_2
SHOW GRANTS FOR'user_0d_2'@'localhost';
