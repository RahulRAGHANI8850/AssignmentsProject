from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexpage, name="indexpage"),
    path('indexpage', views.indexpage, name="indexpage"),
    path('submitted', views.submitted, name="submitted"),
    path('assignmentsubmit', views.assignmentsubmit, name="assignmentsubmit")
]
