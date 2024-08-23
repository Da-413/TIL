# 03-pjt

### 오늘 pjt 를 통해 배운 내용

* 개발자 포트폴리오를 html과 css를 이용해 만들 수 있다.

* 생성형 AI를 활용한다.

-----
## 생성형 AI를 이용해 작성한 코드

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>개발자 포트폴리오</title>
    <!-- Bootstrap CSS -->
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/5.3.0/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .hero {
            background: #333;
            color: #fff;
            padding: 4rem 0;
        }
        .hero h1 {
            font-size: 3rem;
        }
        .project-card {
            margin-bottom: 2rem;
        }
        .footer {
            background-color: #333;
            color: #fff;
            padding: 1rem 0;
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header class="hero text-center">
        <div class="container">
            <h1>홍길동</h1>
            <nav class="navbar navbar-expand-lg navbar-dark">
                <div class="container">
                    <a class="navbar-brand" href="#">포트폴리오</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav ms-auto">
                            <li class="nav-item">
                                <a class="nav-link" href="#about">소개</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#projects">프로젝트</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#contact">연락처</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
    </header>

    <!-- About Section -->
    <section id="about" class="py-5">
        <div class="container">
            <h2 class="text-center mb-4">소개</h2>
            <p class="text-center">안녕하세요! 저는 웹 개발자 홍길동입니다. 다양한 웹 기술을 활용하여 사용자 친화적인 웹 애플리케이션을 개발하고 있습니다.</p>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="py-5 bg-light">
        <div class="container">
            <h2 class="text-center mb-4">프로젝트</h2>
            <div class="row">
                <div class="col-md-4">
                    <div class="card project-card">
                        <div class="card-body">
                            <h5 class="card-title">프로젝트 1</h5>
                            <p class="card-text">프로젝트 1에 대한 간단한 설명을 여기에 작성합니다.</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card project-card">
                        <div class="card-body">
                            <h5 class="card-title">프로젝트 2</h5>
                            <p class="card-text">프로젝트 2에 대한 간단한 설명을 여기에 작성합니다.</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card project-card">
                        <div class="card-body">
                            <h5 class="card-title">프로젝트 3</h5>
                            <p class="card-text">프로젝트 3에 대한 간단한 설명을 여기에 작성합니다.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="py-5">
        <div class="container">
            <h2 class="text-center mb-4">연락처</h2>
            <p class="text-center">이메일: <a href="mailto:example@example.com">example@example.com</a></p>
            <p class="text-center">LinkedIn: <a href="https://www.linkedin.com/in/example" target="_blank">linkedin.com/in/example</a></p>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer text-center">
        <div class="container">
            <p>&copy; 2024 홍길동. All rights reserved.</p>
        </div>
    </footer>

    <!-- Bootstrap JS and dependencies -->
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.7/dist/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.min.js"></script>
</body>
</html>
```
  * bootstrap을 활용하여 반응형 포트폴리오 페이지를 구상했다.

## 생성형 AI 를 활용하여 주가 예측하기

* 내비게이터를 추가하고 기술 카드 영역을 추가했다.

* 여러가지 이미지를 추가하여 웹을 꾸며주었다.

## 오늘 후기

* bootstrap을 활용해 반응형 웹 페이지를 만들 수 있었다.

* 생성형 AI의 도움을 받아 기초 틀을 구상할 수 있었다.

* 강의 시간에 배운 내용을 활용하여 웹 페이지 내용을 추가하고 다양화할 수 있었다.