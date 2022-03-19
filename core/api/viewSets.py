from rest_framework.viewsets import ModelViewSet
from core.models import Jogo
from .serializers import JogoSerializer

class JogoViewSet(ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer