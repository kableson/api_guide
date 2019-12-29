from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import (mixins,
                                     CreateAPIView,
                                     ListAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateAPIView,
                                     RetrieveDestroyAPIView,
                                     RetrieveUpdateDestroyAPIView)


class TestView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin):
    queryset = User.objects.all()


# class UserViewSet(viewsets.ViewSet):
#     """
#     Example empty viewset demonstrating the standard
#     actions that will be handled by a router class.
#
#     If you're using format suffixes, make sure to also include
#     the `format=None` keyword argument for each action.
#     """
#
#     def list(self, request):
#         pass
#
#     def create(self, request):
#         pass
#
#     def retrieve(self, request, pk=None):
#         pass
#
#     def update(self, request, pk=None):
#         pass
#
#     def partial_update(self, request, pk=None):
#         pass
#
#     def destroy(self, request, pk=None):
#         pass
