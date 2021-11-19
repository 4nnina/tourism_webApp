
-- 
-- CREATE TABLE: art_visiting_time
-- Rappresenta la classe: Dati storici sulla durata delle visite dei punti di interesse storico - 94
-- 

CREATE TABLE art_visiting_time (
	classid  varchar(70) NOT NULL,
	end_date  date ,
	poi_visiting_time  numeric(15,0)  NOT NULL,
	start_date  date  NOT NULL,
	poi  varchar(70) NOT NULL
);

-- 
-- CREATE TABLE: art_capacity
-- Rappresenta la classe: Dati storici sulla capienza dei punti di interesse artistico - 93
-- 

CREATE TABLE art_capacity (
	classid  varchar(70) NOT NULL,
	end_date  date ,
	poi_cap  numeric(15,0)  NOT NULL,
	start_date  date  NOT NULL,
	poi  varchar(70) NOT NULL
);


-- 
-- TABLE CONSTRAINT: art_visiting_time
-- PRIMARY KEY per la tabella della classe : Dati storici sulla durata delle visite dei punti di interesse storico - 94
-- 

ALTER TABLE art_visiting_time ADD CONSTRAINT art_visiting_time_PK PRIMARY KEY (classid);


-- 
-- TABLE CONSTRAINT: art_capacity
-- PRIMARY KEY per la tabella della classe : Dati storici sulla capienza dei punti di interesse artistico - 93
-- 

ALTER TABLE art_capacity ADD CONSTRAINT art_capacity_PK PRIMARY KEY (classid);

-- 
-- TABLE CONSTRAINT: art_visiting_time
-- FOREIGN KEY per la tabella della classe : Dati storici sulla durata delle visite dei punti di interesse storico - 94
-- 

ALTER TABLE art_visiting_time ADD CONSTRAINT art_visiting_time_FK1 FOREIGN KEY (poi) REFERENCES  art (classid) ;

-- 
-- TABLE CONSTRAINT: art_capacity
-- FOREIGN KEY per la tabella della classe : Dati storici sulla capienza dei punti di interesse artistico - 93
-- 

ALTER TABLE art_capacity ADD CONSTRAINT art_capacity_FK1 FOREIGN KEY (poi) REFERENCES  art (classid) ;

-- 
-- TABLE INDEX: art_visiting_time
-- INDEX per la tabella della classe : Dati storici sulla durata delle visite dei punti di interesse storico - 94
-- 

CREATE INDEX art_visiting_time_IN1 ON art_visiting_time(poi);

-- 
-- TABLE INDEX: art_capacity
-- INDEX per la tabella della classe : Dati storici sulla capienza dei punti di interesse artistico - 93
-- 

CREATE INDEX art_capacity_IN1 ON art_capacity(poi);


-- 
-- TABLE UNIQUE CONSTRAINT: art_visiting_time
-- UNIQUE CONSTRAINT per la tabella della classe : Dati storici sulla durata delle visite dei punti di interesse storico - 94
-- 

ALTER TABLE art_visiting_time ADD CONSTRAINT art_visiting_time_UN UNIQUE ( START_DATE,POI);


-- 
-- TABLE UNIQUE CONSTRAINT: art_capacity
-- UNIQUE CONSTRAINT per la tabella della classe : Dati storici sulla capienza dei punti di interesse artistico - 93
-- 

ALTER TABLE art_capacity ADD CONSTRAINT art_capacity_UN UNIQUE ( START_DATE,POI);


ALTER TABLE log_crowd ALTER COLUMN data TYPE timestamp with time zone USING data::timestamp with time zone;
ALTER TABLE log_crowd ALTER COLUMN data_creat TYPE timestamp with time zone USING data_creat::timestamp with time zone;

ALTER TABLE crowding ALTER COLUMN data TYPE timestamp with time zone USING data::timestamp with time zone;
ALTER TABLE crowding ALTER COLUMN date_creat TYPE timestamp with time zone USING date_creat::timestamp with time zone;



