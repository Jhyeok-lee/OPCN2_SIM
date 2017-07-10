setTimeout( function() {

  // Import Admin SDK
  var admin = require("firebase-admin");

  // Fetch the service account key JSON file contents
  var serviceAccount = require("opcn2-07a4ca0a60cc.json");

  // Initialize the app with a service account, granting admin privileges
  admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    databaseURL: "https://opcn2-ce140.firebaseio.com/"
  });

  // Get a database reference to our blog
  var db = admin.database();
  var ref = db.ref("/");
  var fs = require('fs');

  var latitude = fs.readFileSync('./latitude', 'utf8');
  var longitude = fs.readFileSync('./longitude', 'utf8');
  var ti = fs.readFileSync('./time', 'utf8');
  var pm1 = fs.readFileSync('./pm1', 'utf8');
  var pm2 = fs.readFileSync('./pm2', 'utf8');
  var pm10 = fs.readFileSync('./pm10', 'utf8');

  var logRef = ref.child(ti);
  logRef.set({
    Latitude: latitude,
    Longitude: longitude,
    Time: ti,
    PM1: pm1,
    PM2: pm2,
    PM10: pm10
  });

}, 1);

setTimeout(function () {
  process.exit();
}, 5000);
