<?php
   include('session.php');
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "Hospital";

	// Create connection
	$conn = new mysqli($servername, $username, $password, $dbname);
	// Check connection
	if ($conn->connect_error) 
	{
   			 die("Connection failed: " . $conn->connect_error);
	}

	 if($_SERVER["REQUEST_METHOD"] == "POST") 
	{
             $id=$_POST["empid"];
             $password=$_POST["psw"];
   
		$sql = "update Admin set  passcode='$password' where empid='$id'";
	
		if ($conn->query($sql) === TRUE) 
		{
    		echo "New record created successfully";
		 header('location: Login1.php');
		} else {
    		echo "Error: " . $sql . "<br>" . $conn->error;
		}

	}

?>
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  font-family: Arial, Helvetica, sans-serif;
  background-color: white;
}

* {
  box-sizing: border-box;
}

/* Add padding to containers */
.container {
  padding: 16px;
  background-color: white;
  max-width: 500px;
}

/* Full-width input fields */
input[type=text], input[type=password],input[type=number] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

input[type=text]:focus, input[type=password]:focus ,input[type=number]:focus{
  background-color: #ddd;
  outline: none;
}

/* Overwrite default styles of hr */
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}

/* Set a style for the submit button */
.registerbtn {
  background-color: #4CAF50;
  color: white;
  padding: 16px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 30%;
  opacity: 0.9;
}

.registerbtn:hover {
  opacity: 1;
}

/* Add a blue text color to links */
a {
  color: dodgerblue;
}

/* Set a grey background color and center the text of the "sign in" section */
.signin {
  background-color: #f1f1f1;
  text-align: center;
}

h1 { color: #4CAF50; }
</style>
</head>
<body background="Forget.jpg">

<form action="" method="post">
  <div class="container">
  <center>
    <h1 >Reset Password</h1>
    <p>Please fill in this form to Reset Password.</p>
    <hr>
	<table>
	<tr>
	<td>
    		<label for="Employee ID"><b>Employee ID</b></label>
	</td>
	<td>
   		 <input type="number" placeholder="Enter Employee ID" name="empid" required>
	</td>
	</tr>
	<tr>
		<td>
    			<label for="psw"><b>New Password</b></label>
		</td>
		<td>
   		 <input type="password" placeholder="Enter Password" name="psw" required>
		</td>
	</tr>
	<tr>
		<td>
   	 		<label for="psw-repeat"><b>Repeat Password</b></label>
		</td>
		<td>
    			<input type="password" placeholder="Repeat Password" name="psw-repeat" required>
		</td>
	</tr>
    <hr>
	</table>
    <p>By creating an account you agree to our <a href="#">Terms & Privacy</a>.</p>

    <button type="submit" class="registerbtn" method="post">Register</button>
  </div>
  </center>
  
</form>

</body>
</html>
