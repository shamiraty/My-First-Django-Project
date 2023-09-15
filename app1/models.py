from django.db import models
from django.utils.html import mark_safe

#like a table
class SlideShow(models.Model):
    Title=models.CharField(max_length=50)
    Heading=models.CharField(max_length=50)
    RegisteredDate=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='slideshow/')

    def __str__(self):
        return self.Title
    def image_tag(self):
        return mark_safe('<img src="%s"width="70"style="border-radius:4px">'% (self.image.url))


# Create your models here.
