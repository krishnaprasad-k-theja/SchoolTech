<!DOCTYPE html>
<html>

<head>
<style>



#nav1 {
    line-height:30px;
    background-color :#DB7093;
    height:450px;
    width:400px;
    float:left;
    padding:40px;
	margin:60px;
	
}


#nav2 {
    line-height:30px;
    background-color :#DB7093;
    height:450px;
    width:400px;
    float:right;
    padding:40px;
	margin:60px;
	
}



form fieldset a {
color: #5a5656;
font-size: 10px;
}
form fieldset a:hover { text-decoration: underline; }



</style>
</head>




<html>
<head>
<meta charset="utf-8">
<title>Student Attendance Management</title>

<style type="text/css">
body 
{
background-color: #f4f4f4;
text-align:center;
color: #5a5656;
font-family: 'Open Sans', Arial, Helvetica, sans-serif;
font-size: 16px;
line-height: 1.5em;
}
a { text-decoration: none; }
h1 { font-size: 1em; }
h1, p {
margin-bottom: 10px;
}
strong {
font-weight: bold;
}
.uppercase { text-transform: uppercase; }

/* ---------- LOGIN ---------- */
#login {
margin: 40px auto;
width: 350px;
height:300px;
}
form fieldset input[type="text"], input[type="password"] {
background-color: #e5e5e5;
border: none;
border-radius: 3px;
-moz-border-radius: 3px;
-webkit-border-radius: 3px;
color: #5a5656;
font-family: 'Open Sans', Arial, Helvetica, sans-serif;
font-size: 14px;
height: 30px;
outline: none;
padding: 0px 10px;
width: 250px;
-webkit-appearance:none;
}
form fieldset input[type="submit"] {
background-color: #008dde;
border: none;
border-radius: 3px;
-moz-border-radius: 3px;
-webkit-border-radius: 3px;
color: #f4f4f4;
cursor: pointer;
font-family: 'Open Sans', Arial, Helvetica, sans-serif;
height: 30px;
text-transform: uppercase;
width: 250px;
-webkit-appearance:none;
}

.btn-round {
background-color: #5a5656;
border-radius: 50%;
-moz-border-radius: 50%;
-webkit-border-radius: 50%;
color: #f4f4f4;
display: block;
font-size: 12px;
height: 50px;
line-height: 50px;
margin: 30px 125px;
text-align: center;
text-transform: uppercase;
width: 50px;
}


form fieldset input[type="submit"] {
background-color: #008dde;
border: none;
border-radius: 3px;
-moz-border-radius: 3px;
-webkit-border-radius: 3px;
color: #f4f4f4;
cursor: pointer;
font-family: 'Open Sans', Arial, Helvetica, sans-serif;
height: 30px;
text-transform: uppercase;
width: 250px;
-webkit-appearance:none;
}
form fieldset input[type="Register"] {
background-color: #008dde;
border: none;
border-radius: 3px;
-moz-border-radius: 3px;
-webkit-border-radius: 3px;
color: #000000;
cursor: pointer;
font-family: 'Open Sans', Arial, Helvetica, sans-serif;
height: 30px;
text-transform: uppercase;
width: 250px;
-webkit-appearance:none;
}




#footer {
    background-color:black;
    color:white;
    clear:both;
    text-align:right;
   padding:20px;	 	 
}




</style>

</head>





</head>





<body style="background-color:	#7FFFD4">

<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<title>Student Attendance Management</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="css/main.css">
<link rel="stylesheet" href="css/print.css" media="print">
<script src="js/jquery-1.6.4.min.js"></script>
<script src="js/custom.js"></script>
<!--[if lt IE 9]>
<script src="js/css3-mediaqueries.min.js"></script>
<script src="js/html5.js"></script>
<script src="js/IE9.js"></script>
<![endif]-->
<meta http-equiv="Content-Type" content="text/html;charset=utf-8">
  <title>Back to Home</title>
  <link rel="shortcut icon" href="http://designshack.net/favicon.ico">
  <link rel="icon" href="http://designshack.net/favicon.ico">
  <link rel="stylesheet" type="text/css" media="all" href="style.css">
  <script type="text/javascript" src="js/jquery-1.9.1.min.js"></script>
  <script type="text/javascript" charset="utf-8" src="js/jquery.leanModal.min.js"></script>
  <!-- jQuery plugin leanModal under MIT License http://leanmodal.finelysliced.com.au/ -->
