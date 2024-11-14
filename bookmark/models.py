from django.db import models
from django.urls import reverse

# 모델 : 데이터베이스를 SQL 없이 다루려고 모델을 사용
# 모델을 사용하는 것은 사용자가 데이터를 객체화해서 다루는 것을 의미 함.
# 모델 = 테이블
# 모델의 필드 = 테이블의 칼럼
# 인스턴스 = 테이블의 레코드
# 필드의 값(인스턴스의 필드값) = 레코드의 칼럼 데이터값


# Create your models here.
# 클래스명의 첫자는 대문자로 표기
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('site URL')

    def __str__(self):
        return "(이름) " + self.site_name + ", (주소) " + self.url
    
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    # 필드의 종류가 결정하는 것
    # 1. 데이터베이스의 컬럼 종류
    # 2. 제약 사항(몇글자까지 허용, ...)
    # 3. Form의 종류 결정
    # 4. Form에서의 제약 사항


# 모델을 만들었다는 것은 데이터베이스에 어떤 데이터들을 어떤 형태로 넣을지 결정
# 마이그레이션 하기 전에 makemigrations을 먼저 해야 됨.
#    -. makemigrations => 모델의 변경사항을 추적해서 기록
# 마이그레이션(migrate) => 데이터베이스에 모델의 내용을 반영(테이블 생성)

