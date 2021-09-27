from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

categories = [
    ("education", "Education"),
    ("general", "General"),
    ("giveaway",  "Giveaway"),
    ("entertainment", "Entertainment"),
    ("telecommunication", "Telecommunication"),
    ("medical", "Medical"),
    ("religion", "Religion"),
    ("fitness", "Fitness"),
    ("gossip",  "Gossip"),
    ("computer science", "Computer Science"),
    ("business", "Business"),
    ("fitness",  "Fitness"),
    ("marriage", "Marriage"),
    ("movie", "Movie"),
    ("health", "Health"),
    ("books",  "Books and Novels"),
    ("fashion", " Fashion and Beauty"),
    ("skin-care", "Skin Care"),
    ("politics",  "Politics"),
    ("engineering", "Engineering"),
    ("food",  "Foods and Nutrition"),
    ("graphics", "Grpahics design"),
    ("fashion", "Fashion"),
    ("media", "Media"),
    ("tricks_and_hacks",  "Tricks and Hacks"),
    ("psychology", "Psychology"),
    ("sports", "Sports"),
    ("food", "Foods"),
    ("technology", "Technology"),
    ("religion", "Religion"),
    ("others", "Others")
]


# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    category = models.CharField(
        choices=categories, max_length=200, default="general")
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images')
    time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.title
