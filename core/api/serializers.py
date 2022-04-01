from core.models import Jogo
from rest_framework.serializers import ModelSerializer
# from drf_base64.fields import Base64ImageField, Base64FileField

class JogoSerializer(ModelSerializer):
    # image = Base64ImageField(required=False)
    class Meta:
        model = Jogo
        fields = '__all__' 