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

//simple squared_sum function

// Write the function squared_sum here
function squared_sum($array){
    
     $sum = 0;
    foreach($array as $number){
       
        $sum += $number**2;
    	
    }
return $sum;
}

echo squared_sum([56, 65, 26, 86, 66, 34, 78, 74, 67, 18, 34, 73, 45, 67, 75, 10, 60, 80, 74, 16, 86, 34, 12, 23, 42, 72, 36, 3, 73, 9, 92, 81, 94, 54, 97, 74, 45, 55, 70, 94, 96, 81, 86, 86, 84, 4, 32, 8, 96, 86, 87, 18, 84, 87, 59, 48, 32, 90, 17, 22, 82, 79, 66, 28, 17, 14, 80, 83, 66, 36, 21, 89, 68, 2, 51, 65, 20, 87, 48, 5, 1, 16, 60, 53, 84, 90, 16, 2, 37, 73, 57, 70, 57, 69, 68, 1, 24, 40, 72, 97]);
//python class

// TODO: Implement the Car class here
class Car{
	public function __construct($brand, $make){
    $this->brand = $brand;
    $this->make = $make;
}
    function print_details(){
    	echo "This car is a $this->make $this->brand.";
        
    }
}

$car = new Car("Toyota", 2006);
$car->print_details();

?>
