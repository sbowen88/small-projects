<?php function g($a, $b) {
  echo $a*$b;
}

$odd_numbers = [1,3,5,7,9];
unset($odd_numbers[2]); 
print_r($odd_numbers);
echo("stuff");
// for loop 
$odd_numbers = [1,3,5,7,9];
for ($i = 0; $i < count($odd_numbers); $i=$i+1) {
    $odd_number = $odd_numbers[$i];
    echo $odd_number . "\n";
}

// simple foreach
$even_numbers = [2,4,6,8,10,12,14,16,18,20];

foreach($even_numbers as $even_number){
echo $even_number . "\n";
}
?>
