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
        "192.168.3.10", "192.168.3.99"
    ],
    forceOptions: ['hostname'], // Options that need to be sent, even if they were not requested
    static: {
        "11:22:33:44:55:66": "192.168.3.100"
    },
    // Option settings
    netmask: '255.255.255.0',
    router: [
        '192.168.0.1'
    ],
    dns: ["8.8.8.8", "8.8.4.4"],
    server: '192.168.0.1', // This is us
    hostname: function () {
        const hostname = `schneorhost${i++}`;
        console.log(`-- Hostname: ${hostname} .... ---`);
        return hostname;
    }
});

server.listen();

console.log(`-- Server Started.... ---`);