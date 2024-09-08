from django import forms
from .models import Expediente,Consulta,Medicamento

class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ['archivo', 'nombre_archivo', 'tipo_archivo']
        # `fecha_subida` no se incluye ya que se asigna automáticamente y no necesita ser editable.


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['cliente', 'mascota', 'motivo']
        widgets = {
            'motivo': forms.Textarea(attrs={'rows': 4}),
        }

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nombre', 'dosis', 'frecuencia']