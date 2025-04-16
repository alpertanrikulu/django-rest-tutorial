from django.urls import path, include
from profiller.api.views import ProfilViewSet, ProfilDurumViewSet, ProfilFotoUpdateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiller', ProfilViewSet)
router.register(r'durum', ProfilDurumViewSet, basename='durum')

# proifl_list = ProfilViewSet.as_view({'get': 'list'})
# proifl_detay = ProfilViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    # path('kullanici-profilleri/', views.ProfilList.as_view(), name='profiller')
    # path('kullanici-profilleri/',proifl_list, name='profiller' ),
    # path('kullanici-profilleri/<int:pk>',proifl_detay, name='profil-detay' ),
    path('', include(router.urls)),
    path('profil-foto/', ProfilFotoUpdateView.as_view(), name="profil-foto"),

]