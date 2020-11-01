from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('galeria/', views.galeria, name='galeria'),
    path('contacto/', views.contacto, name='contacto'),
    path('anime/<int:pk>', views.AnimeDetailView.as_view(), name='anime-detail'),
    path('galeria/<str:pk>', views.GaleriaDetailView.as_view(),
         name='galeria-detail'),
]
urlpatterns += [
    path('anime/create/', views.AnimeCreate.as_view(), name='anime_create'),
    path('anime/<int:pk>/update', views.AnimeUpdate.as_view(), name='anime_update'),
    path('anime/<int:pk>/delete', views.AnimeDelete.as_view(), name='anime_delete'),
    path('galeria/create/', views.GaleriaCreate.as_view(), name='galeria_create'),
    path('galeria/<str:pk>/update',
         views.GaleriaUpdate.as_view(), name='galeria_update'),
    path('galeria/<str:pk>/delete',
         views.GaleriaDelete.as_view(), name='galeria_delete')
]
