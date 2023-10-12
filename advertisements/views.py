from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly, IsOwner
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # источник данных
    queryset = Advertisement.objects.all()
    # сериализатор в JSON
    serializer_class = AdvertisementSerializer
    # класс разрешений по умолчанию
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]

    # разрешенные методы
    http_method_names = ['get', 'post', 'patch', 'delete', 'head']

    # используемые готовые фильтры
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # класс с параметрами фильтрации
    filterset_class = AdvertisementFilter
    # поле, по которому будет осуществляться контекстный поиск
    search_fields = ['title']

    # сортировка по умолчанию
    ordering = '-created_at'
    # размер страницы по умолчанию
    page_size = 20

    # проверка разрешений на выполнение методов
    # TRUE - для безопасных методов (которые не вносят изменения)
    #        [GET, PATCH, PUT]
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    # получение прав доступа при вызове того или иного метода
    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]  # любой
        if self.action in ["create"]:
            return [IsAuthenticated()]  # только аутентифицированный
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwner()]  # только владелец
        return []


