from django.contrib import admin
from .models import CandidateHistory, Candidates

admin.site.register(Candidates)
admin.site.register(CandidateHistory)

# Register your models here.
