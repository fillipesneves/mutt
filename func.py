import os



def mostrarRota():
    r = os.popen("route").read()
    print(r)


def tracarRota(host):
    r = os.popen("traceroute "+host).read()
    print(r)


def mapearHost(host):
    r = os.popen("nmap -sV "+host).read()
    print(r)




