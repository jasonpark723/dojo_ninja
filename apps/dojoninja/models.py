from django.db import models

# Create your models here.


class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField()
    # ninjas = a list of ninja associated with given dojo
    # use .all() or .all for html template

    def __repr__(self):
        return f"Dojo object: {self.name} {self.city} {self.state} {self.ninjas} ({self.id})"


class Ninja(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    dojo = models.ForeignKey(Dojo, related_name="ninjas")

    def __repr__(self):
        return f"Ninja object: {self.first_name} {self.last_name} {self.dojo} ({self.id})"
