from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date','question_test']
    fieldsets = [
        (None,              {'fields':['question_test']}),
        ('Date information',{'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ['question_test','pub_date','was_published_recently']
    list_filter = ['pub_date']
    search_fields = ['question_test']

admin.site.register(Question, QuestionAdmin)
