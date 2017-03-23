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
    print qq{ <div id="newAppointmentForm"  style="display:none;" ><form id="formoid" action="studentFormInsert.php" title="" method="post">

        <div>
            <input type="button" id="addButton"  name="submiaddButtontButton" value="ADD" onclick="submitForm()">
        
            <input type="button" id="cancelButton"  name="cancelButton" value="Cancel" onclick="undisplayFields()">
        </div>
    <br>\n
        <div >
            <label >Date</label>
            <input type="text" id="date" name="date" >
        </div><br>
        <div>
            <label >Time</label>
            <input type="text" id="time" name="time" >
        </div><br>
        <div>
            <label >Description</label>
            <input type="text" id="desc" name="desc" >
        </div>
    
        
 </form></div><br>};
    
	print qq{<input type="text" name="search" placeholder="Enter the Search String..">};
	print qq{\t<input type="button" value="Search" onclick="ajax_search()" >};
    print qq{<div id="result"></div><br>\n};
    print "</center>\n";
    print "</body>\n";
}