from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    #Will show the real string instead of object(number) 
    def __str__(self):
        return '{}'.format(self.search)

    class Meta:
        verbose_name_plural ='Searches'