from pythonping import ping

def fetch_status():
    hosts = {
       "Firewall": {
          "name" : "Firewall",
          "ip": "172.168.0.1",
          "status": ""
       },
       "Casa OS": {
          "name" : "Casa OS",
          "ip": "172.168.0.195",
          "status": ""
       },
       "IDRAC": {
          "name" : "IDRAC",
          "ip": "172.168.0.125",
          "status": ""
       },
       "Switch": {
          "name" : "Switch",
          "ip": "172.168.0.10",
          "status": ""
       },
       "Proxmox-1": {
          "name" : "Proxmox-1",
          "ip": "172.168.0.167",
          "status": ""
       },
       "Proxmox-2": {
          "name" : "Proxmox-1",
          "ip": "172.168.100.213",
          "status": ""
       },
       "Elegoo": {
          "name" : "Elegoo",
          "ip": "172.168.0.165",
          "status": ""
       },
       "Docker Server": {
          "name" : "Docker Server",
          "ip": "172.168.201",
          "status": ""
       },
       "Gitea": {
          "name" : "Gitea",
          "ip": "172.168.0.166",
          "status": ""
       },
       "OKD": {
          "name" : "OKD",
          "ip": "172.168.0.196",
          "status": ""
       },
       "AP": {
          "name" : "AP",
          "ip": "172.168.112.1",
          "status": ""
       },
    }

    for x, host in hosts.items():
        response = ping(host["ip"], count=2)
        if response.success():
            host["status"] = "up"     
        else:
            host["status"] = "down"

    return hosts
