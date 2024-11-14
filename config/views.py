# 뷰 : 기능(페이지 단위)을 담당
# --> 화면이 나타나는 뷰가 있고 화면이 없는 뷰가 있음.
# 화면이 있건 없건 주소 URL은 있어야 함.
# 뷰 내용: 함수 또는 클래스, URL이 있으면 동작 함.
# 뷰의 코드 형식은 함수형과 클래스형 두가지 형태가 있음
#  - 함수형 : request 를 매개변수로 받고 (추가 매개변수 가능), 모양은 함수
#            내가 원하는대로 동작들을 설계하고 만들고 싶을 때
#  - 클래스형 : CRUD  기존에 많이 사용하는 기능을 미리 클래스로 만들어 두고 상속받아 사용
#              --> 장고의 제네릭 뷰를 많이 사용

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # 어떤 계산이나 데이터베이스 조회, 수정, 등록
    # 응답 메세지를 만들어서 반환
    # HTML 변수를 대신해서 템플릿 사용
    html = "<html><body>Hello</body></html>"
    return HttpResponse(html)

def welcome(request):
    html = "<html><body>Welcome to Django.</body></html>"
    return HttpResponse(html)

def template_test(request):
    # 기본 Template 폴더 
    # 1. admin 앱 
    # 2. 각 앱의 폴더에 있는 templates 폴더
    # 3. 사용자가 설정한 폴더
    return render(request, 'test.html')