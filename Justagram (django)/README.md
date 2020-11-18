# Just'agram

> 인스타그램 클론코딩 강의: 16강 ( 10, 8, 4, 7, 7, 7, 4, 11, 4, 7, 3, 6, 7, 10, 4, 8)

## 1. photo 앱 만들기:framed_picture:

```bash
$ touch .gitignore
$ python -m venv venv
$ source venv/Scripts/activate
$ pip install django==2.1.15 django_extensions django_bootstr
ap4
$ pip freeze > requirements.txt
$ django-admin startproject justagram .
$ python manage.py startapp photo
$ pip install Pillow
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver #확인
```



## 2. model 설계하기:zap:



## 3. views 설계하기:sunrise_over_mountains:



## 4. url 연결하기:eagle:

## 5. template 만들기

## 6. 사진 업로드 할 수 있도록 만들기

## 7. success url을 get_absolute_url로 연동하기

## 8. account 앱 만들기

## 9. 권한 문제 해결하기

## 10. 댓글 기능 구현하기

## 11. 좋아요 버튼 만들기

## 12. 좋아요한 게시글만 보기 기능 구현하기

## 13. 게시글 저장하기 기능 구현하기

## 14. 저장한 게시글 리스트 페이지 구현하기

## 15. 좋아요한 게시글 및 저장한 게시글 리스트는 로그인한 사람만 보여주기

## 16. my page 구현하기