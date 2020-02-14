<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Probando PHP!!</title>
    </head>
    <body>
        <?php
            $name = $_POST["name"];
            $surnames = $_POST["surnames"];
            $salary = $_POST["salary"];
            $age = $_POST["age"];

            if ($salary > 1000 and $salary <= 2000){
              if ($age > 45){
                $salary = $salary + ($salary * 3 / 100);
              }
              elseif ($age <= 45){
                $salary = $salary + ($salary * 10 / 100);
              }
            }
            if ($salary <= 1000){
              if($age < 30){
                $salary = 1100;
              }
              elseif ($age >= 30 and $age <= 45){
                $salary = $salary + ($salary * 3 / 100);
              }
              elseif ($age > 45){
                $salary = $salary + ($salary * 15 / 100);
              }
            }
            echo ("Hola $name\n");
            echo ("$surnames!\n");
            echo ("Su salario es: $salary €");
        ?>
    </body>
</html>
