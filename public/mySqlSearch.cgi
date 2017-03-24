#!\Perl\bin\perl.exe
use DBI;
use JSON;
use CGI;

my $cgi = new CGI;
# Connect to the database.
my $dbh = DBI->connect("DBI:Pg:dbname=postgres;host=localhost", "postgres", "password", {'RaiseError' => 1});
my $filterQuery = $cgi->param("filterQuery");

# execute SELECT query
my $sth;
if($filterQuery ne ""){
	$filterQuery = "%".$filterQuery."%";
	$sth = $dbh->prepare("SELECT	apntmnt_desc, apntmnt_time FROM appointments where upper(apntmnt_desc) like upper(?)");
	$sth->execute($filterQuery);
}else{
	$sth = $dbh->prepare("SELECT	apntmnt_desc, apntmnt_time FROM appointments");
	$sth->execute();
}

my $data = $dbh->selectall_arrayref($sth);
print "Content-type:  application/json\n\n";
my $op = JSON -> new -> utf8 -> pretty(1);
my $json = $op -> encode({
    appointments => $data
});

print $json;
# clean up
$dbh->disconnect();