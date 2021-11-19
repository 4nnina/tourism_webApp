-- Database: tourismdb
-- Update: 2021-09-14

-- 
-- CREATE TABLE: crowding
-- Rappresenta la classe: Occupazione del punto di interesse - 90
-- 

CREATE TABLE crowding (
	classid  varchar(70) NOT NULL,
	data  date  NOT NULL,
	date_creat  varchar(19) NOT NULL,
	val_real  double precision ,
	val_stim  double precision ,
	val_stor  double precision ,
	punto_di_interesse  varchar(70) NOT NULL
);


-- 
-- CREATE TABLE: log_vc
-- Rappresenta la classe: Log delle strisciate della veronacard - 91
-- 

CREATE TABLE log_vc (
	classid  varchar(70) NOT NULL,
	attivazione  date  NOT NULL,
	id_vc  varchar(40) NOT NULL,
	istante  varchar(19) NOT NULL,
	profilo  varchar(40) NOT NULL,
	poi  varchar(70) NOT NULL
);


-- 
-- CREATE TABLE: log_crowd
-- Rappresenta la classe: Log delle stime e dei dati reali di occupazione dei punti di interesse - 92
-- 

CREATE TABLE log_crowd (
	classid  varchar(70) NOT NULL,
	data  date  NOT NULL,
	data_creat  varchar(19) NOT NULL,
	val_real  double precision ,
	val_stim  double precision ,
	val_stor  double precision ,
	poi  varchar(70) NOT NULL
);


-- 
-- TABLE CONSTRAINT: crowding
-- PRIMARY KEY per la tabella della classe : Occupazione del punto di interesse - 90
-- 

ALTER TABLE crowding ADD CONSTRAINT crowding_PK PRIMARY KEY (classid);


-- 
-- TABLE CONSTRAINT: log_vc
-- PRIMARY KEY per la tabella della classe : Log delle strisciate della veronacard - 91
-- 

ALTER TABLE log_vc ADD CONSTRAINT log_vc_PK PRIMARY KEY (classid);


-- 
-- TABLE CONSTRAINT: log_crowd
-- PRIMARY KEY per la tabella della classe : Log delle stime e dei dati reali di occupazione dei punti di interesse - 92
-- 

ALTER TABLE log_crowd ADD CONSTRAINT log_crowd_PK PRIMARY KEY (classid);


-- 
-- TABLE CONSTRAINT: crowding
-- FOREIGN KEY per la tabella della classe : Occupazione del punto di interesse - 90
-- 

ALTER TABLE crowding ADD CONSTRAINT crowding_FK1 FOREIGN KEY (punto_di_interesse) REFERENCES  art (classid) ;


-- 
-- TABLE CONSTRAINT: log_vc
-- FOREIGN KEY per la tabella della classe : Log delle strisciate della veronacard - 91
-- 

ALTER TABLE log_vc ADD CONSTRAINT log_vc_FK1 FOREIGN KEY (poi) REFERENCES  art (classid) ;


-- 
-- TABLE CONSTRAINT: log_crowd
-- FOREIGN KEY per la tabella della classe : Log delle stime e dei dati reali di occupazione dei punti di interesse - 92
-- 

ALTER TABLE log_crowd ADD CONSTRAINT log_crowd_FK1 FOREIGN KEY (poi) REFERENCES  art (classid) ;


-- ALTER TABLE a_art_category_art_category ADD CONSTRAINT a_art_category_art_category_PK PRIMARY KEY (category ,points);

ALTER TABLE a_art_category_art_category ADD COLUMN id SERIAL UNIQUE NOT NULL;


--ALTER TABLE a_event_category_event_category ADD CONSTRAINT a_event_category_event_category_PK PRIMARY KEY (event ,category);

ALTER TABLE a_event_category_event_category ADD COLUMN id SERIAL UNIQUE NOT NULL;


-- ALTER TABLE a_art_tour_tour ADD CONSTRAINT a_art_tour_tour_PK PRIMARY KEY (point_of_interest ,tour);

ALTER TABLE a_art_tour_tour ADD COLUMN id SERIAL UNIQUE NOT NULL;


-- 
-- TABLE CONSTRAINT: event_category_name_trad_t
-- PRIMARY KEY e FOREIGN KEY per la tabella delle associzione binaria con attributi: Dt_multilingua - D01
-- 

ALTER TABLE event_category_name_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;


-- 
-- TABLE CONSTRAINT: news_descr_trad_t
-- PRIMARY KEY e FOREIGN KEY per la tabella delle associzione binaria con attributi: Dt_multilingua - D01
-- 

ALTER TABLE news_descr_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;


-- 
-- TABLE CONSTRAINT: news_title_trad_t
-- PRIMARY KEY e FOREIGN KEY per la tabella delle associzione binaria con attributi: Dt_multilingua - D01
-- 

ALTER TABLE news_title_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;


