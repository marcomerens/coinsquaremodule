/* Magic Mirror
 * Module: HelloWorld
 *
 * By Michael Teeuw https://michaelteeuw.nl
 * MIT Licensed.
 */
Module.register("COINSQUARE", {


	defaults: {
		base:"CAD",
		currencies:["BTC"]
	},
	start:function() {
		Log.log("Sending notification")
		var self=this
		setTimeout(function(){
			self.sendSocketNotification("DATA","")
			setInterval(function(){
				self.sendSocketNotification("DATA","")
				},60*1000) // update every minute
			}
			,1000)
	},


	socketNotificationReceived: function(notification,data){
		Log.log(notification+" notification received ")
		Log.log(data)
		var self=this
		if (notification==="DATA") {
			Log.log(data)
			self.config.quotes={}
			self.config.currencies.forEach(function(v){
				var quote=data.quotes.filter(function(d){return d.currency==v && d.base==self.config.base})[0]
				if (quote) {		
					self.config.quotes[v]=quote
				}
			})

			self.updateDom()
		}
	},


	getTemplate: function () {
		return "COINSQUARE.njk";
	},

	getTemplateData: function () {

		return this.config;
	}
	
});
