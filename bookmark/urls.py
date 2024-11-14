from django.urls import path
from .views import *

urlpatterns = [
    # 호스트 주소(http://127.0.0.1/bookmark/) 접속 의미
    # 클래스뷰를 활용하여 접속... 클래스 뷰 사용시에는 반드시 클래스명.as_view()를 해야 됨.
    path("", BookmarkListView.as_view(), name = 'list'),
    path("add/", BookmarkCreateView.as_view(), name = 'add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name = 'detail'),
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name = 'update'),
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name = 'delete'),
]