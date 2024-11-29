from django.contrib import admin
from .models import File
# Register your models here.

# class ChoiceInLine(admin.TabularInline):
#     model = Choice
#     extra = 3

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ("Date information", {"fields": ["pub_date"]}),
#         (None, {"fields":["question_text"]})
#     ]
#     list_display = ["question_text", "pub_date", "was_published_recently"]
#     list_filter = ["pub_date"]
#     search_fields = ["question_text"]
#     inlines = [ChoiceInLine]
admin.site.register(File)