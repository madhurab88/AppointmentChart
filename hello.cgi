#!/usr/bin/env perl
use CGI;
my $cgi = new CGI;
print $cgi->header();
print <<"EOF";
<html>
<head>


<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<script>
//alert("hi..");
$(document).ready(function(){
	


    $("#searchButton").click(function(){
        alert("inside seacrh");
        getAppointments();
       
    });

    





});
</script>

</head>
<body style="padding-left:30px;" >
<style>
.btn {
    background-color: #008CBA; /* Green */
    border: none;
    border-radius: 12px;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
}
</style>
<link rel="stylesheet" type="text/css" href="custom.css">


<h1>Appointment Details</h1>
<title>Appointment Details</title>

<button id="newButton" class="btn" type="button">New </button><br>
<input type="text" name="searchString" id="searchStr" placeholder="Enter the Search String..">
<input id="searchButton" class="btn" type="submit" value="Search" >

</body>
</html>
EOF
