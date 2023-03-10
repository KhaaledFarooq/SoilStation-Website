<?php
$dbhost = 'localhost';
$dbuser = 'root';
$dbpass = '';
$dbname = 'soilstation';

$conn = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname);

if (!$conn)
{
 die('Could not connect: ' . mysqli_error($conn));
}
else{
mysqli_select_db($conn, $dbname);	
echo("connection established");	
}

?>