const express = require('express')
const port = 3000

var app = express();



  
app.get("/hello", function (req, res) {
    
    setTimeout( () => { res.json({'name':'server live','id':'4219'}) },2000)

});


app.listen(3000, function () {
    console.log("Live at port 3000");
});
