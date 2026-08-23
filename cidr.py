import ipaddress
def inspect_subnet(cidr: str) -> dict:
    net = ipaddress.ip_network(cidr, strict=False)
    return {'netmask': str(net.netmask), 'total_hosts': net.num_addresses, 'first_ip': str(net.network_address), 'last_ip': str(net.broadcast_address)}
