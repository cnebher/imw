# Mis series favoritas

## 1.- Creacion de una location

La pagina debe poder abrirse usando `http://alu6462.me/series/`. Para ello vamos a usar nuestro servidor web y creamos una location para el dominio.

* Como se trata de una location dentro de un virtual host haremos lo siguiente:

```console

alu6462@cloud:~$ sudo vi /etc/nginx/sites-available/alu6462.me
```
* Una vez creado el fichero escribimos lo siguiente:

```console
server {
    server_name alu6462.me;

    location /series {
        root /home/alu6462/webapps;
    }
}
```
Una vez creado el fichero con la location le haremos un enlace simbolico a `../sites-available/alu6462.me`. Esto habilitara el fichero creado anteriormente.

```console

alu6462@cloud:/etc/nginx/sites-enabled$ ls -l
total 0
lrwxrwxrwx 1 root root 35 sep 16 15:35 vps.claseando.es -> ../sites-available/alu6462.me
lrwxrwxrwx 1 root root 41 sep 16 15:32 hello.alu6462.me -> ../sites-available/hello.alu6462.me
alu6462@cloud:/etc/nginx/sites-enabled$ sudo systemctl reload nginx
alu6462@cloud:/etc/nginx/sites-enabled$
```
* Hay que recargar la aplicacion nginx para que se guarden los cambios.

>Usar `reload` y no `restart` para que nuetsro servidor web pueda seguir aceptando solicitudes.

![salida de comandos consola](img/1_imw.png)

## Editar la pagina

Una vez creada la location series debemos 
