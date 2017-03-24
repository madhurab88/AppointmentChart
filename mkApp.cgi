#!/usr/bin/env perl
use CGI;
my $cgi = new CGI;
my $jquery = "//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js";

print_page_header();
print_html_head_section();
print_html_body_section();

sub print_page_header {
    print "Content-type:  text/html\n\n";
}
sub print_html_head_section {
    print "<head>\n";
    print "<link rel='stylesheet' type='text/css' href='appointmentCSS.css'>\n";
    print "<script src='$jquery'  type='text/javascript'></script>\n";
    print "<script src='appointmenJS.js'    type='text/javascript'></script>\n";
    print "</head>\n";
}
sub print_html_body_section {
    print "<body>\n";
    print "<center>\n";
    print "<h1>Appointment Schedule</h1>\n";
    print qq{
       <input type="button" id="newAppointment" value="New"  onclick="displayFields()">
        <span id="info"></span><br>
    };
    print qq{ <div id="newAppointmentForm"  style="display:none;" ><form id="formid"  title="" method="post">

        <div>
            <input type="button" id="addButton"  name="submiaddButtontButton" value="ADD" onclick="submitAddForm()">
        
            <input type="button" id="cancelButton"  name="cancelButton" value="Cancel" onclick="undisplayFields()">
        </div>
    <br>\n
        <div >
            <label >Appointment Date</label>
            <input type="date"  min="2017-03-24" id="appDate" name="date" >
        </div><br>
        <div>
            <label >Appointment Time</label>
            <input type="time" id="appTime" name="time" >
        </div><br>
        <div>
            <label >Appointment Description</label>
            <input type="text" id="appDesc" name="desc" >
        </div>
    
        
 </form></div><br>};
    print qq{<div id="result"></div><br>\n};
	print qq{<input id ="appSearchTxt" type="text" name="search" placeholder="Enter the Search String..">};
	print qq{\t<input type="button" id="appSearchBt" value="Search"  >};
    print qq{<div id="displayTable"></div><br>\n};
    print "</center>\n";
    print "</body>\n";
}