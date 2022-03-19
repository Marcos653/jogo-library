from core.models import Jogo
from rest_framework.serializers import ModelSerializer

class JogoSerializer(ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__' 