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
    subject = models.CharField('Beszerzés Tárgya',max_length=50, null= True)
    proc_type = models.CharField('Eljárás fajtája',max_length=50, null= True)
    date = models.DateField('Közzététel dátuma', null= True)
    asker = models.CharField('Ajánlatkérő',max_length=50, null= True)
    asker_type = models.CharField('Ajánlatkérő típusa',max_length=50, null= True)
    asker_act = models.CharField('Tevékenységkör',max_length=50, null= True)
    name = models.CharField('Elnevezés',max_length=200, null= True)
    amount =models.FloatField('Beszerzés Összege',max_length=50, null= True)
    env = models.BooleanField('Körny.védelem?')
    def __str__(self):
        """Return a string representation of the model."""
        return self.text
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    