-- 
-- TABLE CONSTRAINT: benefit_vc_title_trad_t
-- PRIMARY KEY e FOREIGN KEY per la tabella delle associzione binaria con attributi: Dt_multilingua - D01
-- 

ALTER TABLE benefit_vc_title_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;


-- 
-- TABLE CONSTRAINT: art_category_name_trad_t
-- PRIMARY KEY e FOREIGN KEY per la tabella delle associzione binaria con attributi: Dt_multilingua - D01
-- 

ALTER TABLE art_category_name_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;


-- 
-- TABLE CONSTRAINT: benefit_vc_descr_trad_t
-- PRIMARY KEY e FOREIGN KEY per la tabella delle associzione binaria con attributi: Dt_multilingua - D01
-- 

ALTER TABLE benefit_vc_descr_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;


-- 
-- TABLE CONSTRAINT: media_name_trad_t
-- PRIMARY KEY e FOREIGN KEY per la tabella delle associzione binaria con attributi: Dt_multilingua - D01
-- 

ALTER TABLE media_name_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;


-- 
-- TABLE CONSTRAINT: art_descr_trad_t
-- PRIMARY KEY e FOREIGN KEY per la tabella delle associzione binaria con attributi: Dt_multilingua - D01
-- 

ALTER TABLE art_descr_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;


-- 
-- TABLE CONSTRAINT: retailer_category_name_trad_t
-- PRIMARY KEY e FOREIGN KEY per la tabella delle associzione binaria con attributi: Dt_multilingua - D01
-- 

ALTER TABLE retailer_category_name_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;


-- 
-- TABLE CONSTRAINT: rss_text_trad_t
-- PRIMARY KEY e FOREIGN KEY per la tabella delle associzione binaria con attributi: Dt_multilingua - D01
-- 

ALTER TABLE rss_text_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;


-- 
-- TABLE CONSTRAINT: rss_when_descr_trad_t
-- PRIMARY KEY e FOREIGN KEY per la tabella delle associzione binaria con attributi: Dt_multilingua - D01
-- 

ALTER TABLE rss_when_descr_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;


-- 
-- TABLE CONSTRAINT: event_name_trad_t
-- PRIMARY KEY e FOREIGN KEY per la tabella delle associzione binaria con attributi: Dt_multilingua - D01
-- 

ALTER TABLE event_name_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;


-- 
-- TABLE CONSTRAINT: event_descr_trad_t
-- PRIMARY KEY e FOREIGN KEY per la tabella delle associzione binaria con attributi: Dt_multilingua - D01
-- 

ALTER TABLE event_descr_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;


-- 
-- TABLE CONSTRAINT: benefit_vc_benefit_trad_t
-- PRIMARY KEY e FOREIGN KEY per la tabella delle associzione binaria con attributi: Dt_multilingua - D01
-- 

ALTER TABLE benefit_vc_benefit_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;


-- 
-- TABLE CONSTRAINT: art_name_trad_t
-- PRIMARY KEY e FOREIGN KEY per la tabella delle associzione binaria con attributi: Dt_multilingua - D01
-- 

ALTER TABLE art_name_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;


-- 
-- TABLE CONSTRAINT: tour_descr_trad_t
-- PRIMARY KEY e FOREIGN KEY per la tabella delle associzione binaria con attributi: Dt_multilingua - D01
-- 

ALTER TABLE tour_descr_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;


-- 
-- TABLE CONSTRAINT: tour_name_trad_t
-- PRIMARY KEY e FOREIGN KEY per la tabella delle associzione binaria con attributi: Dt_multilingua - D01
-- 

ALTER TABLE tour_name_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;


-- 
-- TABLE INDEX: crowding
-- INDEX per la tabella della classe : Occupazione del punto di interesse - 90
-- 

CREATE INDEX crowding_IN1 ON crowding(punto_di_interesse);


-- 
-- TABLE INDEX: log_vc
-- INDEX per la tabella della classe : Log delle strisciate della veronacard - 91
-- 

CREATE INDEX log_vc_IN1 ON log_vc(poi);


-- 
-- TABLE INDEX: log_crowd
-- INDEX per la tabella della classe : Log delle stime e dei dati reali di occupazione dei punti di interesse - 92
-- 

CREATE INDEX log_crowd_IN1 ON log_crowd(poi);


-- 
-- TABLE UNIQUE CONSTRAINT: crowding
-- UNIQUE CONSTRAINT per la tabella della classe : Occupazione del punto di interesse - 90
-- 

ALTER TABLE crowding ADD CONSTRAINT crowding_UN UNIQUE ( DATE_CREAT,Punto_di_interesse);


-- 
-- TABLE UNIQUE CONSTRAINT: log_crowd
-- UNIQUE CONSTRAINT per la tabella della classe : Log delle stime e dei dati reali di occupazione dei punti di interesse - 92
-- 

ALTER TABLE log_crowd ADD CONSTRAINT log_crowd_UN UNIQUE ( DATA_CREAT,POI);