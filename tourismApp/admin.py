from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Art)
admin.site.register(Calendar)
admin.site.register(Crowding)
admin.site.register(Event)
admin.site.register(Gallery)
admin.site.register(Location)
admin.site.register(Media)
admin.site.register(News)
admin.site.register(Rss)
admin.site.register(Tour)

admin.site.register(AArtCategoryArtCategory)
admin.site.register(AArtTourTour)
admin.site.register(AEventCategoryEventCategory)
admin.site.register(ArtCategory)
admin.site.register(ArtCategoryNameTradT)
admin.site.register(ArtDescrTradT)
admin.site.register(ArtNameTradT)
admin.site.register(ArtTradT)

admin.site.register(BenefitVc)
admin.site.register(BenefitVcDescrTradT)
admin.site.register(BenefitVcBenefitTradT)
admin.site.register(BenefitVcTitleTradT)

admin.site.register(DArtEStato)
admin.site.register(DELang)
admin.site.register(DEVc)
admin.site.register(DMediaETipomm)
admin.site.register(DRssEState)
admin.site.register(DTourETipoit)

admin.site.register(EventCategory)
admin.site.register(EventCategoryNameTradT)
admin.site.register(EventDescrTradT)
admin.site.register(EventNameTradT)

admin.site.register(LogVc)
admin.site.register(LogCrowd)

admin.site.register(MediaNameTradT)

admin.site.register(NewsDescrTradT)
admin.site.register(NewsTitleTradT)

admin.site.register(RetailerCategory)
admin.site.register(RetailerCategoryNameTradT)
admin.site.register(RetailerVc)

admin.site.register(RssCategory)
admin.site.register(RssTextTradT)
admin.site.register(RssTitleTradT)
admin.site.register(RssWhenDescrTradT)
admin.site.register(RssWhenIs)
admin.site.register(RssWhereIs)

admin.site.register(SpatialRefSys)

admin.site.register(TourNameTradT)
admin.site.register(TourDescrTradT)

