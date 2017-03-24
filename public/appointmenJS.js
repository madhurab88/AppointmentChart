
$(document).ready(function(){
    $("#appSearchBt").click(function(){
       getAppointments();
	   
	   //alert($("#appSearchTxt").val());
    });
});

/*function ajax_form() {
    alert("Populate FORM");
}*/

function getAppointments() {
    //alert("Populate Search Result");
	var table ;
	$('#myAppTab').remove();
	$('#displayTable').html("<table id='myAppTab'> <tr> <th>Date</th> <th>Time</th> <th>Description</th> </tr> </table>");
	var ss = $("#appSearchTxt").val();
	$.get("testAjax",{filterQuery:ss},function(myObj){
		//alert(myObj);
		
		$.each(JSON.parse(myObj), function(index, value){
			$.each(value,function(ind, val){
					table += "<tr><td>"+getDate(val[1])+"</td><td>"+getTime(val[1])+"</td><td>"+val[0]+"</td>";
			}
			);			
		});
		$('#myAppTab').append(table);
	} );	
}

function displayFields() {
    //alert("inside displayFields func");
    document.getElementById("newAppointmentForm").style.display="block";
    document.getElementById("newAppointment").style.display="none";

    
}
function undisplayFields() {
    //alert("inside displayFields func");
    document.getElementById("newAppointmentForm").style.display="none";
    document.getElementById("newAppointment").style.display="block";
    	$('#appDate').val('');
    	$('#appTime').val('');
    	$('#appDesc').val('');
    
}

function submitAddForm(){
	alert("Insert New row..");
}

function getDate(timestamp){
	var dat;
	var t = timestamp.replace(" ",".").split(".");
	dat = t[0];
	return dat;
}

function getTime(timestamp){
	var dat;
	var t = timestamp.replace(" ",".").split(".");
	dat = t[1];
	return dat;
}