from django.contrib import admin
from .models import Article, Comments, HashTag

# Register your models here.
@admin.register(Article, Comments, HashTag)
class FeedAdmin (admin.ModelAdmin):
    pass
