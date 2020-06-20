from django.db import models

class Movies(models.Model):
    adult = models.TextField(blank=True, null=True)
    belongs_to_collection = models.TextField(blank=True, null=True)
    budget = models.TextField(blank=True, null=True)
    genres = models.TextField(blank=True, null=True)
    homepage = models.TextField(blank=True, null=True)
    id = models.TextField(primary_key=True, blank=True, null=False)
    imdb_id = models.TextField(blank=True, null=True)
    original_language = models.TextField(blank=True, null=True)
    original_title = models.TextField(blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    popularity = models.TextField(blank=True, null=True)
    poster_path = models.TextField(blank=True, null=True)
    production_companies = models.TextField(blank=True, null=True)
    production_countries = models.TextField(blank=True, null=True)
    release_date = models.TextField(blank=True, null=True)
    revenue = models.TextField(blank=True, null=True)
    runtime = models.TextField(blank=True, null=True)
    spoken_languages = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    tagline = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    video = models.TextField(blank=True, null=True)
    vote_average = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vote_count = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'

    def __str__(self):
        return self.title
