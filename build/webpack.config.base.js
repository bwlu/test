const path = require('path')

const isDev = process.env.NODE_ENV === 'development'

const config = {
  target: 'web',
  entry: path.join(__dirname, '../client/index.js'),
  output: {
    filename: 'bundle.[hash:8].js',
    path: path.join(__dirname, '../dist'),
	publicPath: isDev ? '/public/' : '/' //项目编译根路径
  },
  resolve: {
	  // 别名
  	  alias: {
  		  views: path.resolve(__dirname, '../client/views'),
  		  config: path.resolve(__dirname, '../client/config'),
  		  layout: path.resolve(__dirname, '../client/layout'),
  		  components: path.resolve(__dirname, '../client/components'),
  		  assets: path.resolve(__dirname, '../client/assets'),
  		  util: path.resolve(__dirname, '../client/util'),
  		  service: path.resolve(__dirname, '../client/service'),
  		  client: path.resolve(__dirname, '../client'),
  	  }
  },
  module: {
	// 规则
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {
        test: /\.jsx$/,
        loader: 'babel-loader'
      },
	  {
	    test: /\.js$/,
	    loader: 'babel-loader',
		exclude: /node_modules/
	  },
      {
        test: /\.(gif|jpg|jpeg|png|svg)$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 1024,
              name: 'resources/[name].[hash:8].[ext]'
            }
          }
        ]
      },
	  {
	      test: /\.(eot|svg|ttf|woff|woff2)(\?\S*)?$/,
	      loader: 'file-loader'
	  }
    ]
  }
}

module.exports = config
