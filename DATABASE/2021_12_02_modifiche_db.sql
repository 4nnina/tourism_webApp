--
-- Aggiunti id nelle tabelle per il funzionamento del framework django
--
ALTER TABLE art_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;
ALTER TABLE rss_title_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;

--
--classid da character varying a serial
--
ALTER TABLE log_vc DROP COLUMN classid;
ALTER TABLE log_vc ADD COLUMN classid SERIAL UNIQUE NOT NULL;
ALTER TABLE log_vc ADD CONSTRAINT log_vc_PK PRIMARY KEY (classid);

ALTER TABLE log_crowd DROP COLUMN classid;
ALTER TABLE log_crowd ADD COLUMN classid SERIAL UNIQUE NOT NULL;
ALTER TABLE log_crowd ADD CONSTRAINT log_crowd_PK PRIMARY KEY (classid);

ALTER TABLE crowding DROP COLUMN classid;
ALTER TABLE crowding ADD COLUMN classid SERIAL UNIQUE NOT NULL;
ALTER TABLE crowding ADD CONSTRAINT crowding_PK PRIMARY KEY (classid);

--aggiunta "riduzione percentuale" per distinzione da "ridotto fisso"
INSERT INTO d_e_vc (code, name, alphacode) VALUES ('02', 'riduzione percentuale', 'RIDPERC');

--consistenza dei codici
UPDATE public.art SET vc = '01' WHERE saving_vc<>0;
UPDATE public.art SET vc = '02' WHERE saving_vc=0.5;
UPDATE public.art SET saving_vc = 1 WHERE vc='00';

--tabelle servizi
CREATE TABLE log_lang_preferences (
	device_id  varchar(70) NOT NULL,
	time  timestamp NOT NULL,
	platform  varchar(70),
	device_lang  varchar(70),
	select_lang  varchar(70),
	id SERIAL UNIQUE NOT NULL PRIMARY KEY,
	UNIQUE(device_id, time)
);

CREATE TABLE log_user_location (
	device_id  varchar(70) NOT NULL,
	time  timestamp NOT NULL,
	coordinates  geometry(Point,4326),
	accuracy  double precision,
	id SERIAL UNIQUE NOT NULL PRIMARY KEY,
	UNIQUE(device_id,time)
);



