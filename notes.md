NEW TABLE FOR USERS

---------------------------------------------------------------
DROP TABLE IF EXISTS users; CREATE TABLE users ( user_id serial PRIMARY KEY, name varchar(100), username VARCHAR(20), UNIQUE(username), email VARCHAR(100), dob DATE, password_digest VARCHAR(1000), preferences VARCHAR(1000), picture VARCHAR(1000) );


INSERT INTO users (name, username, email, dob, password_digest, preferences, picture   ) VALUES ('test', 'usernametest', 'test@test.com',  '12-03-13', 'PASS', 'testpref', 'picturetest');

---------------------------------------------------------------

TABLE FOR EVENTS 

---------------------------------------------------------------
DROP TABLE IF EXISTS events; CREATE TABLE events ( event_id serial PRIMARY KEY, activity varchar(64), title VARCHAR(100), descr varchar(100), location varchar(64), spaces varchar(100), date DATE);

INSERT INTO events (activity, title, descr, location, spaces, date) VALUES ('activity', 'title', 'desc', 'location', 'spaces', '2019-05-21' );


---------------------------------------------------------------

TABLE FOR Matches 

---------------------------------------------------------------

DROP TABLE IF EXISTS matches; CREATE TABLE matches (match_id serial PRIMARY KEY, user_id INT, FOREIGN KEY(user_id) REFERENCES users(user_id), event_id INT, FOREIGN KEY(event_id) REFERENCES events(event_id) );

INSERT INTO matches (user_id, event_id) VALUES (1, 1);















TABLE FOR CHAT

---------------------------------------------------------------
DROP TABLE IF EXISTS chats; CREATE TABLE chats ( chat_id serial PRIMARY KEY, message_id INT, FOREIGN KEY(message_id) REFERENCES messages(message_id));

INSERT INTO chats ( message_id ) VALUES (2);


---------------------------------------------------------------

TABLE FOR MESSAGES

---------------------------------------------------------------
DROP TABLE IF EXISTS messages; CREATE TABLE messages ( message_id serial PRIMARY KEY, user_id INT, FOREIGN KEY(user_id) REFERENCES users(user_id), comment VARCHAR(140), time VARCHAR(140));

INSERT INTO messages ( user_id, comment, time) VALUES (29, 'comment', 'time' );




-----------

TABLE FOR CHAT

DROP TABLE IF EXISTS chats; CREATE TABLE chats ( chat_id serial PRIMARY KEY)


--------------


TABLE FOR MESSAGES


DROP TABLE IF EXISTS messages; CREATE TABLE messages ( message_id serial PRIMARY KEY, chat_id INT, FOREIGN KEY(chat_id) REFERENCES messages(chat_id));

INSERT INTO messages ( chat_id, ) VALUES (1);







