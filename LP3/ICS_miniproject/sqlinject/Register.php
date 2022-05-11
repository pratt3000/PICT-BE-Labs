<?php
   include('session.php');
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "Hospital";

	// Create connection
	$conn = new mysqli($servername, $username, $password, $dbname);
	// Check connection
	if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
	}

	 if($_SERVER["REQUEST_METHOD"] == "POST") {
      // username and password sent from form 
           $gender='male';
          if(isset($_POST['gender'])) 
		{
        	if($_POST['gender'] == "female") {
            		$gender='female';
        	}
   	 }

      $name=$_POST["patientName"];
      $age=$_POST["patientAge"];
   
      $dob=$_POST["bday"];
      $address=$_POST["patientAddress"];
      $number=$_POST["phone"];
      $companynm=$_POST["CompanyName"];
      $insuranceno=$_POST["InsuranceAccountNo"];
      $date=$_POST["admissiondate"];
      $wardno=$_POST["WardNo"];
	
	$sql = "INSERT INTO Details  VALUES ('$name',
						'$age',
						'$gender',
						'$dob',
						'$address',
						'$number',
						'$companynm',
						'$insuranceno',
						'$date',
						'$wardno');";
	
	if ($conn->query($sql) === TRUE) {
    	echo "New record created successfully";
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
.label {
  color: white;
  padding: 8px;
}
/* Add padding to containers */
.container {
  padding: 16px;
  background-color: white;
}

/* Full-width input fields */
input[type=text], input[type=password]{
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}
input[type=tel], input[type=date],input[type=number]{
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}
input[type=text]:focus, input[type=password]:focus {
  background-color: #ddd;
  outline: none;
}

/* Overwrite default styles of hr */
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 15px;
}

/* Set a style for the submit button */
.registerbtn {
  background-color: #4CAF50;
  color: white;
  align:center;
  padding: 16px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 30%;
  opacity: 0.9;
}

.split {
  height: 100%;
  width: 50%;
  position: fixed;
  z-index: 1;
  top: 0;
  overflow-x: hidden;
  padding-top: 10px;
  padding-bottom: 5px;
}

.left {
  left: 0;
  background-color:white;
}

.right {
  right: 0;
  background-color: white;
  
}

.centered {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}

.centered img {
  width: 150px;
  border-radius: 50%;
}
</style>
</head>

<body background="Register.jpg">
<form action=""  method="post" >
  <div class="split right">
    <h1 style="color: #4CAF50;" align="center">Hospital Details</h1>
    <hr>
     <table>
	<tr>
	<td>
    		<label for="CompanyName"><b>Insurance Company Name</b></label>
	</td>
	<td>
    	<input type="text" placeholder="Enter Company Name" name="CompanyName" required>
	</td>
       </tr>
    <tr>
	<td>
    		<label for="InsuranceNO"><b>Insurance Account No</b></label></td>
        <td>
    		<input type="number" placeholder="Enter Insurance Account No" name="InsuranceAccountNo" required></td>
    </tr>
    
    
    <tr>
	<td>
    		<label for="admitdate"><b>Admit date</b></label>
	</td>
	<td>
    		<input type="date" name="admissiondate" max="2019-10-19" min="2019-10-18"></td>
    </tr>
	<tr>
        <td>
   		 <label for="WardNO"><b>Ward No</b></label>
	</td>
	<td>
   		 <input type="number" placeholder="Enter Ward No" name="WardNo" required>
	</td>
    </table>
    <center> <button type="submit" class="registerbtn"  method="post">ADD DETAILS</button></center></div>
   
  </div>
  
  
  <div class="split left">
    <h1 style="color: #4CAF50;" align="center">Personal Details</h1>
    <hr>
	<table>
	<tr>
	<td>
    		<label for="PatientName"><b>Patient Name</b></label>
	</td>
	<td>
    <input type="text" placeholder="FirstName   LastName" name="patientName" pattern="[A-Za-z]{2,50}[' ']{0,5}[A-Za-z]{2,50}$" title="enter valid name" required></td>
   
    <tr>
	<td>
    <label for="PatientAge"><b>Patient Age</b></label>
	</td>
	<td>
   	 <input type="number" placeholder="Enter Patient Age" name="patientAge" min=0 >
	</td>
    </tr>
    
	<tr>
	<td>
    	<label for="PatientGender"><b>Patient Gender</b></label>
	</td>
	<td>
    <input type="radio" name="gender" value="male" checked> Male
    <input type="radio" name="gender" value="female"> Female
    </td>
    
	<tr>
	<td>
    		<label for="PatientDOB"><b>Patient DOB</b></label></td>
	<td>
    		<input type="date" name="bday" max="2019-10-19" min="1919-10-18"></td>
	</tr>
	
	<tr>
	<td>
     		<label for="PatientAddress"><b>Patient Address</b></label></td>
	<td>
    		<input type="text" placeholder="Enter Patient Address" name="patientAddress" required></td>
    </tr>
    <tr>
     <td>
    <label for="phone"><b>Phone number</b></label></td>
    <td>
    <input type="tel" id="phone" name="phone" pattern="[0-9]{10}" required></td></tr>
	</table></div>   
     </form>

</body>
<script>
function validate()
 {
 
}
</script>
</html> 

