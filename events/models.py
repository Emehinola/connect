from django.db import models

# Create your models here.


class Event(models.Model):
    event_title = models.CharField(max_length=100)
    event_location = models.CharField(max_length=100, default="")
    event_description = models.TextField()
    event_date = models.DateField(auto_now=False)
    event_time = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.event_title}"  # string to display in dashboard
