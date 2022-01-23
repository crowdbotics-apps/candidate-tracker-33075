from django.conf import settings
from django.db import models


class Candidates(models.Model):
    "Generated Model"
    candidateID = models.BigIntegerField()
    rippleHireID = models.BigIntegerField()
    candidateName = models.TextField(
        null=True,
        blank=True,
    )
    status = models.TextField(
        null=True,
        blank=True,
    )
    competency = models.TextField(
        null=True,
        blank=True,
    )
    dateAdded = models.DateField(
        auto_now=True,
        null=True,
        blank=True,
    )
    dateUpdated = models.DateField(
        auto_now=True,
        null=True,
        blank=True,
    )


class CandidateHistory(models.Model):
    "Generated Model"
    candidateID = models.ForeignKey(
        "home.Candidates",
        on_delete=models.CASCADE,
        related_name="candidatehistory_candidateID",
    )
    eventDate = models.DateTimeField()
    eventNotes = models.TextField()
    status = models.TextField()
