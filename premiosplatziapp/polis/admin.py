from django.contrib import admin
from polis.models import Question, Choice

admin.site.register([Question,Choice])
