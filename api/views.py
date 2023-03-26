from rest_framework import generics, serializers, status
from rest_framework.response import Response
from .models import Music
from .serializers import MusicSerializer

# Create your views here.


class MusicListCreateView(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

    def like(self, request, pk=None):
        music = self.get_object()
        music.likes += 1
        music.save()
        return Response({'likes': music.likes})


class MusicLikeView(generics.GenericAPIView):
    queryset = Music.objects.all()

    def post(self, request, pk=None):
        music = self.get_object()
        music.likes += 1
        music.save()
        return Response({'likes': music.likes}, status=status.HTTP_200_OK)


class MusicRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
