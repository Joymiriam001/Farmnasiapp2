from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"



from django.db import models

class County(models.Model):
    name = models.CharField(max_length=100)
    county = models.CharField(max_length=100, choices=[
        ('Mombasa', 'Mombasa'),
            ('Kisumu', 'Kisumu'),
            ('Nakuru', 'Nakuru'),
            ('Eldoret', 'Eldoret'),
            ('Machakos', 'Machakos'),
            ('Meru', 'Meru'),
            ('Kiambu', 'Kiambu'),
            ('Nyeri', 'Nyeri'),
            ('Kajiado', 'Kajiado'),
            ('Narok', 'Narok'),
            ('Nyandarua', 'Nyandarua'),
            ('Laikipia', 'Laikipia'),
            ('Bomet', 'Bomet'),
            ('Kericho', 'Kericho'),
            ('Uasin Gishu', 'Uasin Gishu'),
            ('Bungoma', 'Bungoma'),
            ('Trans Nzoia', 'Trans Nzoia'),
            ('West Pokot', 'West Pokot'),
            ('Isiolo', 'Isiolo'),
            ('Samburu', 'Samburu'),
            ('Turkana', 'Turkana'),
            ('Wajir', 'Wajir'),
            ('Garissa', 'Garissa'),
            ('Mandera', 'Mandera'),
            ('Lamu', 'Lamu'),
            ('Kilifi', 'Kilifi'),
            ('Makueni', 'Makueni'),
            ('Embu', 'Embu'),
            ('Kitui', 'Kitui'),
        # Add more county options here
    ])

    def __str__(self):
        return self.name