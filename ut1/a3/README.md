# UT1-A3: Trabajo con virtual hosts

### Sitio web 1

* En primer lugar vamos a crear el virtual host: http://imw.alu6462.me. Para ello creamos un fichero en la ruta **/etc/nginx/sites-available/imw.alu6462.me**. Hay que poner lo siguiente dentro:

![imw.alu6462.me_contenido](img/sitioweb1/2.png)

* Luego enlazaremos dicho fichero a la ruta **/etc/nginx/sites-enabled** usando el comando ln -s

![imw.alu6462.me_enlace](img/sitioweb1/3.png)

* Además de ello recargamos el servicio para que se cargue la configuracion de ngingx. Por otro lado creamos la carpeta imw dentro de webappps.

![imw.alu6462.me_comandos](img/sitioweb1/4.png)

![imw.alu6462.me_prueba](img/sitioweb1/5.png)

* A continuacion nos pasaremos con el comando scp una imagen de la máquina de desarrollo  a la máquina de producción.

![imw.alu6462.me_pasar_imagen](img/sitioweb1/6.png)

![imw.alu6462.me_lugar_imagen](img/sitioweb1/7.png)

* Despues de ello añadimos a nuestro fichero ***index.html*** la imagen que previamente nos hemos descargado.

![imw.alu6462.me_html](img/sitioweb1/8.png)

> Comprobamos como ha quedado ahora la pagina

![imw.alu6462.me_final1](img/sitioweb1/9.png)

* Finalmente creamos un location editando el fichero **/etc/nginx/sites-available/imw.alu6462.me**. Además crearemos un index.html con el enlace al Real decreto del título de Administración de Sistemas Informáticos en Red - MEC.

![imw.alu6462.me_finalcomandos](img/sitioweb1/10.png)

![imw.alu6462.me_final2](img/sitioweb1/11.png)

### Sitio web 2

* Creamos un virtual host llamado varlib.alu6462.me el cual se escuche por el puerto 9000 y este la opción de ***autoindex on*** para listar los archivos.

![varlib.alu6462.me_1](img/sitioweb2/1.png)

* Por otro lado creamos un enlace a la ruta **/etc/nginx/sites-enabled** usando el comando ln -s. Y al final recargamos el servicio de nginx.

![varlib.alu6462.me_2](img/sitioweb2/3.png)

* Para finalizar creamos otro enlace con nuestra carpeta **/var/lib** usando **ln -s**. Y nos tendría que salir lo siguinte:

![varlib.alu6462.me_3](img/sitioweb2/4.png)

![varlib.alu6462.me_4_final](img/sitioweb2/5.png) ### Sitio web 3

* Para empezar vamos a crear un virtual host llamado ssl.alu6462.me y su location. Estará dentro de la carpeta **/etc/nginx/sites-available/ssl.alu6462.me**. Enlazaremos a la carpeta **/etc/nginx/sites-enabled** y recargaremos la configuración de nginx.

![ssl.alu6462.me_1](img/sitioweb3/1.png)

* Luego crearemos una carpeta llamada students y dentro haremos un archivo index.html con el nombre de los compañeros de clase.

![ssl.alu6462.me_2](img/sitioweb3/2.png)

![ssl.alu6462.me_3](img/sitioweb3/3.png)

* A continuacion vamos a obtener los certificados SSL y configurar el sitio web que queramos para que utilice protocolo https. Para ello usaremos la aplicaion cerbot haciendo los siguiente:

![ssl.alu6462.me_4](img/sitioweb3/4.png)

![ssl.alu6462.me_5](img/sitioweb3/5.png)

* Luego vamos abrir cerbot usando ***sudo certbot --nginx***. Y lo configuramos de la siguiente forma:

![ssl.alu6462.me_6](img/sitioweb3/6.png)

* Reiniciamos el servicio nginx:

![ssl.alu6462.me_8](img/sitioweb3/8.png)

![ssl.alu6462.me_9](img/sitioweb3/9.png)

* Se prohibira el acceso al fichero .htpasswd creando una constraseña y un usuario. El usuario sera admim. Se realizara de la siguiente forma:

![ssl.alu6462.me_10](img/sitioweb3/12.png)

>Añadimos tambien dos lineas al archivo donde creamos el virtual host

![ssl.alu6462.me_9_final](img/sitioweb3/11.png)

### Sitio web 4

* Primeramente nos descargamos un archivo de github usando wget(Previamente descargado).

![ssl.alu6462.me_1](img/sitioweb4/1.png)

* Luego lo descomprimes usando unzip y lo guardas dentro de webapps.

![ssl.alu6462.me_3](img/sitioweb4/3.png)

![ssl.alu6462.me_4](img/sitioweb4/4.png)
>Al paso anterior hay que crear una virtual host llamada http://target.alu6462.me
* Reiniciamos el servicio nginx:

![redirect.alu6462.me_5](img/sitioweb4/5.png)

* Creamos la carpeta /var/log/nginx/redirect para que no nos de fallo en lo siguiente que vamos a hacer:

![redirect.alu6462.me_6](img/sitioweb4/6.png)

* Finalmente creamos un virtual host que redireccione con el anterior creado, para ello debe de escuchar por el puerto 80 y tener salida por el 301. Además de tener que guardar los error en la ruta especifica que nosotros le marcamos.

![redirect.alu6462.me_5](img/sitioweb4/7.png)

* Reiniciamos el servivio y una vez comprobado que redirige a donde queremos miramos si ha ocurrido algún error durante el proceso.

![redirect.alu6462.me_8](img/sitioweb4/8.png) ![redirect.alu6462.me_9_final](img/sitioweb4/9.png)
