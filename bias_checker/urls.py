from django.urls import path

from . import views

app_name = 'bias_checker'

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

urlpatterns = [
    path('', views.index, name="index"),
    path('output/', views.output, name="output"),
    path('convert/',views.convert, name="convert"),
    path('privacy-policy/', views.privacy_policy, name="privacy_policy"),
    path('web-ext-policy/', views.web_ext_policy, name="web_ext_policy"),
    #path('error/', views.error, name="error"),
]