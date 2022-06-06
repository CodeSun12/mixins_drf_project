from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework import status


# Create your views here.
#
# # TODO GENERIC_APIVIEW OF GETTING DATA FROM API
# class StudentList(GenericAPIView, ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#
# # TODO GENERIC_APIVIEW METHOD OF POSTING DATA ON API
# class StudentCreate(GenericAPIView, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# # TODO GENERIC_APIVIEW METHOD OF RETRIEVING DATA FROM API (SINGLE ID DATA LIKE WHEN WE FETCH FROM PK)
# class StudentRetrieve(GenericAPIView, RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#
# # TODO GENERIC_APIVIEW METHOD TO UPDATE DATA BOTH OF TYPE PARTIALLY OR FULL UPDATE DATA
# class StudentUpdate(GenericAPIView, UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#
# # TODO GENERIC_APIVIEW METHOD TO DESTROY DATA FROM API
# class StudentDestroy(GenericAPIView, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# TODO NOW WE ARE GOING TO GROUP THESE CLASSES BECAUSE WE DON'T NEED TO MAKE THESE FOUR CLASSES.
# TODO WE'LL GROUP LIST_MODEL_MIXIN CLASS AND CREATE_MODEL_MIXIN CLASS BECAUSE WE DONT NEED PK IN THESE CLASSES
class LCStudentApi(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# TODO WE'LL GROUP UPDATE_MODEL_MIXIN CLASS AND DESTROY_MODEL_MIXIN CLASS BECAUSE WE NEED PK IN THESE CLASSES
class UDStudentApi(GenericAPIView, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
