var Perlcgi = require('spawn-perl').spawnPerlCGI;
var express = require('express')
  ,http = require('http')
  ,url = require('url')
  ,path = require('path');
var app = express();

app.use(express.static(__dirname + '/public'));
 
app.set('port', process.env.PORT || 3000);
 
 
app.get('/testAjax', function(req,res){
	var perl = new Perlcgi(path.join(__dirname, 'public/mySqlSearch.cgi'),req,null,function(err,data){
			//console.log("test..."+data);
			 
			if(err){
			console.log(err);
			}
			//console.log(data);
			//res.header(perl.getHeader());
			res.send(data);
			res.end();
		});  
}
);
app.get('/mkApp.cgi', function(req, res){
		
      var perl = new Perlcgi(path.join(__dirname, '/mkApp.cgi'),req,null,function(err,data){
			//console.log("test..."+data);
			 
			if(err){
			console.log(err);
			}

			res.header(perl.getHeader());
			res.write(data);
			res.end();
		});                    
   });

http.createServer(app).listen(app.get('port'), function(){
  console.log("Express server listening on port " + app.get('port'));
});