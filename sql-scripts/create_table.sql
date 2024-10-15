CREATE TABLE PLAYLISTA (
	ID						varchar(255)	NOT NULL 	PRIMARY KEY,
	DATE 					datetime 		NOT NULL,
	TIME		 			datetime 		NOT NULL,
	TITLE 					varchar(255)	NOT NULL,
	ARTIST					varchar(255)	NOT NULL,
	FEAT					varchar(255),
	OTHERS_ARTISTS			varchar(255)
)

CREATE TABLE HOP_BEC (
	ID						varchar(255)	NOT NULL 	PRIMARY KEY,
	EDITION 				datetime 		NOT NULL,
	POSITION 				datetime 		NOT NULL,
	MUSIC_TITLE 			varchar(255)	NOT NULL,
	ARTIST					varchar(255)	NOT NULL,
	FEAT					varchar(255),
	OTHERS_ARTISTS			varchar(255)
)