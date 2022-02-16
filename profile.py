  
import geni.portal as portal
import geni.rspec.pg as pg
import geni.rspec.igext as IG

pc = portal.Context()
request = pc.makeRequestRSpec()

tourDescription = \
"""
This profile provides the template for a compute node with Docker installed on Ubuntu 20.04
"""

#
# Setup the Tour info with the above description and instructions.
#  
tour = IG.Tour()
tour.Description(IG.Tour.TEXT,tourDescription)
request.addTour(tour)

prefixForIP = "192.168.1."
link = request.LAN("lan")

virt_engine = ["kvm", "docker", "singularity", "podman"]

for i in range(4):
  node = request.XenVM(virt_engine[i])
  node.cores = 8
  node.ram = 8192
  node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD"
  iface = node.addInterface("if" + str(i))
  iface.component_id = "eth1"
  iface.addAddress(pg.IPv4Address(prefixForIP + str(i + 1), "255.255.255.0"))
  link.addInterface(iface)
  cmd = "sudo bash /local/repository/install_" + virt_engine + ".sh"
  node.addService(pg.Execute(shell="sh", command=cmd))
  
pc.printRequestRSpec(request)
