from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from core.models import Category, Jogo
from .serializers import CategorySerializer, JogoSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.order_by('category')
    serializer_class = CategorySerializer
    
class JogoViewSet(ModelViewSet):
    queryset = Jogo.objects.order_by('title')
    serializer_class = JogoSerializer

    @action(detail=False, methods=['get'], url_path='filter')
    def get_title(self, request):
        try:
            title = request.query_params.get('title', None)
            print(title)
            queryset = self.queryset.filter(title__icontains=title)
            page = self.paginate_queryset(queryset)
            serializer = JogoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data, )            
        
        except:
            return Response({'worked': False})

        
