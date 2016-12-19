var webpack = require('webpack');
var path = require('path');
var BundleTracker = require('webpack-bundle-tracker');


var config = {
    
    entry: {
        user: "./static/user",
        home: "./home",
    },

  

  output: {
    path: "./static/js",
    filename: '[name].bundle.js'
  },

  	plugins: [
		new BundleTracker({filename: './webpack-stats.json'}),
	],
};
