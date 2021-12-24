const token = "ODU2NDUyNTE5MDA2MTc1MjUz.YNBPkA.s0o_ktwONA7m2z0plpOgtSIorZI";
const Discord = require("discord.js");
const client = new Discord.Client();

client.login(token);

client.on('ready', ()=> {
    console.log('Bot is online.');
});