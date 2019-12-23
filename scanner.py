import nmap

nm = nmap.PortScanner()

print("Welcome!!!")
print("<---------------------------------------------------->")

ip_addr = input("Enter the target IP address: ")
print("The entered IP address is: ", ip_addr)
type(ip_addr)

nm.scan(ip_addr, '22-443')

for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
