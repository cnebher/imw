<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Probando PHP!!</title>
    </head>
    <body>
        <?php
            $nombre = $_POST["nombre"];
            $apellidos = $_POST["apellidos"];
            $salario = $_POST["salario"];
            $edad = $_POST["edad"];

            if ($salario => 1000 and $salario =< 2000){
              if ($edad > 45){
                $salario = $salario * 1,03
              }
            }
            echo ("Hola $nombre\n");
            echo ("$apellidos!\n");
            echo ("Su salario es: $salario €");
        ?>
    </body>
</html>
