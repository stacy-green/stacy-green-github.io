from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .forms import AuthForm, NewTodoForm
from .models import TodoItem, Priority

@login_required
def index(request):
    # if request.user.is_anonymous:
    #     return redirect('login')
    todos = TodoItem.objects.filter(user=request.user, completed_date__isnull=True)
    completed_todos = TodoItem.objects.filter(user=request.user, completed_date__isnull=False)
    context = {
        "todos": todos,
        "completed": completed_todos,
        "form": NewTodoForm()
    }

    return render(request, 'todos/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = NewTodoForm(request.POST)
        if form.is_valid():
            todo_item = TodoItem()
            todo_item.text = form.cleaned_data['text']
            # Wrap in try/except
            priority = Priority.objects.get(id=form.cleaned_data['priority'])
            todo_item.priority = priority
            todo_item.user = request.user
            todo_item.save()
    return redirect('index')

def delete(request, todo_id):
    try:
        todo = TodoItem.objects.get(id=todo_id)
        if request.user == todo.user:
            todo.delete()
    except TodoItem.DoesNotExist:
        pass

    return redirect('index')

def update(request, todo_id):
    if request.method == "GET":
        try:
            todo = TodoItem.objects.get(id=todo_id)
        except TodoItem.DoesNotExist:
            return redirect('index')
        context = {
            "todo": todo,
            "form": NewTodoForm({"text": todo.text, "priority": todo.priority.id})
        }
        return render(request, 'todos/update.html', context)
    elif request.method == "POST":
        try:
            todo = TodoItem.objects.get(id=todo_id)
        except TodoItem.DoesNotExist:
            return redirect('index')

        form = NewTodoForm(request.POST)
        if form.is_valid():
            todo.text = form.cleaned_data['text']
            priority = Priority.objects.get(id=form.cleaned_data['priority'])
            todo.priority = priority
            todo.save()

        return redirect('index')

def complete(request, todo_id):
    try:
        todo = TodoItem.objects.get(id=todo_id)
    except TodoItem.DoesNotExist:
        pass
    todo.completed_date = timezone.now()
    todo.save()

    return redirect('index')


def signup(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password']
            )
            auth.login(request, user)
            return render(request, 'todos/signup.html')
        else:
            context = {
                'form': form
            }
            return render(request, 'todos/signup.html', context)
    context = {
        'form': AuthForm()
    }
    return render(request, 'todos/signup.html', context)

def login(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user != None:
                auth.login(request, user)
                next = request.GET.get('next')
                if next:
                    redirect('next')
                return redirect('index')
        form.add_error(error="Invalid username and/or password", field="username")
        context = {
            "form": form
        }
        return render(request, 'todos/login.html', context)
    context = {
        'form': AuthForm()
    }
    return render(request, 'todos/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('index')


