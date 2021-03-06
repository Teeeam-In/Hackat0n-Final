from django.db import models
        
class Events(models.Model):
    title = models.TextField(blank=True)
    time = models.TextField(blank=True)
    description = models.TextField(blank=True)
    cout_people = models.BigIntegerField()
    place = models.TextField(blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Івенти'
        verbose_name_plural = 'Івенти'
    