</head>
<body>
<header class="clearFix">
  <div class="wrap"> <a id="logo" href="#">Student Attendence Management</a>
    <hr>
    <nav>
      <div id="nav"> <strong>Navigation</strong>
        <ul>
          <li class="active"> <a href="/Attendence/index.html">Home</a> </li>
          <li> <a href="#">Profile</a> </li>
                
          <li> <a href="/Attendence/home.jsp">Logout</a> </li>
        </ul>
      </div>
    </nav>
  </div>
</header>

<marquee><h1 style="color:#FF9933 " style="font-family:slicks" >Dont let your education slip away, Come to college everyday...You’ll never know what you missed unless you show up!</h1></marquee>
<center>
<h3 align="left" style="color:black " style="font-family:slicks" >
		Here student will check their attendence...</h3>
	<h4 align="left" >Enter Roll No.:<form name="frm" method="Get" style="background-color:	#7FFFD4" action="/Attendence/servlet/Search"><input type="text" name="srch" value="" >
		<input type="submit" value="search"></form></h4>
	
</center>
<div id="nav1">

<fieldset>

<div id="login">
<h1 style="color:black ">HOD login.</h1>
<form name="frm" method="Post" action="/Attendence/servlet/Check1">
<form action="javascript:void(0);" method="get">
<fieldset>

<p><input type="text" name="uid" required value="Username" onBlur="if(this.value=='')this.value='Username'" onFocus="if(this.value=='Username')this.value='' "></p>
<p><input type="password" name="psw" required value="Password" onBlur="if(this.value=='')this.value='Password'" onFocus="if(this.value=='Password')this.value='' "></p>
<p><a href="changepwd.jsp">Forgot Password?</a></p>
<p>
<input type="submit" value="Login" onclick="window.location.href='/Attendence/underlogin.html'">
</p>
<br>

</form>
</fieldset>

<form action="javascript:void(0);" method="get">
<fieldset>
<p>
<input type="submit" value="Register" onclick="window.location.href='/Attendence/hodregister.html'">
</p>
</form >
</fieldset>
</fieldset>	
	</div>

<div id="nav2">
<fieldset>

<div id="login">
<h1 style="color:black ">Faculty login.</h1>
<form name="frm" method="Post" action="/Attendence/servlet/Check">
<form action="javascript:void(0);" method="get">
<fieldset>

<p><input type="text" name="uid" required value="Username" onBlur="if(this.value=='')this.value='Username'" onFocus="if(this.value=='Username')this.value='' "></p>
<p><input type="password" name="psw" required value="Password" onBlur="if(this.value=='')this.value='Password'" onFocus="if(this.value=='Password')this.value='' "></p>
<p><a href="changepwd.jsp">Forgot Password?</a></p>
<p>
<input type="submit" value="Login" onclick="window.location.href='/Attendence/underlogin.html'">
</p>
<br>

</form>
</fieldset>

<form action="javascript:void(0);" method="get">
<fieldset>
<input type="submit" value="Register" onclick="window.location.href='/Attendence/register.html'">
</form >
</fieldset>
</fieldset>

</div>


<div id="footer">
<center>
<li><a href="/Attendence/home.jsp"> Home </a> | <a href="/Attendence/login.html"> Login </a> | <a href="#">  Profile </a>| <a href="#"> Help </a> |<a href="#"> Contacts Us </a></li>
</center>
<p class="floatRight"> Copyright &copy; 2015 <a href="#">Foolish Boys </a> &ndash; All Rights Reserved<br>
</div>

</body>

<!-- Mirrored from www.w3schools.com/html/tryit.asp?filename=tryhtml_layout_divs by HTTrack Website Copier/3.x [XR&CO'2014], Fri, 23 Jan 2015 07:20:27 GMT -->
</html>
