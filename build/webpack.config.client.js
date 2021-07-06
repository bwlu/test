const path = require('path')
const HTMLPlugin = require('html-webpack-plugin')
const webpack = require('webpack')
const merge = require('webpack-merge')
const ExtractPlugin = require('extract-text-webpack-plugin')
const baseConfig = require('./webpack.config.base.js')

const isDev = process.env.NODE_ENV === 'development'

const defaultPlugins = [
	new webpack.DefinePlugin({
	  'process.env': {
	    NODE_ENV: isDev ? '"development"' : '"production"'
	  }
	}),
	new HTMLPlugin({
		template: path.join(__dirname, 'template.html'),
		favicon: path.join(__dirname, 'favicon.ico')
	})
]
// 测试服务器配置
const devServer = {
	port: 8899,
	host: '0.0.0.0',
	overlay: {
		errors: true,
	},
	// contentBase: path.resolve(__dirname, '../dist'),
	headers: { 'Access-Control-Allow-Origin': '*' },
	// historyApiFallback: true,
	historyApiFallback: {
	  index: '/public/index.html'
	},
	proxy: {
	  // '/': 'http://127.0.0.1:8000',
	},
	hot: true
}

let config

if (isDev) {
	config = merge(baseConfig, {
		devtool: '#cheap-module-eval-source-map',
		module: {
			// 规则
			rules: [
				{
					test: /\.css/,
					use: [
						'style-loader',
						'css-loader',
						{
							loader: 'postcss-loader',
							options: {
								sourceMap: true,
							}
						}
					]
				}
			]
		},
		devServer,
		plugins: defaultPlugins.concat([
			new webpack.HotModuleReplacementPlugin(),
			new webpack.NoEmitOnErrorsPlugin()
		]),
	})
} else {
	config = merge(baseConfig, {
		entry: {
			app: path.join(__dirname, '../client/index.js'),
			vendor: ['vue']
		},
		output: {
			filename: '[name].[chunkhash:8].js',
		},
		module: {
			rules: [
				{
					test: /\.css/,
					use: ExtractPlugin.extract({
						fallback: 'style-loader',
						use: [
							'css-loader',
							{
								loader: 'postcss-loader',
								options: {
									sourceMap: true,
								}
							}
						]
					})
				}
			]
		},
		plugins: defaultPlugins.concat([
			new ExtractPlugin('styles.[contentHash:8].css'),
			new webpack.optimize.CommonsChunkPlugin({
				name: 'vendor'
			}),
			new webpack.optimize.CommonsChunkPlugin({
				name: 'runtime'
			})
		])
	})
}

module.exports = config
