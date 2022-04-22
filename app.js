const express = require('express')
const app = express()
require('dotenv').config()
const mongoURL = process.env.KEY;

var MongoClient = require('mongodb').MongoClient;

app.set('view engine', 'ejs')

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

        res.setHeader("Content-Type", "application/json");
        // Make output readable
        res.end(JSON.stringify(result));
      });

})


// Makes local port that enables rapid prototyping

app.listen(process.env.PORT || 3000)
