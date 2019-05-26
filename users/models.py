from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=32, unique=True, primary_key=True)
    chat_id = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=10, default='')

    def __str__(self):
        return str({
            'user_id': self.user_id,
            'chat_id': self.chat_id,
            'name': self.name
        })


class Friend(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='friends_user', related_query_name='friend_users')
    friend = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='friends_friend', related_query_name='friend_friends')

    class Meta:
        unique_together = (("user", "friend"))

    def __str__(self):
        return str({
            'user': self.user.__str__(),
            'friend': self.friend.__str__()
        })
