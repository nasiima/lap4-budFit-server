DROP TABLE IF EXISTS users; CREATE TABLE users ( user_id serial PRIMARY KEY, name varchar(100), email varchar(100), age int,password_digest varchar(1000), rating int, preferences varchar(100), likedby varchar(100), matches varchar(100), events varchar(100), 
rejected_events varchar(100), chats varchar(140) );



INSERT INTO users (name, email, age, password_digest, rating, preferences, likedby, matches, events, rejected_events, chats    ) VALUES ('test', 'test@test.com', 18, 'test', 4, 'testsport', 'testlike', 'testmatche', 'testevent', 'rejectedtest', 'testchat');