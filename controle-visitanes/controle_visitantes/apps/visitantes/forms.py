from django import forms
from visitantes.models import Visitante

class VisitanteForm(forms.ModelForm):
    
    class Meta:
        model=Visitante
        fields=["nome_completo","CPF","data_nascimento","numero_casa","placa_veiculo","registrado_por","morador_responsavel"]
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

class AutorizaVisitanteForm(forms.ModelForm):

    morador_responsavel = forms.CharField(required=True)

    class Meta:
        model=Visitante
        fields=["morador_responsavel"]
        error_messages={
            "morador_responsavel":{
                "required":"Por favor, informe o nome do morador por autorizar a entrada do visitante"
            }
        }