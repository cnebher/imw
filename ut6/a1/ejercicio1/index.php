<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Probando PHP!!</title>
    </head>
    <body>
        <?php
            $random = mt_rand(1,2);
            if ($random == 1) {
              echo '<img src="img/1.jpg">' ;
            }
            else {
              echo'<img src="img/2.jpg">';
            }
        ?>
    </body>
</html>
