from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 100, db_index=True)
    
    def __str__(self):
        return self.name