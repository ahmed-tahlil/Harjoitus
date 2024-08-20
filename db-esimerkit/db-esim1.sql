-- 

CREATE USER user1@localhost IDENTIFIED BY 'salakala';
 -- Poistetaan tietokanta jos on olemassa
DROP DATABASE IF EXISTS ankkalinna;

-- Luodaan ankkalinnatietokanta

CREATE DATABASE ankkalinna;

-- Annetaan käyttäjän oikeuksia tietokantaan
GRANT SELECT, INSERT, UPDATE ON database_name.* TO username@localhost;
