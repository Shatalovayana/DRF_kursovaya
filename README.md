### DRF-project*
Это трекер полезных привычек, с помощью данного приложения вы можете получать напоминани о необходимости выполнения той или иной привычки


### _УСТАНОВКА_
Для работы с программой вам потребуется Python 3.7 и выше, а также установить пакеты и библиотеки, которые хранятся в файле requrements.txt


Вы можете установить эти библиотеки с помощью команды pip, например:

* pip install redis

Вы можете скачать или клонировать этот репозиторий на свой компьютер.

Вам необходимо внести свои настройки в config/settings.py, для удобства вы можете посмотреть файл .env.sample
### _ИСПОЛЬЗОВАНИЕ_

Вам необходимо зарегистрироваться на сайте, для этого нужно заполнить обязательные поля (password, email, tg_id(ваш id в telegram))

После этого вам будут доступны все возможности сервиса, а именно - вы сможете добавить свои привычки, вознаграждения и активировать рассылку-напоминание.

Для запуска сервиса вам необходимо выполнить в консоли команду:
* python manage.py runserver

Чтобы использовать периодические задачи, нужно запустить не только Celery worker, но и планировщик Celery beat. Выполните следующую команду в командной строке:

celery -A my_project worker —loglevel=info
celery -A my_project beat —loglevel=info

Это запустит Celery worker и планировщик Celery beat, которые будут совместно работать для выполнения периодических задач.


