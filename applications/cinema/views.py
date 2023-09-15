from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Movie, Like, Rating
from .serializers import MovieSerializer, RatingSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class MovieApiView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['owner', 'title']
    search_fields = ['title']
    ordering_fields = ['id']

    @action(methods=['POST'], detail=True)
    def like(self, request, pk, *args, **kwargs):
        try:
            user = request.user
            movie_id = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'movie not found'},status=status.HTTP_404_NOT_FOUND)
        like_obj, _ = Like.objects.get_or_create(owner=user, movie_id=pk)
        like_obj.is_like = not like_obj.is_like
        like_obj.save()
        status_text = 'liked' if like_obj.is_like else 'unliked'
        return Response({'status': status_text})

    @action(methods=['POST'], detail=True)
    def rating(self, request, pk, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rat_obj, _ = Rating.objects.get_or_create(owner=request.user, movie_id=pk)
        rat_obj.rating = serializer.data['rating']
        rat_obj.save()
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)







