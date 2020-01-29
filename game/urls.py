from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'game'

urlpatterns = [
    path('', views.home, name='home'),                              # 홈 화면 (공격하기, 대응하기)
    path('login/', views.login, name='login'),                      # 로그인 페이지
    path('record/', views.record_list, name='record_list'),         # 전적 보기 리스트
    path('record/info/<int:pk>/', views.record_info, name='record_info'),    # 전적 보기에서 게임 정보 페이지
    path('atk/', views.atk, name='atk'),                            # 공격 화면
    path('atk/fin/', views.atk_fin, name='atk_fin'),                # 공격 후 선택 화면(추가 공격 or 홈)
    path('dfs/', views.dfs_list, name='dfs_list'),                  # 대응 화면 리스트
    path('dfs/<int:pk>/', views.dfs, name='dfs'),                   # 대응 화면
    path('dfs/<int:pk>/fin/', views.dfs_fin, name='dfs_fin'),     # 대응 후 선택 화면(추가 대응 or 홈) + 게임 결과
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/#', views.sign),
    path('accounts/profile/', views.sign)

]