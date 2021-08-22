#from django.db import models
from django.contrib.gis.db import models
from django.db.models import CheckConstraint, Q


class AArtCategoryArtCategory(models.Model):
    id_Category_Points = models.AutoField(primary_key=True)
    category = models.ForeignKey('ArtCategory', models.DO_NOTHING, db_column='category')
    points = models.ForeignKey('Art', models.DO_NOTHING, db_column='points')

    class Meta:
        managed = False
        db_table = 'a_art_category_art_category'
        unique_together = (('category', 'points'),)


class AArtTourTour(models.Model):
    id_Point_of_interest_Tour = models.AutoField(primary_key=True)
    point_of_interest = models.ForeignKey('Art', models.DO_NOTHING, db_column='point_of_interest')
    tour = models.ForeignKey('Tour', models.DO_NOTHING, db_column='tour')
    num = models.DecimalField(max_digits=15, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'a_art_tour_tour'
        unique_together = (('point_of_interest', 'tour'),)


class AEventCategoryEventCategory(models.Model):
    id_Event_Category = models.AutoField(primary_key=True)
    event = models.ForeignKey('Event', models.DO_NOTHING, db_column='event')
    category = models.ForeignKey('EventCategory', models.DO_NOTHING, db_column='category')

    class Meta:
        managed = False
        db_table = 'a_event_category_event_category'
        unique_together = (('event', 'category'),)


class Art(models.Model):
    classid = models.CharField(primary_key=True, max_length=70)
    descr_it = models.TextField(blank=True, null=True)
    image_url = models.CharField(max_length=200, blank=True, null=True)
    name_it = models.CharField(max_length=100)
    state = models.ForeignKey('DArtEStato', models.DO_NOTHING, db_column='state')
    area_di_download = models.GeometryField(blank=True, null=True)
    notes = models.CharField(max_length=1024, blank=True, null=True)
    open_time = models.CharField(max_length=1024, blank=True, null=True)
    tickets = models.CharField(max_length=1024, blank=True, null=True)
    rss = models.CharField(max_length=30, blank=True, null=True)
    saving_vc = models.FloatField()
    vc = models.CharField(max_length=80)
    vc_id = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'art'


class ArtCategory(models.Model):
    classid = models.CharField(primary_key=True, max_length=70)
    name_it = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'art_category'


class ArtCategoryNameTradT(models.Model):
    id_Classref_Name_trad_lang_Name_trad_value = models.AutoField(primary_key=True)
    classref = models.ForeignKey(ArtCategory, models.DO_NOTHING, db_column='classref')
    name_trad_lang = models.ForeignKey('DELang', models.DO_NOTHING, db_column='name_trad_lang')
    name_trad_value = models.CharField(max_length=16384)

    class Meta:
        managed = False
        db_table = 'art_category_name_trad_t'
        unique_together = (('classref', 'name_trad_lang', 'name_trad_value'),)


class ArtDescrTradT(models.Model):
    id_Classref_Descr_trad_lang = models.AutoField(primary_key=True)
    classref = models.ForeignKey(Art, models.DO_NOTHING, db_column='classref')
    descr_trad_lang = models.ForeignKey('DELang', models.DO_NOTHING, db_column='descr_trad_lang')
    descr_trad_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'art_descr_trad_t'
        unique_together = (('classref', 'descr_trad_lang'),)


class ArtNameTradT(models.Model):
    id_Classref_Name_trad_lang_Name_trad_value = models.AutoField(primary_key=True)
    classref = models.ForeignKey(Art, models.DO_NOTHING, db_column='classref')
    name_trad_lang = models.ForeignKey('DELang', models.DO_NOTHING, db_column='name_trad_lang')
    name_trad_value = models.CharField(max_length=16384)

    class Meta:
        managed = False
        db_table = 'art_name_trad_t'
        unique_together = (('classref', 'name_trad_lang', 'name_trad_value'),)


class ArtTradT(models.Model):
    classref = models.ForeignKey(Art, models.DO_NOTHING, db_column='classref', blank=True, null=True)
    lang = models.CharField(max_length=80, blank=True, null=True)
    notes_trad = models.CharField(max_length=16384, blank=True, null=True)
    open_time_trad = models.CharField(max_length=16384, blank=True, null=True)
    tickets_trad = models.CharField(max_length=16384, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'art_trad_t'


class BenefitVc(models.Model):
    classid = models.CharField(primary_key=True, max_length=70)
    benefit = models.CharField(max_length=1024)
    descr = models.CharField(max_length=2048)
    title = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'benefit_vc'


class BenefitVcBenefitTradT(models.Model):
    id_Classref_Benefit_trad_lang_Benefit_trad_value = models.AutoField(primary_key=True)
    classref = models.ForeignKey(BenefitVc, models.DO_NOTHING, db_column='classref')
    benefit_trad_lang = models.ForeignKey('DELang', models.DO_NOTHING, db_column='benefit_trad_lang')
    benefit_trad_value = models.CharField(max_length=16384)

    class Meta:
        managed = False
        db_table = 'benefit_vc_benefit_trad_t'
        unique_together = (('classref', 'benefit_trad_lang', 'benefit_trad_value'),)


class BenefitVcDescrTradT(models.Model):
    id_Classref_Descr_trad_lang_Descr_trad_value = models.AutoField(primary_key=True)
    classref = models.ForeignKey(BenefitVc, models.DO_NOTHING, db_column='classref')
    descr_trad_lang = models.ForeignKey('DELang', models.DO_NOTHING, db_column='descr_trad_lang')
    descr_trad_value = models.CharField(max_length=16384)

    class Meta:
        managed = False
        db_table = 'benefit_vc_descr_trad_t'
        unique_together = (('classref', 'descr_trad_lang', 'descr_trad_value'),)


class BenefitVcTitleTradT(models.Model):
    id_Classref_Title_trad_lang_Title_trad_value = models.AutoField(primary_key=True)
    classref = models.ForeignKey(BenefitVc, models.DO_NOTHING, db_column='classref')
    title_trad_lang = models.ForeignKey('DELang', models.DO_NOTHING, db_column='title_trad_lang')
    title_trad_value = models.CharField(max_length=16384)

    class Meta:
        managed = False
        db_table = 'benefit_vc_title_trad_t'
        unique_together = (('classref', 'title_trad_lang', 'title_trad_value'),)


class Calendar(models.Model):
    classid = models.CharField(primary_key=True, max_length=70)
    day = models.DateField()
    end_time = models.CharField(max_length=8, blank=True, null=True)
    start_time = models.CharField(max_length=8)
    event = models.ForeignKey('Event', models.DO_NOTHING, db_column='event')

    class Meta:
        managed = False
        db_table = 'calendar'
        unique_together = (('day', 'event'),)


class DArtEStato(models.Model):
    code = models.CharField(primary_key=True, max_length=80)
    name = models.CharField(max_length=160, blank=True, null=True)
    definition = models.CharField(max_length=1200, blank=True, null=True)
    alphacode = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_art_e_stato'


class DELang(models.Model):
    code = models.CharField(primary_key=True, max_length=80)
    name = models.CharField(max_length=160, blank=True, null=True)
    definition = models.CharField(max_length=1200, blank=True, null=True)
    alphacode = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_e_lang'


class DEVc(models.Model):
    code = models.CharField(primary_key=True, max_length=80)
    name = models.CharField(max_length=160, blank=True, null=True)
    definition = models.CharField(max_length=1200, blank=True, null=True)
    alphacode = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_e_vc'


class DMediaETipomm(models.Model):
    code = models.CharField(primary_key=True, max_length=80)
    name = models.CharField(max_length=160, blank=True, null=True)
    definition = models.CharField(max_length=1200, blank=True, null=True)
    alphacode = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_media_e_tipomm'


class DRssEState(models.Model):
    code = models.CharField(primary_key=True, max_length=80)
    name = models.CharField(max_length=160, blank=True, null=True)
    definition = models.CharField(max_length=1200, blank=True, null=True)
    alphacode = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_rss_e_state'


class DTourETipoit(models.Model):
    code = models.CharField(primary_key=True, max_length=80)
    name = models.CharField(max_length=160, blank=True, null=True)
    definition = models.CharField(max_length=1200, blank=True, null=True)
    alphacode = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_tour_e_tipoit'


class Event(models.Model):
    classid = models.CharField(primary_key=True, max_length=70)
    descr_it = models.TextField(blank=True, null=True)
    image_url = models.CharField(max_length=200, blank=True, null=True)
    name_it = models.CharField(max_length=512)
    state = models.ForeignKey(DArtEStato, models.DO_NOTHING, db_column='state')
    source_rss = models.ForeignKey('Rss', models.DO_NOTHING, db_column='source_rss')
    notes = models.CharField(max_length=1024, blank=True, null=True)
    open_time = models.CharField(max_length=1024, blank=True, null=True)
    tickets = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'


class EventCategory(models.Model):
    classid = models.CharField(primary_key=True, max_length=70)
    name_it = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'event_category'


class EventCategoryNameTradT(models.Model):
    id_Classref_Name_trad_lang_Name_trad_value = models.AutoField(primary_key=True)
    classref = models.ForeignKey(EventCategory, models.DO_NOTHING, db_column='classref')
    name_trad_lang = models.ForeignKey(DELang, models.DO_NOTHING, db_column='name_trad_lang')
    name_trad_value = models.CharField(max_length=16384)

    class Meta:
        managed = False
        db_table = 'event_category_name_trad_t'
        unique_together = (('classref', 'name_trad_lang', 'name_trad_value'),)


class EventDescrTradT(models.Model):
    id_Classref_Descr_trad_lang_Descr_trad_value = models.AutoField(primary_key=True)
    classref = models.ForeignKey(Event, models.DO_NOTHING, db_column='classref')
    descr_trad_lang = models.ForeignKey(DELang, models.DO_NOTHING, db_column='descr_trad_lang')
    descr_trad_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'event_descr_trad_t'
        unique_together = (('classref', 'descr_trad_lang', 'descr_trad_value'),)


class EventNameTradT(models.Model):
    id_Classref_Name_trad_lang_Name_trad_value = models.AutoField(primary_key=True)
    classref = models.ForeignKey(Event, models.DO_NOTHING, db_column='classref')
    name_trad_lang = models.ForeignKey(DELang, models.DO_NOTHING, db_column='name_trad_lang')
    name_trad_value = models.CharField(max_length=16384)

    class Meta:
        managed = False
        db_table = 'event_name_trad_t'
        unique_together = (('classref', 'name_trad_lang', 'name_trad_value'),)


class Gallery(models.Model):
    classid = models.CharField(primary_key=True, max_length=70)
    image_url = models.CharField(max_length=1024)
    linked_event = models.ForeignKey(Event, models.DO_NOTHING, db_column='linked_event', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gallery'


class Location(models.Model):
    classid = models.CharField(primary_key=True, max_length=70)
    address = models.TextField(blank=True, null=True)
    num = models.DecimalField(max_digits=15, decimal_places=0)
    event = models.CharField(max_length=70)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'
        unique_together = (('num', 'event'),)


class Media(models.Model):
    classid = models.CharField(primary_key=True, max_length=70)
    name_it = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    type = models.ForeignKey(DMediaETipomm, models.DO_NOTHING, db_column='type')
    art = models.ForeignKey(Art, models.DO_NOTHING, db_column='art')

    class Meta:
        managed = False
        db_table = 'media'
        unique_together = (('name_it', 'art'),)


class MediaNameTradT(models.Model):
    id_Classref_Name_trad_lang = models.AutoField(primary_key=True)
    classref = models.ForeignKey(Media, models.DO_NOTHING, db_column='classref')
    name_trad_lang = models.ForeignKey(DELang, models.DO_NOTHING, db_column='name_trad_lang')
    name_trad_value = models.CharField(max_length=16384, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'media_name_trad_t'
        unique_together = (('classref', 'name_trad_lang'),)


class News(models.Model):
    classid = models.CharField(primary_key=True, max_length=70)
    descr = models.TextField()
    image_url = models.CharField(max_length=1024, blank=True, null=True)
    pubb_date = models.DateField()
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'


class NewsDescrTradT(models.Model):
    id_Classref_Descr_trad_lang_Descr_trad_value = models.AutoField(primary_key=True)
    classref = models.ForeignKey(News, models.DO_NOTHING, db_column='classref')
    descr_trad_lang = models.ForeignKey(DELang, models.DO_NOTHING, db_column='descr_trad_lang')
    descr_trad_value = models.CharField(max_length=16384)

    class Meta:
        managed = False
        db_table = 'news_descr_trad_t'
        unique_together = (('classref', 'descr_trad_lang', 'descr_trad_value'),)


class NewsTitleTradT(models.Model):
    id_Classref_Title_trad_lang_Title_trad_value = models.AutoField(primary_key=True)
    classref = models.ForeignKey(News, models.DO_NOTHING, db_column='classref')
    title_trad_lang = models.ForeignKey(DELang, models.DO_NOTHING, db_column='title_trad_lang')
    title_trad_value = models.CharField(max_length=16384)

    class Meta:
        managed = False
        db_table = 'news_title_trad_t'
        unique_together = (('classref', 'title_trad_lang', 'title_trad_value'),)


class RetailerCategory(models.Model):
    classid = models.CharField(primary_key=True, max_length=70)
    name_it = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'retailer_category'


class RetailerCategoryNameTradT(models.Model):
    id_Classref_Name_trad_lang_Name_trad_value = models.AutoField(primary_key=True)
    classref = models.ForeignKey(RetailerCategory, models.DO_NOTHING, db_column='classref')
    name_trad_lang = models.ForeignKey(DELang, models.DO_NOTHING, db_column='name_trad_lang')
    name_trad_value = models.CharField(max_length=16384)

    class Meta:
        managed = False
        db_table = 'retailer_category_name_trad_t'
        unique_together = (('classref', 'name_trad_lang', 'name_trad_value'),)


class RetailerVc(models.Model):
    classid = models.CharField(primary_key=True, max_length=70)
    address = models.CharField(max_length=2048)
    name = models.CharField(max_length=1024)
    retailer_category = models.ForeignKey(RetailerCategory, models.DO_NOTHING, db_column='retailer_category')
    geo = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'retailer_vc'


class Rss(models.Model):
    classid = models.CharField(primary_key=True, max_length=70)
    pub_date = models.CharField(max_length=19)
    state = models.ForeignKey(DRssEState, models.DO_NOTHING, db_column='state')
    text_it = models.TextField()
    title_it = models.CharField(max_length=500)
    url = models.CharField(max_length=500, blank=True, null=True)
    when_descr_it = models.TextField(blank=True, null=True)
    when_is = models.TextField(blank=True, null=True)
    where_is = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rss'


class RssCategory(models.Model):
    classid = models.CharField(primary_key=True, max_length=70)
    rss = models.ForeignKey(Rss, models.DO_NOTHING, db_column='rss')
    category = models.TextField()
    state = models.ForeignKey(DRssEState, models.DO_NOTHING, db_column='state', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rss_category'


class RssTextTradT(models.Model):
    id_Classref_Text_trad_lang_Text_trad_value = models.AutoField(primary_key=True)
    classref = models.ForeignKey(Rss, models.DO_NOTHING, db_column='classref')
    text_trad_lang = models.ForeignKey(DELang, models.DO_NOTHING, db_column='text_trad_lang')
    text_trad_value = models.CharField(max_length=16384)
    state = models.ForeignKey(DRssEState, models.DO_NOTHING, db_column='state', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rss_text_trad_t'
        unique_together = (('classref', 'text_trad_lang', 'text_trad_value'),)


class RssTitleTradT(models.Model):
    id_Classref_Title_trad_lang_Title_trad_value = models.AutoField(primary_key=True)
    classref = models.ForeignKey(Rss, models.DO_NOTHING, db_column='classref')
    title_trad_lang = models.ForeignKey(DELang, models.DO_NOTHING, db_column='title_trad_lang')
    title_trad_value = models.TextField()
    state = models.ForeignKey(DRssEState, models.DO_NOTHING, db_column='state', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rss_title_trad_t'
        unique_together = (('classref', 'title_trad_lang', 'title_trad_value'),)


class RssWhenDescrTradT(models.Model):
    id_Classref_When_descr_trad_lang_When_descr_trad_value = models.AutoField(primary_key=True)
    classref = models.ForeignKey(Rss, models.DO_NOTHING, db_column='classref')
    when_descr_trad_lang = models.ForeignKey(DELang, models.DO_NOTHING, db_column='when_descr_trad_lang')
    when_descr_trad_value = models.CharField(max_length=16384)
    state = models.ForeignKey(DRssEState, models.DO_NOTHING, db_column='state', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rss_when_descr_trad_t'
        unique_together = (('classref', 'when_descr_trad_lang', 'when_descr_trad_value'),)


class RssWhenIs(models.Model):
    classid = models.CharField(primary_key=True, max_length=70)
    rss = models.ForeignKey(Rss, models.DO_NOTHING, db_column='rss')
    day = models.DateField()
    state = models.ForeignKey(DRssEState, models.DO_NOTHING, db_column='state', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rss_when_is'


class RssWhereIs(models.Model):
    classid = models.CharField(primary_key=True, max_length=70)
    rss = models.ForeignKey(Rss, models.DO_NOTHING, db_column='rss')
    location = models.TextField()
    state = models.ForeignKey(DRssEState, models.DO_NOTHING, db_column='state', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rss_where_is'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'
 #       constraints = [CheckConstraint(
 #                       check=Q('srid' > 0 & 'srid' <= 998999),
  #                      name='srid_interval')]


class Tour(models.Model):
    classid = models.CharField(primary_key=True, max_length=70)
    descr_it = models.CharField(max_length=8192)
    image_url = models.CharField(max_length=100, blank=True, null=True)
    kml_path = models.CharField(max_length=8192, blank=True, null=True)
    name_it = models.CharField(max_length=200)
    geom_path = models.GeometryField(blank=True, null=True)
    proximity_area = models.GeometryField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    type = models.ForeignKey(DTourETipoit, models.DO_NOTHING, db_column='type', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tour'


class TourDescrTradT(models.Model):
    classref = models.ForeignKey(Tour, models.DO_NOTHING, db_column='classref')
    descr_trad_lang = models.ForeignKey(DELang, models.DO_NOTHING, db_column='descr_trad_lang')
    descr_trad_value = models.CharField(max_length=16384)

    class Meta:
        managed = False
        db_table = 'tour_descr_trad_t'


class TourNameTradT(models.Model):
    id_Classref_Name_trad_lang_Name_trad_value = models.AutoField(primary_key=True)
    classref = models.ForeignKey(Tour, models.DO_NOTHING, db_column='classref')
    name_trad_lang = models.ForeignKey(DELang, models.DO_NOTHING, db_column='name_trad_lang')
    name_trad_value = models.CharField(max_length=16384)

    class Meta:
        managed = False
        db_table = 'tour_name_trad_t'
        unique_together = (('classref', 'name_trad_lang', 'name_trad_value'),)