from django.urls import path

from . import views

app_name = 'polls'
# index.html 파일에 <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li> gownsmsrjek
# urlpatterns = [
#     path('', views.index, name='index'),
# #변수받을땐 <int: var>
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
#
# ]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
