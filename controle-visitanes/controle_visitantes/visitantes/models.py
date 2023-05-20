from django.db import models

class Visitante(models.Model):

    nome_completo = models.CharField(
        verbose_name = "Nome completo",
        max_length=194
    )

    CPF = models.CharField(
        verbose_name="CPF",
        max_length=11
    )

    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False,
        auto_now_add=False
    )

    numero_casa = models.PositiveSmallIntegerField(
        verbose_name = "Numero da casa"
    )

    placa_veiculo = models.CharField(
        verbose_name = "Placa de veiculo",
        max_length=7,
        blank=True,
        null=True
    )

    horario_chegada = models.DateTimeField(
        verbose_name = "Horario de chegada na portaria",
        auto_now_add=True

    )

    horario_saida = models.DateTimeField(
        verbose_name = "Horario de daida na portaria",
        auto_now=False,
        blank=True,
        null=True
    )

    horario_autorizacao = models.DateTimeField(
        verbose_name = "Horario de autorização",
        auto_now=False,
        blank=True,
        null=True
    )

    morador_responsavel = models.CharField(
        verbose_name="Nome do morador que autorizou a entrada",
        max_length=194,
        blank=True
    )

    registrado_por = models.ForeignKey(

        "porteiros.Porteiro",
        verbose_name="Porteiro responsável pelo registro",
        on_delete=models.PROTECT
    )

    def get_horario_saida(self):
        if self.horario_saida:
            return self.horario_saida
        
        return "Horario de saída não registrado"
    
    def get_horario_autorizacao(self):
        if self.horario_autorizacao:
            return self.horario_autorizacao
        
        return "Horario de autorização não registrado"
    
    def get_morador_responsavel(self):
        if self.morador_responsavel:
            return self.morador_responsavel
        
        return "Morador responsável não registrado"
    
    def get_placa_veiculo(self):
        if self.placa_veiculo:
            return self.placa_veiculo
        
        return "Placa do veículo não registrado"
    
    
    
    class Meta:
        verbose_name="Visitante",
        verbose_name_plural="Visitantes",
        db_table="visitante"

    def __str__(self):
        return self.nome_completo
