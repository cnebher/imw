<!doctype html>
<html>
    <head>
        <title>Probando PHP!!</title>
    </head>
    <body>
      <form action="index.php" method="post">
        ¿Número de filas?<input type="number" name="rows"><br/>
        ¿Numero de columnas?<input type="number" name="columns"><br>
        <input type="submit" name="send" value="Enviar">
      </form>
      <table border = "2">
        <?php
        if (isset($_POST["rows"]) and isset($_POST["columns"])) {
            $rows = (int)$_POST["rows"];
            $columns = (int)$_POST["columns"];
            $number_rows = 1;
            $number_columns = 1;
            if ($rows >= 1 and $columns >= 1) {
                echo("<p>$rows filas y $columns columnas.<p/>");
                while ($number_rows <= $rows) {
                    $number_rows++;
                    echo("<tr>");
                    while ($number_columns <= $columns) {
                        $number_columns++;
                        echo("<td>1</td>");
                    }
                    $number_columns = 1;
                    echo("</tr>");
                }
            }
            else{
                echo("Error");
            }
        }

        ?>
        <table/>
    </body>
</html>
