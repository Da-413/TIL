# PJT 0n

### 오늘 pjt 를 통해 배운 내용

* Django를 이용해 웹 페이지에서 이용자 관리를 할 수 있다.

* Django를 이용해 데이터베이스를 조작할 수 있다.


## A. Movie 앱의 View 함수 작성

* 주요 요구 사항 : index, create, detail, update, delete 함수 작성

* 결과
  
    ```python
    from django.shortcuts import render, redirect
    from .models import Movie
    from .forms import MovieForm

    def index(request):
        movies = Movie.objects.all()
        context = {
            'movies': movies,
        }
        return render(request, 'movies/index.html', context)


    def create(request):
        if request.method == 'POST':
            form = MovieForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('movies:index')
        else:
            form = MovieForm()
        context = {
            'form': form
        }
        return render(request, 'movies/create.html', context)


    def detail(request, pk):
        movie = Movie.objects.get(pk = pk)
        context = {
            'movie': movie
        }
        return render(request, 'movies/detail.html', context)


    def update(request, pk):
        if request.method == 'POST':
            movie = Movie.objects.get(pk=pk)
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = MovieForm(instance=movie)
        context = {
            'movie': movie,
            'form': form
        }
        return render(request, 'movies/update.html', context)


    def delete(request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return redirect('movies:index')
      ```

  
-----

## B. accounts 앱의 view 함수 작성

* 주요 요구 사항 : login, logout, signup, update, delete, change_password 함수 작성

* 결과
  
    ```python
    from django.shortcuts import render, redirect
    from django.contrib.auth import login as auth_login
    from django.contrib.auth import logout as auth_logout
    from django.contrib.auth import update_session_auth_hash
    from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
    from django.contrib.auth.decorators import login_required
    from .forms import CustomUserCreationForm, CustomUserChangeForm


    # Create your views here.
    def login(request):
        if request.user.is_authenticated:
            return redirect('movies:index')

        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('movies:index')
        else:
            form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/login.html', context)


    @login_required
    def logout(request):
        auth_logout(request)
        return redirect('movies:index')


    def signup(request):
        if request.user.is_authenticated:
            return redirect('movies:index')

        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('movies:index')
        else:
            form = CustomUserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)


    @login_required
    def delete(request):
        # 누가 요청한건지 User모델에서 검색할 필요가 없다.
        # request 객체에 요청을 보내는 user 정보가 함께 들어있기 때문.
        request.user.delete()
        return redirect('movies:index')


    @login_required
    def update(request):
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('movies:index')
        else:
            form = CustomUserChangeForm(instance=request.user)
        context = {
            'form': form,
        }
        return render(request, 'accounts/update.html', context)


    @login_required
    def change_password(request, user_pk):
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                return redirect('movies:index')
        else:
            form = PasswordChangeForm(request.user)
        context = {
            'form': form,
        }
        return render(request, 'accounts/update.html', context)

    ```
  
-----

## C. template 작성

* base template,
  movies 앱의 create, detail, index, update 템플릿
  accounts 앱의 login, signup 템플릿 작성
  
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
    </head>
    <body>
      <nav>
        <a href="{% url 'movies:index' %}">INDEX</a>
        {% if user.is_authenticated %}
          <a href="{% url 'movies:create' %}">CREATE</a>
          <a href="{% url 'accounts:update' %}">회원정보수정</a>
          <a href="{% url 'accounts:update' %}">비밀번호변경</a>
          <form action="{% url 'accounts:logout'%}" method="POST" value="로그아웃">
            {% csrf_token %}
          </form>
        {% else %}
          <a href="{% url 'accounts:signup' %}">회원가입</a>
          <a href="{% url 'accounts:login' %}">로그인</a>
        {% endif %}

      </nav>
      {% block content %}
      {% endblock content %}
    </body>
    </html>
    ```

  * base.html에서 nav bar를 이용한다.




# 오늘 후기

* 사용자 인증에 대해 새롭게 알게 된 사실을 적용해 프로젝트를 진행했다.

* 시간이 많으면 버전 1번 프로젝트도 진행해보고 싶었다.



### 참고 사이트

* [챗 지피티](https://chatgpt.com/)

