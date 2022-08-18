from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    #ex: /polls/
    path("", views.index, name="index"), #<int:question_id/> es  la manera que da jango de poder pasar parametros variables metoante la url que nosotros estamos utilizado para una pagina
    #ex: /polls/5/
    path("<int:question_id>/detail/", views.detail, name="detail"),
    #ex: /polls/5/result
    path("<int:question_id>/results/", views.results, name="results"),
    #ex: /polls/5/vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
]