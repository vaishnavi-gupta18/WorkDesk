from rest_framework import serializers

from users.models import User
from .models import Project, List, Member, Card, Comment


class UserSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for User model
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'groups']


class MemberSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for Member model
    """
    class Meta:
        model = Member
        fields = ['id', 'users', 'fullname', 'position', 'year']


class CommentSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for Comment model
    """
    class Meta:
        model = Comment
        fields = ['id', 'member', 'card', 'date_created', 'body']


class CardSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for Card model
    """
    class Meta:
        model = Card
        fields = ['id', 'title', 'description', 'start_date', 'due_date', 'creator', 'assignees', 'list']


class ListSerializer(serializers.ModelSerializer):
    """
    Nested ModelSerializer for List model including cards
    """
    cards = CardSerializer(many=True)

    class Meta:
        model = List
        fields = ['id', 'title', 'start_date', 'project', 'cards']


class ProjectSerializer(serializers.ModelSerializer):
    """
    Nested ModelSerializer for Project model including lists,cards
    """
    lists = ListSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'start_date', 'creator', 'members', 'status', 'is_public', 'lists']
