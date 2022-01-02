import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from todos.models import Todo

# Create your views here.


def list_todo_items(request: HttpRequest):
    context = {
        'todo_list': Todo.objects.all()
    }

    # field = Todo.objects.first()._meta.get_field('is_completed')

    # value = field.value_from_object(Todo.objects.first())

    # print('Context', value)

    return render(request, 'todos/todo_list.html', context)


def insert_todo_item(request: HttpRequest):
    content = request.POST.get('content', '')
    is_completed = request.POST.get('is_completed', False)

    if is_completed == '':
        is_completed = True

    todo = Todo(content=content, is_completed=is_completed)
    todo.save()
    return redirect('/todos/list/')


def delete_todo_item(request, todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/list/')


def mark_as_completed_todo_item(request, todo_id):
    data = json.load(request)
    is_completed = data['is_completed']
    Todo.objects.filter(pk=todo_id).update(is_completed=is_completed)

    return HttpResponse({'is_completed': is_completed})
