from django.db import models

# Create your models here.


class Course(models.Model):
    course_title = models.CharField(max_length=100)
    # for o'level
    olevel_subjects = models.TextField()

    # for jamb
    jamb_subjects = models.TextField()
    description = models.TextField(default='')

    # number of views
    no_of_views = models.IntegerField(default="100")

    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'Courses'

    def __str__(self):
        return f'{self.course_title}'
