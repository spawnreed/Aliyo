from django.contrib import admin
from .models import Board, Response, Phrase, Tag

admin.site.register(Board)
admin.site.register(Response)
admin.site.register(Phrase)
admin.site.register(Tag)

# Register your models here.
