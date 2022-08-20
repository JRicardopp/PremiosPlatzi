from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    #ex: /polls/
    path("", views.indexView.as_view(), name="index"), #<int:question_id/> es  la manera que da jango de poder pasar parametros variables metoante la url que nosotros estamos utilizado para una pagina
    #ex: /polls/5/
    path("<int:pk>/detail/", views.DetailView.as_view(), name="detail"),
    #ex: /polls/5/result
    path("<int:pk>/results/", views.ResultlView.as_view(), name="results"),
    #ex: /polls/5/vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
]