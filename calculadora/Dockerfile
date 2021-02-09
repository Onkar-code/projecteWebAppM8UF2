FROM ubuntu:20.04

ENV TZ=Europe/Madrid
RUN ln -snf /usr/share/zoneinfo$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get install -y tzdata

RUN apt-get update -y && apt-get install -y \
	apache2 --no-install-recommends\
	libapache2-mod-wsgi-py3 \
	python3 \
	python3-pip \
 && a2enmod wsgi

RUN mkdir /var/www/calculadora
COPY . /var/www/calculadora

RUN pip3 install -r /var/www/calculadora/requirements.txt

COPY calculadora.conf /etc/apache2/sites-available/calculadora.conf
RUN a2ensite calculadora

RUN rm -rf /etc/apache2/sites-available/000-default.conf
RUN rm -rf /etc/apache2/sites-enabled/000-default.conf

RUN rm -rf /var/www/calculadora/calculadora.conf
RUN rm -rf /var/www/calculadora/Dockerfile
RUN rm -rf /var/www/calculadora/requirements.txt

RUN chown -R $user:$user /var/www/calculadora

RUN service apache2 stop
RUN sleep 4

RUN service apache2 start
RUN sleep 4

EXPOSE 80

RUN apt-get clean

ENTRYPOINT ["/bin/bash", "/usr/sbin/apache2ctl", "-D", "FOREGROUND"]