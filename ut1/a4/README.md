# Sitio web 1

#### 1.1 - Descomprimir archivo

* Primero vamos a descargar el archivo **demo_php.zip** del enunciado del ejercicio. Para ello usamos el siguiente comando: wget https://github.com/sdelquin/claseando/raw/master/imw/UT1/assignments/assignment4/demo_php.zip

![wget](img/sitioweb1_1_1.png)

* Despues de ello usamos el comando **unzip demo_php.zip** para descomprimir el archivo.

![unzip](img/sitioweb1_2.png)

* Seguidamente cambiamos el archivo de lugar y lo movemos (Usando el comando mv) a webapps. Y para finalizar eliminaremos el archivo **demo_php.zip** (El cual esta ubicado en /home/alu6462) que nos descargamos anteriormente.

![mv](img/sitioweb1_3.png)

> El archivo **demo_php.zip** sigue ubicado en **/home/alu6462**, lo que movemos al directorio **/home/alu6462/webapps** es el directorio **demo_php**

#### 1.2 - Crear virtual host

* En primer lugar vamos a crear una virtual host llamda *php.alu6462.me*. Para ello creamos dentro del directorio **/etc/nginx/sites-available** el siguinte archivo:

![sites-available](img/sitioweb1_5.png)

* Le tenemos que expesificar que coja el **index.php** y obligarlo a que lo utilice:

~~~console
---
index index.php
---
~~~

* Además hay que expecificar al servidor web que debe utilizar el módulo php-fpm cuando vaya a manejar ficheros .php y así interpretarlos.

~~~console
---
location ~ \.php {    
  include snippets/fastcgi-php.conf;    
  fastcgi_pass unix:/run/php/php7.2-fpm.sock;}
---
~~~

* Luego enlazaremos dicho fichero a la ruta **/etc/nginx/sites-enabled** usando el comando ln -s. Y por ultimo recargamos ngingx usando el comando **systemctl reload nginx**

![reload](img/sitioweb1_6.png)

* Comprobamos el resultado final:

![web1](img/sitioweb1_7.png)

# Sitio web 2

#### 2.1 - Crear `main.py`

* Para empezar vamos a crear un archivo llamdo `main.py`, el cual es un codigo escrito en phyton. Para ello, y pensando en la creacion de la posterior virtual host, creamos tal archivo en **/home/alu6462/webapps/now**. El contenido del fichero será el siguiente:

![main.py](img/sitioweb2_1.png)

#### 2.2 - Instalar paquetes `flask` y `pytz`

* Instalamos los paquetes `flask` y `pytz` al entorno virtual. Para ello usamos el comando **pipenv install flask** y **pipenv install pytz**.

![flnpy](img/sitioweb2_2.png)

#### 2.3 - Crear Virtual host

* Para empezar vamos a crear un archivo en /etc/nginx/sites-available llamdo `now.alu6462.me`. Luego de ello enlazamos el fichero a la ruta **/etc/nginx/sites-enabled** usando el comando ln -s. Y por ultimo recargamos ngingx usando el comando **systemctl reload nginx**

![virtualhost](img/sitioweb2_3.png)

![reload](img/sitioweb2_8.png)

* Dentro del fichero hay una linea nueva que sirve para llamar a la funcion uwsgi y definir al puerto por el que seran escuchados (En nuestro caso 8081).

![uwsgi](img/sitioweb2_3_1.png)

#### 2.4 Crear script

* A continuacion creamos un script para llamar al comando uwsgi cada vez que lo necesitemos. Además le damos permisos.

![run.sd](img/sitioweb2_4.png)

![run.sd](img/sitioweb2_5.png)

#### 2.5 Activar supervisor

* Ahora añadimos una nueva configuracion para supervisor, el cual activara el script que hemos creado anteriormente. Para ello vamos a crear el archivo en **/etc/supervisor/conf.d**.

![supervisor](img/sitioweb2_6.png)

* Luego reiniciamos supervisor y miramos que el proseso esta corriendo.

![restart](img/sitioweb2_7.png)

#### 2.6 Salida de comandos

* Probamos los siguientes comandos:

~~~console
$ supervisorctl status
~~~

![status](img/sitioweb2_10.png)

~~~console
$ supervisorctl start now
~~~

![start](img/sitioweb2_11.png)

~~~console
$ supervisorctl stop now
~~~

![stop](img/sitioweb2_12.png)

~~~console
$ supervisorctl restart now
~~~

![restart](img/sitioweb2_13.png)
