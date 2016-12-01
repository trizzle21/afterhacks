var webpack = require('webpack');
var path = require('path');


var config = {
      entry: {
        user: "./user",
        home: "./home",
    },

  

  output: {
    path: BUILD_DIR,
    filename: [name] + 'bundle.js'
  }
};
