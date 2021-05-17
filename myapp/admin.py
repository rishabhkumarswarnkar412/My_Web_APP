from django.contrib import admin
from myapp.models import Get_quote
from myapp.models import Feedback
from myapp.models import Design

admin.site.register(Design)
admin.site.register(Get_quote)

admin.site.register(Feedback)


