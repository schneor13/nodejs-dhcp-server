/**
 * ---------------------------------
 * NodeJS DHCP Server
 * author: schneor13
 * ---------------------------------
 */

console.log(`-- Starting Server.... ---`);

const dhcp = require("dhcp");
const server = dhcp.createServer({
    range: [
        "172.30.0.10", "172.30.255.255"
    ],
    forceOptions: ['hostname'], // Options that need to be sent, even if they were not requested
    /*static: {
        "11:22:33:44:55:66": "192.168.3.100"
    },*/
    // Option settings
    netmask: '255.255.0.0',
    router: [
        '172.30.0.1'
    ],
    dns: ["8.8.8.8", "8.8.4.4"],
    server: '172.30.0.1', // This is us
    hostname: function () {
        const hostname = `schneorhost${i++}`;
        console.log(`-- Hostname: ${hostname} .... ---`);
        return hostname;
    }
});

server.listen();

console.log(`-- Server Started.... ---`);