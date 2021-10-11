from tempfile import NamedTemporaryFile
from urllib.request import urlopen

from django.core.files import File
from django.db import models

# Create your models here.
class ImageModel(models.Model):

    titulo = models.CharField(max_length=100,blank=False,null=False)
    foto = models.ImageField(upload_to="", blank=True)
    url_foto = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.url_foto and not self.foto:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(str(self.url_foto)).read())
            img_temp.flush()
            self.foto.save(f"{self.titulo}", File(img_temp))
        if not self.foto and not self.url_foto:
            raise
        super(ImageModel,self).save(*args, **kwargs)



    class Meta:
        abstract=True