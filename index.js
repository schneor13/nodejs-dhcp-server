/**
 * ---------------------------------
 * NodeJS DHCP Server
 * author: schneor13
 * ---------------------------------
 */


let dhcp = require('dhcp');

let dhcpServer = dhcp.createServer({
    // System settings
    range: [
        "192.168.3.10",
        "192.168.3.99"
    ],
    static: {
        "11:22:33:44:55:66": "192.168.3.100"
    },

    // Option settings (there are MUCH more)
    netmask: '255.255.255.0',
    router: [
        '192.168.0.1'
    ],
    bootFile: function (req) {

        if (req.clientId === 'foo bar') {
            return 'x86linux.0';
        } else {
            return 'x64linux.0';
        }
    }
});

dhcpServer.listen();