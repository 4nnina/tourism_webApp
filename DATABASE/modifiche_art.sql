DROP VIEW public.v_art;

ALTER TABLE public.art ALTER COLUMN tickets TYPE TEXT;
ALTER TABLE public.art ALTER COLUMN open_time TYPE TEXT;

CREATE OR REPLACE VIEW public.v_art
 AS
 SELECT a.classid,
    a.descr_it,
    a.image_url,
    a.name_it,
    a.state,
    a.area_di_download,
    a.notes,
    a.open_time,
    a.tickets,
    a.rss,
    a.saving_vc,
    a.vc,
    min(at_en.name_trad_value::text) AS name_en,
    min(at_de.name_trad_value::text) AS name_de,
    min(at_fr.name_trad_value::text) AS name_fr,
    min(at_es.name_trad_value::text) AS name_es,
    min(dt_en.descr_trad_value) AS descr_en,
    min(dt_de.descr_trad_value) AS descr_de,
    min(dt_fr.descr_trad_value) AS descr_fr,
    min(dt_es.descr_trad_value) AS descr_es,
    min(ot_en.open_time_trad::text) AS open_time_en,
    min(ot_de.open_time_trad::text) AS open_time_de,
    min(ot_fr.open_time_trad::text) AS open_time_fr,
    min(ot_es.open_time_trad::text) AS open_time_es,
    min(ot_en.tickets_trad::text) AS tickets_en,
    min(ot_de.tickets_trad::text) AS tickets_de,
    min(ot_fr.tickets_trad::text) AS tickets_fr,
    min(ot_es.tickets_trad::text) AS tickets_es,
    min(ot_en.notes_trad::text) AS notes_en,
    min(ot_de.notes_trad::text) AS notes_de,
    min(ot_fr.notes_trad::text) AS notes_fr,
    min(ot_es.notes_trad::text) AS notes_es,
    string_agg(cat.name_it::text, ','::text) AS category_name_it,
    string_agg(ac_en.name_trad_value::text, ','::text) AS category_name_en,
    string_agg(ac_de.name_trad_value::text, ','::text) AS category_name_de,
    string_agg(ac_fr.name_trad_value::text, ','::text) AS category_name_fr,
    string_agg(ac_es.name_trad_value::text, ','::text) AS category_name_es,
    string_agg(at.tour::text, ','::text) AS tours_id,
    string_agg(t.name_it::text, ','::text) AS tours_name_it,
    string_agg(tt_en.name_trad_value::text, ','::text) AS tours_name_en,
    string_agg(tt_de.name_trad_value::text, ','::text) AS tours_name_de,
    string_agg(tt_fr.name_trad_value::text, ','::text) AS tours_name_fr,
    string_agg(tt_es.name_trad_value::text, ','::text) AS tours_name_es
   FROM art a
     JOIN a_art_category_art_category ac ON ac.points::text = a.classid::text
     JOIN art_category cat ON cat.classid::text = ac.category::text
     LEFT JOIN a_art_tour_tour at ON a.classid::text = at.point_of_interest::text
     LEFT JOIN tour t ON t.classid::text = at.tour::text
     LEFT JOIN art_category_name_trad_t ac_en ON ac_en.classref::text = cat.classid::text AND ac_en.name_trad_lang::text = 'en'::text
     LEFT JOIN art_category_name_trad_t ac_de ON ac_de.classref::text = cat.classid::text AND ac_de.name_trad_lang::text = 'de'::text
     LEFT JOIN art_category_name_trad_t ac_fr ON ac_fr.classref::text = cat.classid::text AND ac_fr.name_trad_lang::text = 'fr'::text
     LEFT JOIN art_category_name_trad_t ac_es ON ac_es.classref::text = cat.classid::text AND ac_es.name_trad_lang::text = 'es'::text
     LEFT JOIN tour_name_trad_t tt_en ON tt_en.classref::text = t.classid::text AND tt_en.name_trad_lang::text = 'en'::text
     LEFT JOIN tour_name_trad_t tt_de ON tt_de.classref::text = t.classid::text AND tt_de.name_trad_lang::text = 'de'::text
     LEFT JOIN tour_name_trad_t tt_fr ON tt_fr.classref::text = t.classid::text AND tt_fr.name_trad_lang::text = 'fr'::text
     LEFT JOIN tour_name_trad_t tt_es ON tt_es.classref::text = t.classid::text AND tt_es.name_trad_lang::text = 'es'::text
     LEFT JOIN art_name_trad_t at_en ON at_en.classref::text = a.classid::text AND at_en.name_trad_lang::text = 'en'::text
     LEFT JOIN art_name_trad_t at_de ON at_de.classref::text = a.classid::text AND at_de.name_trad_lang::text = 'de'::text
     LEFT JOIN art_name_trad_t at_fr ON at_fr.classref::text = a.classid::text AND at_fr.name_trad_lang::text = 'fr'::text
     LEFT JOIN art_name_trad_t at_es ON at_es.classref::text = a.classid::text AND at_es.name_trad_lang::text = 'es'::text
     LEFT JOIN art_descr_trad_t dt_en ON dt_en.classref::text = a.classid::text AND dt_en.descr_trad_lang::text = 'en'::text
     LEFT JOIN art_descr_trad_t dt_de ON dt_de.classref::text = a.classid::text AND dt_de.descr_trad_lang::text = 'de'::text
     LEFT JOIN art_descr_trad_t dt_fr ON dt_fr.classref::text = a.classid::text AND dt_fr.descr_trad_lang::text = 'fr'::text
     LEFT JOIN art_descr_trad_t dt_es ON dt_es.classref::text = a.classid::text AND dt_es.descr_trad_lang::text = 'es'::text
     LEFT JOIN art_trad_t ot_en ON ot_en.classref::text = a.classid::text AND ot_en.lang::text = 'en'::text
     LEFT JOIN art_trad_t ot_de ON ot_de.classref::text = a.classid::text AND ot_de.lang::text = 'de'::text
     LEFT JOIN art_trad_t ot_fr ON ot_fr.classref::text = a.classid::text AND ot_fr.lang::text = 'fr'::text
     LEFT JOIN art_trad_t ot_es ON ot_es.classref::text = a.classid::text AND ot_es.lang::text = 'es'::text
  WHERE a.state::text = '01'::text
  GROUP BY a.classid;

ALTER TABLE public.v_art
    OWNER TO postgres;

