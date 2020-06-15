from django.urls import path

from . import views

#urlpatterns = [
    #path('', views.index, name='index'),
    #path('', views.home_page, name='home'),
#]

urlpatterns = [
    #TDD home page
    path('', views.home_page, name='home'),
    # ex: /lists/
    path('lists/', views.index, name='index'),
    # ex: /lists/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /lists/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /lists/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
