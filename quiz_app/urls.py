from django.urls import path

# from .views import quiz                           # relative import [importing only the specific view -> views]
# from quiz_app.views import quiz                   # absolute import [importing only the specific view -> views]

from . import views                                 # importing all the views [dynamic]          



urlpatterns = [

    path('', views.quiz, name='quiz'),


]