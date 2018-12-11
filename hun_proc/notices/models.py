from django.db import models
    
class Cpv(models.Model):
    """This is the CPV code of the notice"""
    text = models.CharField('CPV-kód',max_length=10, null= True)
        
    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Nuts(models.Model):
    """This is the NUTS code of the notice"""
    text = models.CharField('NUTS-kód',max_length=6, null= True)
    
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.text
    
class RegNumber(models.Model):
    """This is the registration number of the notice"""
    text = models.CharField('Iktatószám',max_length=10, primary_key=True)
    cpv = models.ForeignKey(Cpv, on_delete=models.PROTECT, verbose_name='CPV-kód')
    nuts = models.ForeignKey(Nuts, on_delete=models.PROTECT, verbose_name='NUTS-kód')
    def __str__(self):
        """Return a string representation of the model."""
        return self.text