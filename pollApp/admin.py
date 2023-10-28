from django.contrib import admin
from .models import *

admin.site.site_header = "O centro de pesquisas"
admin.site.site_title = "Área administrativa de votação"
admin.site.index_title = "Bem-vindo à nossa área administrativa de votação"

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)