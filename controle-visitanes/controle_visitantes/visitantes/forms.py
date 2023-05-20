from django.forms import ModelForm
from visitantes.models import Visitante

class VisitanteForm(ModelForm):
    
    class Meta:
        model=Visitante
        fields={"nome_completo","CPF","data_nascimento","numero_casa","placa_veiculo","registrado_por","morador_responsavel"}
        error_messages={
            "nome_completo":{
                "required":"O nome completo do visitante é obrigatório."
            },
            "CPF":{
                "required":"O CPF é obrigatório."
            },
            "data_nascimento":{
                "required":"A data de nascimento é obrigatória",
                "invalid":"Por favor, informe uma data válida"
            },
            "numero_casa":{
                "required":"O número da casa é obrigatório"            
            },

        }
