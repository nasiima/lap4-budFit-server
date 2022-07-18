TABLE FOR USERS
DROP TABLE IF EXISTS users; CREATE TABLE users ( user_id serial PRIMARY KEY, name varchar(100), username varchar(20), email varchar(100), age int,password_digest varchar(1000), rating int, preferences varchar(100), likedby varchar(100), matches varchar(100), events varchar(100), rejected_events varchar(100), chats varchar(140) );

INSERT INTO users (name, username, email, age, password_digest, rating, preferences, likedby, matches, events, rejected_events, chats    ) VALUES ('test', 'usernametest', 'test@test.com', 18, 'test', 4, 'testsport', 'testlike', 'testmatche', 'testevent', 'rejectedtest', 'testchat');

------------------

TABLE FOR EVENTS 
DROP TABLE IF EXISTS events; CREATE TABLE events ( event_id serial PRIMARY KEY, user_id INT, FOREIGN KEY(user_id) REFERENCES users(user_id), activity varchar(64), descr varchar(100), location varchar(64), spaces varchar(100), age int, pic varchar(200), skilllevel varchar(64), time varchar(64), lookingfor varchar(64), partysize varchar(64));

INSERT INTO events ( user_id, activity, descr, location, spaces, age, pic, skilllevel, time, lookingfor, partysize) VALUES (29, 'activity', 'desc', 'location', 'spaces', 18, 'ss', 'skilllevel', 'time', 'lookingfor', 'partysize');

------------

TABLE FOR CHAT
DROP TABLE IF EXISTS chats; CREATE TABLE chats ( chat_id serial PRIMARY KEY, message_id INT, FOREIGN KEY(message_id) REFERENCES messages(message_id));

INSERT INTO chats ( message_id ) VALUES (2);

-----------

TABLE FOR CHAT
DROP TABLE IF EXISTS chats; CREATE TABLE chats ( chat_id serial PRIMARY KEY)


--------------


TABLE FOR MESSAGES
DROP TABLE IF EXISTS messages; CREATE TABLE messages ( message_id serial PRIMARY KEY, chat_id INT, FOREIGN KEY(chat_id) REFERENCES messages(chat_id));

INSERT INTO messages ( chat_id, ) VALUES (1);


-----------

TABLE FOR MESSAGES

DROP TABLE IF EXISTS messages; CREATE TABLE messages ( message_id serial PRIMARY KEY, user_id INT, FOREIGN KEY(user_id) REFERENCES users(user_id), comment VARCHAR(140), time VARCHAR(140));

INSERT INTO messages ( user_id, comment, time) VALUES (29, 'comment', 'time' );











