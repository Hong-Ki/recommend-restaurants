from django.shortcuts import render
from rest_framework import viewsets, response, status
from .serializers import UserSerializer, FriendSerializer
from rest_framework.decorators import action
from .models import User, Friend


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        user_id = request.POST.get('user_id')
        name = request.POST.get('name')
        chatId = request.POST.get('chat_id')

        queryset = User.objects.all()
        if queryset.filter(user_id=user_id).count() > 0:
            return response.Response({'result': 'ERROR', 'message': 'ID_DUP'})

        newUser = User(user_id=user_id, name=name, chat_id=chatId)
        newUser.save()

        return response.Response({'result': 'OK'})

    @action(detail=True, methods=['GET'], name='Friends')
    def friends(self, request, pk=None):
        user = User.objects.get(pk=pk)
        friends = user.friends_user.all()

        list = []

        for friend in friends:
            list.append(friend.friend.name)

        return response.Response(list)

    @friends.mapping.post
    def delete_password(self, request, pk=None):
        friend_id = request.POST.get('user_id')
        try:
            friend = User.objects.get(pk=friend_id)
            user = User.objects.get(pk=pk)
            user.friends_user.create(user=user, friend=friend)
        except(NameError):
            return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response.Response({'result': 'OK'})

    @action(detail=True, methods=['GET'], name='Reviews')
    def reviews(self, request, pk=None):
        restaurant_id = request.query_params.get('restaurant_id')
        friend_name = request.query_params.get('friend_name')
        user = User.objects.get(pk=pk)
        friend = user.friends_user.get(friend__name=friend_name).friend
        review = friend.rating_set.get(restaurant_id=restaurant_id)
        return response.Response({'rate': review.rate, 'review': review.etc})
