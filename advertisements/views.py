from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes

from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly, IsOwner
from advertisements.serializers import AdvertisementSerializer

@permission_classes([IsAuthenticated])
class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    # фильтрация
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['creator', 'created_at', 'status']
    search_fields = ['title',]
    ordering_fields=['created_at',]



    def get_permissions(self):
        """Получение прав для действий."""
        if self.request.method == 'GET':
            self.permission_classes = [IsOwnerOrReadOnly]
        elif self.request.method in ['DELETE', 'PATCH', 'PUT']:
            self.permission_classes = [IsOwner]
        else:
            self.permission_classes = [IsAuthenticated ]

        return super().get_permissions()    # super(ModelViewSet, self).get_permissions()


        # if self.action in ["create", "update", "partial_update"]:
        #     return [IsAuthenticated()]
        # return []

        # return super().get_permissions() #дополнил, но теперь при где запросе получить данные просит
        # # идентификацию не пойму
