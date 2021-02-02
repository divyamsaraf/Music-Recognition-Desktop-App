function recognize_songs() {

    console.log('hello world1');

    var pyshell =  require('python-shell');
    pyshell.run('1.py',  function  (err, results)  {
        if  (err)  throw err;
        console.log('1.py finished.');
       alert(results);
        // alert('Secs: '+ results[0] + '\n Song ID: ' + results[1] + '\n Song Name: '+ results[0][2]+ '\n Confidence: ' + results[0][3]+ '\n Offset: ' + results[0][4]+ '\n Offset Seconds: ' + results[0][5]+ '\n File_sha1: ' + results[0][6]);
       });

       

       
    // console.log(' finished.');
    // var python = require('child_process').spawn('python', ['./1.py']);
    // python.stdout.on('data',function(data){
    // console.log("data: ",data.toString('utf8'));
    // });

    // document.getElementById("detect").value = "hang on...";
    // var python = require("python-shell")
    // var path = require("path")
    
    // var options = {
    //     scriptPath : path.join(__dirname, "/python/"),
        // pythonPath : "C:\Users\divya\AppData\Local\Programs\Python\Python36"
    // }
    // console.log('hello world2');
    
    // var recog = new python ("1.py", options);
    // console.log('hello world3');
    
    // recog.end(function(err, code, message) {
    //     // document.getElementById("detect").value = "Recognize Songs : ";
    //     console.log('hello world4');
       
    // })
}

recognize_songs();