from django.db import models
from model_utils.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _


class Artist(TimeStampedModel):
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,)
    spotify_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,)

    def __str__(self):
            return self.name

    @property
    def get_song(self):
        return Song.objects.filter(artist_id=self.pk).first()

    class Meta:
        verbose_name = _('Artist')


class Venue(TimeStampedModel):
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,)
    location = models.CharField(
        max_length=255,
        null=True,
        blank=True,)


class Show(TimeStampedModel):
    title = models.TextField(
        null=True,
        blank=True,)
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,)
    date = models.DateTimeField(
        blank=True,
        null=True)
    venue = models.ForeignKey(
        Venue,
        on_delete=models.SET_NULL,
        blank=True,
        null=True)


class Song(TimeStampedModel):
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True,)
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,)
    album = models.CharField(
        max_length=255,
        null=True,
        blank=True,)
    spotify_track_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,)
    preview = models.CharField(
        max_length=255,
        null=True,
        blank=True,)
