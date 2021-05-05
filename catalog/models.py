from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    date_start = models.DateField()
    date_end = models.DateField()
    number_of_lectures = models.PositiveIntegerField()

    def __str__(self):
        return self.title
