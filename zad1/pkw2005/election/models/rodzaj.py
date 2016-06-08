from django.db import models

class RodzajGminy(models.Model):

    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length = 100)


