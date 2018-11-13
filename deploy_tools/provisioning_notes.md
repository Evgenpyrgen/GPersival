Обеспечение работы нового сайта
===============================

##Необходимые пакеты:
*nginx
*Python3.7
*virtualenv + pip
*Git

например в Ubuntu:

sudo add-apt-repository ppa:fkrull/deadsnakes

sudo apt-get install nginx git python3.7 python3.7-venv

##Конфигурация виртуального узла Nginx

*см. nginx.template.conf
*заменить SITENAME, например, на pers.icu

##Служба Systemd
*см. gunicorn-systemd.template.service
* заменить SITENAME, например, на pers.icu

##Структура папок
Если допустить что есть учетная запись пользователяв /root/

/root/
    |__sites
       |__SITENAME
          |__database
          |__source
          |__static
          |__virtualenv
