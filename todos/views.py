# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Todo
# Create your views here.


@api_view(['GET'])
def view_todos(request):
    """
    Endpoint: /todos/view_todos/
    Method: GET
    Description: Returns a list of all todos
    """

    todos = Todo.objects.all()

    # convert queryset todo objects to a list of dicts
    response_data = [todo.as_dict() for todo in todos]
    return Response(response_data)


@api_view(['GET'])
def get_todo(request, todo_id):
    """
    Endpoint: /todos/get_todo/<todo_id>/
    Method: GET
    Description: Returns a specific todo
    """

    try:
        todo = Todo.objects.get(_id=todo_id)
    except ObjectDoesNotExist:
        return Response({"error", "todo not found"},
                        status=status.HTTP_404_NOT_FOUND)

    # convert todo object to dict
    response_data = todo.as_dict()

    return Response(response_data)
