from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("login/",views.login_view,name='login'),
    path("register/",views.register,name='register'),
    path("dashboard/",views.dashboard,name='dashboard'),
    path("create-task/",views.createTask,name='createtask'),
    path("display/",views.displayAllTasks,name="display"),
    path("view-task/",views.viewTask,name="viewtask"),
    path("edit-task/",views.editTask,name='edittask'),
    path("delete-task/",views.deleteTask,name='deletetask'),
]
