## open vz notes:

- [link to virtualization intro paper](http://download.openvz.org/doc/openvz-intro.pdf)

- Three main virtualization approaches:
  * emulation
  * para-virtualization
  * operating-system level virtualization
  * Multi-server  (cluster) virtualization.

- Main kernal components:
  * isolation and virtualization
  * resource management
  * check-pointing
  * live migration

- Emulations:
  * Imitation of behavior of a computer or other electronic system with the help of another type of computer/system. *to run any non-modified operating system.*
  * The main disadvantages of emulation are low performance and low density.
  * Examples: VMware products, QEmu , Bochs , Parallels

- Paravirtualization :
  * Is a technique to run multiple modified OSs on top of a thin layer called a *hypervisor, or virtual machine monitor.*
  * Here guest OS needs to be modified.
  * Examples: Xen , UML.

- Operating system-level virtualization :
  * multiple isolated execution environments within a single operating system kernel.
  *  features dynamic resource management.
  * FreeBSD Jail , Solaris Zones/Containers ,Linux-VServer,OpenVZ and Virtuozzo.
