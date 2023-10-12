from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        ''' Проверяет права на конкретный объект '''
        print(request)
        return request.user == obj.creator



class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        ''' Проверяет права на конкретный объект '''
        print(request)
        if request.method == 'GET':
            return True
        return request.user == obj.creator
