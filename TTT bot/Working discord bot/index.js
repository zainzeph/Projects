const Discord = require('discord.js')
const bot = new Discord.Client();
const ms = require("ms");

const token = 'NzMyMzc1NTAzMjg1MTI1Mjcw.Xwzr3g.TJglXLmXugBZIMYpwobWa8DMG4U';



const PREFIX = '!TTT';






const client = new Discord.Client()

client.on('ready', () => {
    const generalChannel = client.channels.cache.get("732050200574820492") // Replace with known channel ID
    generalChannel.channel.send("!TTTmute @Zainzephninja")  
})



bot.on('ready',()=>{
    console.log('Bot started')
})


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

