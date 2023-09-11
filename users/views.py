from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework import generics, mixins

# Create your views here.


from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Speciality, Address, Language
from .serializers import SpecialitySerializer, AddressSerializer, LanguageSerializer


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_specialitys': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/speciality/pk/delete'
    }

    return Response(api_urls)


@api_view(['POST'])
def add_specialities(request):
    speciality = SpecialitySerializer(data=request.data)

    # validating for already existing data
    if Speciality.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if speciality.is_valid():
        speciality.save()
        return Response(speciality.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# = = = = = = = = = = =  A D D R E S S  = = = = = = = = = = = = = = = =#

class AddressCreate(generics.CreateAPIView):
    """
    This view should POST an Address in DATABASE
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressList(generics.ListAPIView):
    """
    This view should return a list of all the Addresses
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# = = = = = = = =  =  L A N G U A G E  = = = = = = = = = = = = = = = =#


class LanguageCreate(generics.CreateAPIView):
    """
    This view should POST a Language in DATABASE
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageList(generics.ListAPIView):
    """
    This view should return a list of all the LANGUAGES
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (AllowAny,)


class LanguageDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# = = = = = = = =  =  L A N G U A G E  = = = = = = = = = = = = = = = =#


class SpecialityCreate(generics.CreateAPIView):
    """
    This view should POST a Language in DATABASE
    """
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


class SpecialityList(generics.ListAPIView):
    """
    This view should return a list of all the LANGUAGES
    """
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    permission_classes = (AllowAny,)


class SpecialityDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)