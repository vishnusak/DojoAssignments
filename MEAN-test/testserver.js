var express = require('express'),
    bp      = require('body-parser'),
    fs      = require('fs'),
    request = require('request'),
    http    = require('http')
    PORT    = 8000

var app     = express()
app.use(express.static(__dirname))
app.use(bp.urlencoded({extended: true}))
app.use(bp.json())

// var url = "http://2.bp.blogspot.com/-DeV-rz20DAc/UUdquUwWCSI/AAAAAAAAAXU/FA6-5fWVKYM/s1600/cast-of-teenage-mutant-ninja-turtles-5.jpg",
    // fileName = "ninja.jpg"
var count = 1

app.get('/', function(req, res, next){
  res.locals = {}
  res.locals.pdt = "All Products"
  next()
}, function(req, res, next){
  res.locals.ord = "All Orders"
  next()
}, function(req, res, next){
  res.locals.cust = "All Customers"
  res.json(res.locals)
})

app.post('/show', function(req, res){
  console.log(req.body);
  var fileName = `image${count}`
  getImage(req.body.link, fileName, function(file){
    count++
    res.json(file)
  })
})

function getImage(url, file, callback){
  request.head(url, function(err, res, body){
    console.log(res.headers['content-length'])
    console.log(res.headers['content-type'])

    if (res.headers['content-type'].substring(0, 5) === 'image'){
      if (res.headers['content-type'].substring(6) === 'jpeg'){
        file = `${file}.jpg`
      }
      if (res.headers['content-type'].substring(6) === 'png'){
        file = `${file}.png`
      }
    }

    if (!res.headers['content-type']){
      file = `${file}.jpg`
    }

    console.log(file)

    request(url).pipe(fs.createWriteStream(file)).on('close', function(){
      callback(file)
    })
  })
}


app.listen(PORT, function(){
  console.log(`Server is up. Listening on port ${PORT}`)
})
