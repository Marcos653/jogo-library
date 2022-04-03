from core.models import Category, Jogo
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class CategorySerializer(ModelSerializer):
    jogos = serializers.SerializerMethodField()

    def get_jogos(self, obj):
        jogos = Jogo.objects.filter(categories=obj.id)
        return JogoSerializer(jogos, many=True).data
    class Meta:
        model = Category
        fields = '__all__' 

class JogoSerializer(ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__' 
        depth = 1

 
      