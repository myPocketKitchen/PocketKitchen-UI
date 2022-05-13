const express = require('express')
const app = express()
const {spawn} = require('child_process');
require('dotenv').config()
const mongoURL = process.env.KEY;

var MongoClient = require('mongodb').MongoClient;
var fs = require("fs"),
    json;

app.set('view engine', 'ejs')

// -------------------------
// Connect to the db

var dbo;

MongoClient.connect(mongoURL, function(err, db) {
    if (err) throw err;
    dbo = db.db("food");
});

app.get('/', (req, res) => {
    // get data

    dbo.collection("records").find({}).toArray(function(err, result) {
        if (err) throw err;
        // Make output readable
        text = JSON.stringify(result)
        jason = JSON.parse(text);

        res.render("index")
      });
      
})

// -------------------------
// Post to client

app.post('/getdata', (req, res) => {
    // get data

    dbo.collection("records").find({}).toArray(function(err, result) {
        if (err) throw err;
        // console.log("I got here!")
        res.setHeader("Content-Type", "application/json");
        // Make output readable
        res.end(JSON.stringify(result));
        // console.log(JSON.stringify(result));
      });

})

app.post('/getrecipes', (req, res) => {
    // get recipes
    function delay(time) {
        return new Promise(resolve => setTimeout(resolve, time));
    }

    function readJsonFileSync(filepath, encoding){
        if (typeof (encoding) == 'undefined'){
            encoding = 'utf8';
        }
        var file = fs.readFileSync(filepath, encoding);
        return JSON.parse(file);
    }
    
    function getConfig(file){
    
        var filepath = __dirname + '/' + file;
        return readJsonFileSync(filepath);
    }

    // var ingredients2 = [];
    const PythonShell = require('python-shell').PythonShell;
    var ingredients = [];
    dbo.collection("records").find({}).project({_id:0, food:1}).toArray(function(err, ingredients1) {  
        ingredients1.forEach(function (arrayElement) {
            ingredients.push(arrayElement.food) 
            arg = JSON.stringify(ingredients) 
            console.log(arg)

            delay(1000).then(() => console.log('ran after 1 second1 passed'));

            var options = {
                    args: arg
                  };

            // // console.log(options)

            PythonShell.run('words2vec_rec.py', options, function (err) {
                if (err) throw err;
                console.log('finished');
            });
            
            delay(1000).then(() => console.log('ran after 1 second1 passed'));
            
            json = getConfig('sample.json');
            // // console.log(json)
            // fix this!
            // res.send(json);
        })
    });
});


// Makes local port that enables rapid prototyping

app.listen(process.env.PORT || 5000)