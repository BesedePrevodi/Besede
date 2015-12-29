from django.db import models

# Create your models here.

class Nivo(models.Model):  
  ime_nivoja = models.CharField(max_length=100, default='Nivo')

  def __str__(self):
    return self.ime_nivoja.encode('utf8')



class Sklop(models.Model):
  nivo       = models.ForeignKey(Nivo)
  ime_sklopa = models.CharField(max_length=50)

  def __str__(self):
    return self.ime_sklopa.encode('utf8') 
  
  

class Beseda(models.Model):
  sklop     = models.ForeignKey(Sklop)
  beseda    = models.CharField(max_length=100)
  prevod    = models.CharField(max_length=100)
  opis      = models.CharField(max_length=100, default="")

  def __str__(self):
    return self.beseda.encode('utf8') + " = " + \
           self.prevod.encode('utf8') + " (" + \
           self.opis  .encode('utf8') + ")"
  
