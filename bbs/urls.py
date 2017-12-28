from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from bbs import views

urlpatterns = [
    # Class 기반 View 처리
    path('', views.BbsList.as_view()),
    path('<int:pk>/bbs', views.BbsDetail.as_view()),

    # 함수 기반 View 처리
    # path('', views.bbs_list),
    # path('<int:pk>/bbs', views.bbs_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)