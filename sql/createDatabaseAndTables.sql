CREATE DATABASE test CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

use test;

CREATE TABLE users (
    id int(11) NOT NULL AUTO_INCREMENT,
    email varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB;

-- encode the password with a "one way hash code" - it means the database stores this value:
--     f857606c76b9d72353257dbd273c9b9e
-- if someone stole the data from the database, they would never know the password, as it is almost impossible to
-- calculate it from that string. if we want to check someone knows the password, we take what they give us, and
-- use the MD5 function to encode what they give us and we compare that to the database
insert into users (email, password)
    values ('ant@somerandomdomain.com', MD5('mySecretPassword'))
;

-- example for checking if the person knows the password:
select *
from users
where email = 'ant@somerandomdomain.com'
    AND password = MD5('some wrong password that a hacker gave use'); -- returns no results! :-)
-- Empty set (0.00 sec)
