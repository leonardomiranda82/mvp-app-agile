DROP TABLE IF EXISTS messages;

CREATE TABLE messages (
    id serial PRIMARY KEY,
    message_text varchar (150) NOT NULL
);

INSERT INTO messages (message_text) VALUES ('Hello World, PostgreSQL!');

