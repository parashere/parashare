from django.urls import path
from . import views
from .nfc_reader import read_nfc_tag

urlpatterns = [
    path('', views.page0, name='home'),  # ルートURLでページ0を表示
    path('0/', views.page0, name='page0'),
    path('1/', views.page1, name='page1'),
    path('2/', views.page2, name='page2'),
    path('3/', views.page3, name='page3'),
    path('4/', views.page4, name='page4'),
    path('5/', views.page5, name='page5'),
    path('6/', views.page6, name='page6'),
    path('7/', views.page7, name='page7'),
    path('8/', views.page8, name='page8'),
    path('9/', views.page9, name='page9'),
    path('api/nfc-read/', read_nfc_tag, name='nfc_read'),  # NFC読み取りAPI
]
