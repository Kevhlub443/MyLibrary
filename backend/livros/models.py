from django.db import models

class livros(models.Model):
    title = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    paginas = models.IntegerField
    
    status_dos_livros = [
        ('c', 'Em casa'),
        ('p', 'Perdido'),
        ('E', 'Emprestado')
    ]

    status = models.CharField(max_length=1, choices=status_dos_livros)

    def __str__(self):
        return self.titulo

