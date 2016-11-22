from django.contrib import admin
from api.models import Issue, IssueState

# Register your models here.
admin.site.register(Issue)
admin.site.register(IssueState)