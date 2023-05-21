from django.db import models


# Create your models here.
class Usuario(models.Model):

    nome = models.CharField(max_length=20)

    is_active = models.BooleanField(
        verbose_name="Usuario esta ativo",
        default = True
    )

    is_staff = models.BooleanField(
        verbose_name="Usuario e da equipe de desenvolvimento",
        default=False
    )

    is_superuser = models.BooleanField(
        verbose_name="Usuario e superusuario",
        default=False
    )
    

    class Meta:
        verbose_name="Usuario",
        verbose_name_plural="Usuarios",
        db_table="usuario"

    def __str__(self):
        return self.nome