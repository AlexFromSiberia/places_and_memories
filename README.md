# Places and Memories

Проект доступен для теста по адресу : http://alexfromsiberia.site/
Посмотреть остальные проекты можно тут: http://alexfromsiberia.site:3009

## Для запуска локально:

- Убедитесь что Docker, Docker-compose установлены;
- Открыть терминал в папке проекта (там где лежит docker-compose.yml);
- Выполнить:
  - docker-compose build
  - docker-compose up
- Проект будет запущен на 3009 порту (lockalhost:3009)
Изменить порт на привычный Вам: файл docker-compose.yml, строка 13.


Для запуска локально в Docker используются: 
- guincorn.py в app/;
- папка docker;
- docker-compose.yml в корне;
- в requirements.txt: gevent, gunicorn.
----

## Extra information:

- Click event on maps with Folium and information retrieval: https://gis.stackexchange.com/questions/313382/click-event-on-maps-with-folium-and-information-retrieval/353035#353035
- Folium map module quick start: https://python-visualization.github.io/folium/quickstart.html

- Google and VK authentication: - https://dev.to/mdrhmn/django-google-authentication-using-django-allauth-18f8

----

## Цель
Создать веб-приложение, с помощью которого люди смогут хранить свои впечатления о посещаемых
местах.

## Описание проекта
Пользователь заходит на сайт и видит страницу с кратким описанием сервиса. Также, он замечает
кнопки “Войти с помощью Google/VK”, нажимая на которую Google/VK предлагает ему разрешить доступ
к его базовой информации.
Он разрешает доступ, после чего должна открыться страница. В ее шапке будет имя и фотография
(информация взята из профиля Google/VK), по центру страницы надпись “У вас нет ни одного
воспоминания”, кнопка “Добавить воспоминание” (ее расположение на ваше усмотрение), при нажатии
на которую должна открываться форма с возможностью указания места на карте, а также поле для
ввода названия и поле для ввода комментария об этом месте.
Далее пользователь может нажать на кнопку “Сохранить”, после чего он снова попадает на домашнюю
страницу со списком из этого элемента и возможностью добавлять новые места. Весь добавленный
список мест будет отображаться на домашней странице.
На домашней странице пользователя также есть кнопка, позволяющая ему выйти из своего аккаунта.
После выхода он должен попасть на приветственную страницу сервиса без возможности видеть список
посещаемых мест. При повторной авторизации через Google/VK пользователь снова видит все свои
добавленные места.

## Требования к реализации:
● Приложение должно быть реализовано на базе фреймворка Django.
● Оформление кода должно соответствовать стандартам (PEP8, Django coding style)
● Все используемые зависимости должны быть актуальными на момент создания проекта.
● С самого начала разработки необходимо использовать git, а также следовать стилю коммитов:
https://chris.beams.io/posts/git-commit/. Исходный код приложения должен быть размещён на
github.
● Основной функционал (создание впечатлений о посещаемых местах и получение их списка)
должен быть покрыт юнит-тестами.
● Возможно использование любых сторонних пакетов, для стилей рекомендуется использовать
bootstrap.
● Если что-то не удалось сделать, необходимо описать проблемы в файле README.md

## Будет плюсом:
● Запуск тестов при новых коммитах реализован с использованием github actions.
● Локальный запуск через docker/docker-compose
● В README проекта есть бейдж с текущим покрытием тестами (https://coveralls.io/).
● Сконфигурированные правила для линтеров, запуск линтеров при коммите/пуше/github actions
● Приложение запускается на одном из облачных сервисов, например, https://www.heroku.com/