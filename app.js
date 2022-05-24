const express = require('express')
const app = express()
const spawn = require("child_process").spawn;
require('dotenv').config()
const mongoURL = process.env.KEY;
var bodyParser=require("body-parser");

var MongoClient = require('mongodb').MongoClient;
var fs = require("fs"),
    json;

app.set('view engine', 'ejs')

// -------------------------
// Connect to the db

app.use(bodyParser.urlencoded({extended: true}))
app.use(bodyParser.json());
    
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

app.post('/expiry', function(req, res){
    var data = req.body; //prints john
    // var id = data["_id"]
    var mongo = require('mongodb');
    var o_id = new mongo.ObjectId(data["_id"]);
    const updateDoc = {
        $set: {
          "Expiry Date" : data["Expiry Date"]
        },
      };
    // // console.log(filter)
    // // console.log(updateDoc)
    dbo.collection("records").updateOne({'_id': o_id}, updateDoc);
    console.log("donezo")
});

app.post('/getrecipes', (req, res) => {
    const PythonShell = require('python-shell').PythonShell;

    function getIngredients() {
        // getIngredients returns a promise that resolves to an ingredients array
        return new Promise((resolve, reject) => {
            var ingredients = [];
            dbo.collection("records").find({}).project({"_id":0, "Item":1}).toArray(function(err, readout) {
                readout.forEach(function (arrayElement) {
                    ingredients.push(arrayElement.Item)
                    })
                    options = {
                        args : ingredients.join(', ')
                    }
                    // console.log(options)
                    resolve(options);
                })
        });
    }

    function getRecipes(arg) {
        return new Promise((resolve, reject) => {
            console.log(arg)
            PythonShell.run('./words2vec_rec.py', arg, function (err, result) {
                if (err) throw err;
                resolve(); // resolve the empty promise
            });
        })
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


    const ingredients = getIngredients();
    ingredients
        .then(getRecipes)
        // .then(function (responseObj) {
        //     return JSON.stringify(responseObj)
        // })
        .then(function () {
            file = getConfig('sample.json')
            // var string = JSON.parse(data)
            // console.log(string)
            res.send(file);
        });
});



//     function getIngredients() {
//         var ingredients = [];
//         dbo.collection("records").find({}).project({"_id":0, "Item":1}).toArray(function(err, readout) {
//             readout.forEach(function (arrayElement) {
//                 ingredients.push(arrayElement.Item)
//                 // console.log("Hello from inside getIngredients")
//                 // console.log(ingredients)
//                 // console.log(JSON.stringify(ingredients))
//                 // console.log(ingredients)
//                 // delay(1000).then(() => console.log('ran after 1 second1 passed'));
//                 })
//             })
//             // return options = {
//             //     args: arg
//             // };
//         return ingredients;
//     };
// });

// app.post('/getrecipes', (req, res) => {
//     // get recipes
//     // function delay(time) {
//     //     return new Promise(resolve => setTimeout(resolve, time));
//     // }

//     function readJsonFileSync(filepath, encoding){
//         if (typeof (encoding) == 'undefined'){
//             encoding = 'utf8';
//         }
//         var file = fs.readFileSync(filepath, encoding);
//         return JSON.parse(file);
//     }
    
//     function getConfig(file){
    
//         var filepath = __dirname + '/' + file;
//         return readJsonFileSync(filepath);
//     }

//     // var ingredients2 = [];
    // const PythonShell = require('python-shell').PythonShell;
    

//     // let test = true;

//     function getIngredients() {
//         var ingredients = [];
//         dbo.collection("records").find({}).project({"_id":0, "Item":1}).toArray(function(err, readout) {
//             readout.forEach(function (arrayElement) {
//                 ingredients.push(arrayElement.Item)
//                 console.log("Hello from inside getIngredients")
//                 console.log(ingredients)
//                 // console.log(JSON.stringify(ingredients))
//                 // console.log(ingredients)
//                 // delay(1000).then(() => console.log('ran after 1 second1 passed'));
//                 })
//             })
//             // return options = {
//             //     args: arg
//             // };
//         return ingredients;
//     };

//     // getIngredients();
//     // console.log(arg);
    
    


//     function getRecipes(arg) {
//         // console.log(arg)
//         PythonShell.run('words2vec_rec.py', arg, function (err) {
//             if (err) throw err;
//             console.log('finished');
//         });
//     }

//     function sendRecipes() {
//         json = getConfig('sample.json');
//         res.send(json)
//         console.log("finito completo")
//     }



//     async function waiter() {
//         const arg = await getIngredients();
//         console.log("hello from here 123123")
//         console.log(arg) 
//         getRecipes(arg);
//     }

//     async function waitress() {
//         const output = await waiter();
//         console.log(output)
//         sendRecipes();
//     }
    

//     waitress();
//     // sendRecipes();

//             // // console.log(options)

//             // PythonShell.run('words2vec_rec.py', options, function (err) {
//             //     if (err) throw err;
//             //     json = getConfig('sample.json');
//             //     res.send(json);
//             //     console.log('finished');
//             // });

//             // async function asyncCall() {
//             //     console.log('calling');
//             //     await cabbage();
//             //     json = getConfig('sample.json');
//             //     res.send(json);
//             //     console.log("success!")
//             //     // console.logresult);
//             //     // expected output: "resolved"
//             //   }
            
//             // await asyncCall();
//             // // console.log(json)
//             // fix this!
            
// });


// Makes local port that enables rapid prototyping

app.listen(process.env.PORT || 5000);