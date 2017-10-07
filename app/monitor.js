/**
 * ---------------------------------
 * NodeJS DHCP Server
 * author: schneor13
 * ---------------------------------
 */

console.log(`-- Starting Monitor.... ---`);

const dhcp = require('dhcp');
const monitor = dhcp.createBroadcastHandler();

monitor.on('message', function (data) {

    if (data.options[53] === dhcp.DHCPDISCOVER) {
        if (data.chaddr === '12-34-56-78-90-AB') {
            console.log('Welcome home!');
        }
    }
});

monitor.listen();

console.log(`-- Monitoring.... ---`);