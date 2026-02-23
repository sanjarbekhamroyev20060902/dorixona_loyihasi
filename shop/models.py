from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Kategoriyalar"

class Medicine(models.Model):
    # Bu kategoriya bilan bog'lanish (K harfi katta bo'lishi shart!)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='medicines', verbose_name="Kategoriya", null=True, blank=True)
    
    name = models.CharField(max_length=200, verbose_name="Dori nomi")
    
    # Narx IntegerField bo'lishi kerak
    price = models.IntegerField(verbose_name="Narxi (so'm)")
    
    image = models.ImageField(upload_to='medicines/', verbose_name="Rasmi")
    description = models.TextField(verbose_name="Tavsif")

    def __str__(self):
        return self.name