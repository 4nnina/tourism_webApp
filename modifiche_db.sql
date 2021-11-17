-- aggiunti id nelle tabelle

ALTER TABLE public.art_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;

ALTER TABLE public.rss_title_trad_t ADD COLUMN id SERIAL UNIQUE NOT NULL;

--classid non più character varying
ALTER TABLE log_vc DROP COLUMN classid;
ALTER TABLE log_vc ADD COLUMN classid SERIAL UNIQUE NOT NULL;
ALTER TABLE log_vc ADD CONSTRAINT log_vc_PK PRIMARY KEY (classid);

ALTER TABLE log_crowd DROP COLUMN classid;
ALTER TABLE log_crowd ADD COLUMN classid SERIAL UNIQUE NOT NULL;
ALTER TABLE log_crowd ADD CONSTRAINT log_crowd_PK PRIMARY KEY (classid);

ALTER TABLE crowding DROP COLUMN classid;
ALTER TABLE crowding ADD COLUMN classid SERIAL UNIQUE NOT NULL;
ALTER TABLE crowding ADD CONSTRAINT crowding_PK PRIMARY KEY (classid);

--saving_vc a null dove zero

