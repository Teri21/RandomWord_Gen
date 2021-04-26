from django.urls import path
from .import views

# path to our views:

urlpatterns = [
    path('', views.Random_Word),  # This is the home views.
    # assign dir. asking for route to display random_word.
    path('Random_Word', views.Random_Word),
    path('Generate', views.Generate),
    path('reset', views.reset)

]
