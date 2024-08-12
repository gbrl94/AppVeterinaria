from django import forms
from .models import Expediente

class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ['archivo', 'nombre_archivo', 'tipo_archivo']
        # `fecha_subida` no se incluye ya que se asigna automáticamente y no necesita ser editable.
