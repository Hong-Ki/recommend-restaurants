from restaurants.models import Rating
from users.models import User, Friend
from rest_framework import viewsets, generics, mixins, response, status
from .crawler.cralwer import parsingRestaurnts
from .serializers import RatingSerializer


class RestaurantView(viewsets.ViewSet):
    def list(self, request):
        query = request.query_params.get('query')

        if query == '' or query == None:
            return response.Response(['Please enter keyword...'])
        queryset = parsingRestaurnts(query)
        return response.Response(queryset)


class ReviewView(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def list(self, request):
        friend_name = request.query_params.get('friend_name')

        friends = User.object.all()
        # print(friends)

        return response.Response({''})
