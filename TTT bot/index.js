const Discord = require('discord.js')
const bot = new Discord.Client();
const client = new Discord.Client()
const ms = require("ms");

const token = 'NzMyMzc1NTAzMjg1MTI1Mjcw.Xwzr3g.TJglXLmXugBZIMYpwobWa8DMG4U';


var args;
var trigger;



bot.on('message', () => {
  if (trigger == true){
    var generalChannel = bot.channels.get("732050200574820492") // Replace with known channel ID
    generalChannel.send("!TTTmute" + args);
    trigger = false
  }


})



var dgram = require("dgram");
  var fs = require("fs");
  var stream = fs.createWriteStream("received.json",{ flags: 'w',
    encoding: "utf8",
    mode: 0666 });
 var server = dgram.createSocket("udp4");

server.on("message", function (msg, rinfo) {
  console.log("server got: " + msg + " from " +
    rinfo.address + ":" + rinfo.port);
    stream.write(msg);
    args = msg.toString()
    trigger =true;
});


  
    
   


const PREFIX = '!TTT';




bot.on('message',message=>{

    if (!message.content.startsWith(PREFIX) || message.author.bot) return;

   
        let args = message.content.substring(PREFIX.length).split(" ");
        
        switch (args[0]){
            case 'mute':
           

            var person = message.guild.member(message.mentions.users.first() || message.guild.members.get(args[1]))
            if(!person) return message.reply("No member fond"); 

            var role1 = message.guild.roles.cache.find(role => role.name === "TTTMute");
            var role2 = message.guild.roles.cache.find(role => role.name === "TTTSpeak");

            if (!role1) return message.reply("no role found");
        }
        
        person.roles.add(role1.id);
        person.roles.remove(role2.id);
        

        setTimeout(function(){
        person.roles.add(role2.id);
        person.roles.remove(role1.id);
        }, 10000);
    
    
})

bot.login(token);

bot.on('ready',()=>{
  console.log('Bot started')
})




server.on("listening", function () {
  var address = server.address();
  console.log("server listening " +
      address.address + ":" + address.port);
      
});

server.bind(41234);
// server listening 0.0.0.0:41234

        

bot.login(token);

