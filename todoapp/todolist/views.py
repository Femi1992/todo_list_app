from django.shortcuts import render, redirect
from .models import TodoList, Category
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm
# Create your views here.

def index(request):
    todos = TodoList.objects.all()
    categories = Category.objects.all()
    if request.method == "POST":
        if "taskAdd" in request.POST: #checking if there is a request to add atodo
            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + date + " " + category #content
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save() #saving thetodo
            return redirect("/") #reloading the page
        if "taskDelete" in request.POST: #checking if there is a request to delete atodo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #gettingtodo id
                todo.delete() #deletingtodo
    return render(request, "index.html", {"todos": todos, "categories":categories})

class CreateCategoryView(CreateView):
    redirect_field_name = 'todolist/index.html'

    form_class = CategoryForm

    model = Category

