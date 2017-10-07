/**
 * ---------------------------------
 * NodeJS DHCP Client
 * author: schneor13
 * ---------------------------------
 */


let dhcp = require('dhcp');
let client = dhcp.createClient();

client.on('bound', function () {

    console.log("State: ", this._state);

    // `ip address add IP/MASK dev eth0`
    // `echo HOSTNAME > /etc/hostname && hostname HOSTNAME`
    // `ip route add default via 192.168.1.254`
    // `sysctl -w net.inet.ip.forwarding=1`

});

client.listen();

client.sendDiscover();