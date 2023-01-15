from django.urls import path

from . import views

app_name = "polis"

urlpatterns = [
    #ex: /polis/
    path("",views.IndexView.as_view(),name="index"),
    #ex: /polis/5
    path("<int:pk>/detail/",views.DetailView.as_view(),name="detail"),
    #ex: /polis/5/results
    path("<int:pk>/results/",views.ResultsView.as_view(),name="results"),
    #ex: /polis/vote
    path("<int:question_id>/vote/",views.vote,name="vote"),
]