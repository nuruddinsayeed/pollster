from django.contrib import admin
from .models import Question, Choice


admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to pollster Admin area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # TO add extra empty fields


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]  # classes collapse to hide dateTime

    inlines = [ChoiceInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
