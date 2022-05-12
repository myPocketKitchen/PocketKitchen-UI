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

    // var dataToSend;
    // // spawn new child process to call the python script
    // const python = spawn('python', ['print-test.py']);
    // // collect data from script
    // python.stdout.on('data', function (data) {
    //     console.log('Pipe data from python script ...');
    //     dataToSend = data.toString();
    // //     });
    // // // in close event we are sure that stream from child process is closed
    // python.on('close', (code) => {
    //     console.log(`child process close all stdio with code ${code}`);
    //     // send data to browser
    // //     // res.send(dataToSend)
    //     console.log(dataToSend)
    // });

    const PythonShell = require('python-shell').PythonShell;

    PythonShell.run('words2vec_rec.py', null, function (err) {
        if (err) throw err;
        console.log('finished');
        });
        
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
    
    //assume that config.json is in application root
    
    json = getConfig('sample.json');
    console.log(json)

})

// -------------------------
// Post to client

app.post('/getdata', (req, res) => {
    // get data

    dbo.collection("records").find({}).toArray(function(err, result) {
        if (err) throw err;
        console.log("I got here!")
        res.setHeader("Content-Type", "application/json");
        // Make output readable
        res.end(JSON.stringify(result));
      });

})

app.post('/getrecipes', (req, res) => {
    // get recipes
    

})


// Makes local port that enables rapid prototyping

app.listen(process.env.PORT || 5000)