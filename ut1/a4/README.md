# Sitio web 1

#### 1.1 - Descomprimir archivo

* Primero vamos a descargar el archivo **demo_php.zip** del enuciado del ejercicio. Para ello usamos el siguiente comando: wget https://github.com/sdelquin/claseando/raw/master/imw/UT1/assignments/assignment4/demo_php.zip

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

 * Además hay que expesificar al servidor web que debe utilizar el módulo php-fpm cuando vaya a manejar ficheros .php y así interpretarlos.

~~~console
---
location ~ \.php {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php7.2-fpm.sock;}
---
~~~
# Sitio web 2
