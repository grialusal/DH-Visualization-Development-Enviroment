const webpack = require('webpack');
const config = {
	mode: 'development',
    entry:  __dirname + '/js/index.js',
    output: {
        path: __dirname + '/dist',
        filename: 'bundle.js',
    },
    module: {
	  rules: [
	    {
	      test: /\.m?js$/,
	      exclude: /(node_modules|bower_components)/,
	      use: {
	        loader: 'babel-loader',
	        options: {
	          presets: ['@babel/preset-env']
	        }
	      }
	    }
	  ]
	},
    resolve: {
        extensions: ['.js', '.css']
    },
     stats: {
         colors: true
     },
     devtool: 'inline-source-map'

};
module.exports = config;