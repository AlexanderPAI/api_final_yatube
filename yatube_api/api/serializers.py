from rest_framework.serializers import (CurrentUserDefault, ModelSerializer,
                                        SlugRelatedField, ValidationError)
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('post',)
        model = Comment


class GroupSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=CurrentUserDefault()
    )
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Follow

        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
            )
        ]

    def validate_following(self, value):
        user = self.context.get('request').user
        if user == value:
            raise ValidationError('Нельзя подписаться на самого себя')
        return value


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post
