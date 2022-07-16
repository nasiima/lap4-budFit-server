DROP TABLE IF EXISTS users; CREATE TABLE users ( user_id serial PRIMARY KEY, name varchar(100), username varchar(20), email varchar(100), age int,password_digest varchar(1000), rating int, preferences varchar(100), likedby varchar(100), matches varchar(100), events varchar(100), rejected_events varchar(100), chats varchar(140) );

INSERT INTO users (name, username, email, age, password_digest, rating, preferences, likedby, matches, events, rejected_events, chats    ) VALUES ('test', 'usernametest', 'test@test.com', 18, 'test', 4, 'testsport', 'testlike', 'testmatche', 'testevent', 'rejectedtest', 'testchat');


DROP TABLE IF EXISTS events; CREATE TABLE events ( event_id serial PRIMARY KEY,  activity varchar(64), descr varchar(100), location varchar(64), spaces varchar(100), age int, pic varchar(200), skilllevel varchar(64), time varchar(64), lookingfor varchar(64), partysize varchar(64));


INSERT INTO events ( activity, descr, location, spaces, age, pic, skilllevel, time, lookingfor, partysize) VALUES ('activity', 'desc', 'location', 'spaces', 18, 'ss', 'skilllevel', 'time', 'lookingfor', 'partysize');


FOREIGN KEY (user_id) REFERENCES Users (user_id),
 user_id,
 1

