from django.db import models

STATE_CHOICE = (
    ('Bihar', 'Bihar'),
    ('MP','MP')
)

class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    dob = models.DateTimeField(auto_now=False, auto_now_add=False)
    state = models.CharField(choices=STATE_CHOICE, max_length=50)
    location = models.CharField(max_length=50)
    pimage = models.ImageField(upload_to='pimage', blank=True)
    rdoc = models.FileField(upload_to='rdoc', blank=True)

    def __str__(self):
        return self.name
    