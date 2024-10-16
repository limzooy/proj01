from django.db import models

# Create your models here.
class Play(models.Model):
    #id = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    benefit_name = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    period = models.TextField(blank=True, null=True)
    age_rating = models.TextField(db_column='age rating', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ticket_price = models.TextField(db_column='Ticket Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'play'