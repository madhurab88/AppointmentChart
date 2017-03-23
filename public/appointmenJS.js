//
// Note:  adding the line:
//
//    var J = jQuery.noConflict();
//
// lets you change '$' everywhere in this file to 'J'.
//


function displayFields() {
    //alert("inside displayFields func");
    document.getElementById("newAppointmentForm").style.display="block";
    document.getElementById("newAppointment").style.display="none";

    
}
function undisplayFields() {
    //alert("inside displayFields func");
    document.getElementById("newAppointmentForm").style.display="none";
    document.getElementById("newAppointment").style.display="block";
    
}

function submitForm() {
    alert("form submit");
}

function ajax_search() {
    alert("Populate Search Result");
}
