from django.contrib import admin
from pages.models import Page,HomePage,SliderImage,Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('page','position','title')

admin.site.register(Page)
admin.site.register(HomePage)
admin.site.register(SliderImage)
admin.site.register(Article,ArticleAdmin)