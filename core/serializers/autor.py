from rest_framework.serializers import ModelSerializer

from core.models import Autor


class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"

    def __str__(self):
        return f'({self.id}) {self.nome}'

    class Meta:
        verbose_name = 'autor'
        verbose_name_plural = 'autores'