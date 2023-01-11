from django.contrib.auth import get_user_model
from rest_framework.serializers import (PrimaryKeyRelatedField,
                                        CurrentUserDefault,
                                        ValidationError,
                                        ModelSerializer)
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post, Group, Follow

User = get_user_model()


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = ('__all__')


class CommentSerializer(ModelSerializer):
    post = PrimaryKeyRelatedField(
        read_only=True,
        source='post.pk'
    )
    author = SlugRelatedField(
        required=False,
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=CurrentUserDefault()
    )
    following = SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Вы уже подписаны'
            )
        ]

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise ValidationError(
                'Подписка запрещена'
            )
        return data
