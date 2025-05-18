from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100,blank=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.name

    @classmethod
    def getall(cls):
        return cls.objects.filter(status=True)

    @classmethod
    def get_catagory_by_id(cls, id):
        return cls.objects.filter(pk=id).first()

    def softdelete(self):
        self.status = False
        self.save()
