/**
 * ---------------------------------
 * NodeJS DHCP Client
 * author: schneor13
 * ---------------------------------
 */


const dhcp = require("dhcp");
const dhcpClient = dhcp.createClient();

dhcpClient.on('bound', function (state) {

    console.log("State: ", state);

    // Configure your host system, based on the current state:
    // `ip address add IP/MASK dev eth0`
    // `echo HOSTNAME > /etc/hostname && hostname HOSTNAME`
    // `ip route add default via 192.168.1.254`
    // `sysctl -w net.inet.ip.forwarding=1`

});

dhcpClient.listen();

dhcpClient.sendDiscover();