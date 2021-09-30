from django.db import models


class dependencia(models.Model):
    codDep = models.CharField(max_length=20, unique=True)
    descDep = models.CharField(max_length=50)

    def __str__(self):
        return self.descDep

# Create your models here.
class ambiente(models.Model):
    codAmb = models.CharField(max_length=11)
    descAmb = models.CharField(max_length=50)
    dependencia = models.ForeignKey(dependencia, on_delete=models.CASCADE)

    def __str__(self):
        return self.descAmb

class personal(models.Model):
    dniPer = models.CharField(max_length=8, unique=True)
    apePatPer = models.CharField(max_length=50)
    apeMatPer = models.CharField(max_length=50)
    nomPer = models.CharField(max_length=50)
    codPlaPer = models.CharField(max_length=50)
    fecNacPer = models.DateField(null=True)
    estPer = models.CharField(max_length=5, default=1)

    def __str__(self):
        return self.codPlaPer

class bienpat(models.Model):
    codEti = models.CharField(max_length=30, unique=True)
    desBien = models.CharField(max_length=100)    
    serBien = models.CharField(max_length=50)
    modBien = models.CharField(max_length=15)
    marBien = models.CharField(max_length=15)
    situBien = models.CharField(max_length=5, default='B')
    valBien = models.IntegerField()
    estBien = models.CharField(max_length=5, default=1)
    
    def __str__(self):
        return self.desBien

class certiDigital(models.Model):
    personal = models.ForeignKey(personal, on_delete=models.CASCADE)
    fecOtor = models.DateField()
    fecLimInsta = models.DateField()
    fecInsta = models.DateField()
    fecVenci = models.DateField()
    obsCerti = models.CharField(max_length=50)
    tipoCerti = models.CharField(max_length=30)

    def __str__(self):
        return self.obsCerti

class bienImag(models.Model):
    imagen = models.ImageField(upload_to='fotos/')
    bienpat = models.ForeignKey(bienpat, on_delete=models.CASCADE)

class bienPersonal(models.Model):
    personal = models.ForeignKey(personal, on_delete=models.CASCADE)
    bienpat = models.ForeignKey(bienpat, on_delete=models.CASCADE)

class bienAmbiente(models.Model):
    ambiente = models.ForeignKey(ambiente, on_delete=models.CASCADE)
    bienpat = models.ForeignKey(bienpat, on_delete=models.CASCADE)

class bienAmbiente(models.Model):
    ambiente = models.ForeignKey(ambiente, on_delete=models.CASCADE)
    bienpat = models.ForeignKey(bienpat, on_delete=models.CASCADE)

