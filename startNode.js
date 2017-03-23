var Perlcgi = require('spawn-perl').spawnPerlCGI;
var express = require('express')
  ,http = require('http')
  ,url = require('url')
  ,path = require('path');
var app = express();

app.use(express.static(__dirname + '/public'));
var script = path.join(__dirname, '/guest.cgi');
 
  app.set('port', process.env.PORT || 3000);
 
 
app.get('/guest.cgi', function(req, res){
      var perl = new Perlcgi(script,req,null,function(err,data){
			//console.log("test..."+data);
			 
			if(err){
			console.log(err);
			}

			res.header(perl.getHeader());
			res.write(data);
			res.end();
		});                    
   });

app.get('/hello.cgi', function(req, res){
		
      var perl = new Perlcgi(path.join(__dirname, '/hello.cgi'),req,null,function(err,data){
			//console.log("test..."+data);
			 
			if(err){
			console.log(err);
			}

			res.header(perl.getHeader());
			res.write(data);
			res.end();
		});                    
   });
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
app.post('/guest.cgi', function(req, res){
       var perl = new Perlcgi(script,req,null,function(err,data){
         
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