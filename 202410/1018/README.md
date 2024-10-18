# 01-pjt

### 오늘 pjt 를 통해 배운 내용

* 회원정보 관리와 관련된 추가 기능(회원 정보 수정, 비밀번호변경)을 제공한다

* 프로필 페이지의 다양한 기능을 제공한다.

-----
## C번 : 프로필 페이지 구현 / D번 : 팔로워 기능 구현
  
* 기억해볼 부분

  ```html
    {% extends "base.html" %}

    {% block content %}
      <div class="container-fluid mt-5"> <!-- container-fluid로 변경하여 전체 너비 사용 -->
        <div class="row">
          <div class="col-md-6"> <!-- offset 제거 -->
            <div class="card text-start">
              <div class="card-body">
                <h1 class="card-title">{{person.username}}님의 프로필 페이지</h1>
                <p class="card-text">
                  팔로잉 : <strong>{{ person.followings.all|length }}</strong> / 
                  팔로워 : <strong>{{ person.followers.all|length }}</strong>
                </p>
                <br>

                {% if request.user != person %}
                  <div class="mb-3">
                    <form action="{% url "accounts:follow" person.pk %}" method="POST">
                      {% csrf_token %}
                      {% if request.user in person.followers.all %}
                        <input type="submit" value="언팔로우" class="btn btn-danger">
                      {% else %}
                        <input type="submit" value="팔로우" class="btn btn-primary">
                      {% endif %}
                    </form>
                  </div>
                {% endif %}

                <p><strong>회원번호:</strong> {{person.pk}}</p>
                <p><strong>유저이름:</strong> {{person.username}}</p>
                <p><strong>가입날짜:</strong> {{person.date_joined}}</p>
              </div>
            </div>

            <div class="mt-5 text-start">
              <h2>유저가 작성한 게시글</h2>
              {% if person.board_set.all|length == 0 %}
                <p>작성한 게시글이 없습니다.</p>
              {% else %}
                <ul class="list-group">
                  {% for boards in person.board_set.all %}
                    <li class="list-group-item">
                      <strong>글번호:</strong> {{ boards.pk }} <br>
                      <strong>글제목:</strong> 
                      <a href="{% url "boards:detail" boards.pk %}">{{ boards.title }}</a>
                    </li>
                  {% endfor %}
                </ul>
              {% endif %}
            </div>

            <div class="mt-5 text-start">
              <h2>유저가 작성한 댓글</h2>
              {% if person.comment_set.all|length == 0 %}
                <p>아직 작성한 댓글이 없습니다.</p>
              {% else %}
                <ul class="list-group">
                  {% for comment in person.comment_set.all %}
                    <li class="list-group-item">
                      <strong>게시물 제목:</strong> 
                      <a href="{% url "boards:detail" comment.board.pk %}">{{ comment.board.title }}</a> <br>
                      <strong>댓글:</strong> {{ comment.content }}
                    </li>
                  {% endfor %}
                </ul>
              {% endif %}
            </div>

            <div class="mt-5 text-start">
              <h2>팔로워</h2>
              {% if person.followers.all|length == 0 %}
                <p>팔로워 한 사람이 없습니다.</p>
              {% else %}
                <ul class="list-group">
                  {% for follower in person.followers.all %}
                    <li class="list-group-item">
                      <a href="{% url "accounts:profile" follower %}">{{ follower }}</a>
                    </li>
                  {% endfor %}
                </ul>
              {% endif %}
            </div>
          </div>
        </div>
      </div>
    {% endblock content %}

  ```

  * 프로필 페이지를 구현한다.

  * 역참조를 이용해 팔로워를 찾을 수 있다.

  * 역참조를 이용해 댓글이 씌여진 게시글을 찾을 수 있다.

  <!-- * 트러블 슈팅한 부분
  
    ```
    트러블 코드 조각
    ```
  
    * 트러블 현상 및 에러 정보
    * 원인 및 해결 방법 -->


## E. 생성형 AI 활용하기

* 생성형 AI 를 활용하여 bootstrap 디자인을 추가한다.

* 결과 : chat-Gpt를 활용해 프로필 페이지에서 박스 디자인 구현


## 오늘 후기

* 상세 페이지를 직접 구현하는 경험이었다.

* Chat Gpt를 사용하면 bootstrap 디자인을 어느 정도 구현할 수 있다.



### 참고 사이트