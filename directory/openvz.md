## open vz notes:

- [link to virtualization intro paper](http://download.openvz.org/doc/openvz-intro.pdf)

- virtualization approaches:
  * emulation
  * para-virtualization
  * operating-system level virtualization, and
  * HVM

- Main kernal components:
  * isolation and virtualization
  * resource management
  * check-pointing
  * live migration

- Emulations:
  * Imitation of behavior of a computer or other electronic system with the help of another type of computer/system. **to run any non-modified operating system.**
  * The main disadvantages of emulation are low performance and low density.
  * Examples: VMware products, QEmu , Bochs , Parallels

- Paravirtualization :
  * Is a technique to run multiple modified OSs on top of a thin layer called a **hypervisor, or virtual machine monitor.**
  * Here guest OS needs to be modified.
  * Examples: Xen , UML.

- HVM:
  * Stands for Hardware-assisted virtual machine. It provides complete hardware isolation. The hardware provides support to run independently for each OS.
- PV on HVM
  * Paravirtual guests traditionally performed better with storage and network operations than HVM guests because they could leverage special drivers for I/O that avoided the overhead of emulating network and disk hardware, whereas HVM guests had to translate these instructions to emulated hardware. Now these PV drivers are available for HVM guests, so operating systems that cannot be ported to run in a paravirtualized environment can still see performance advantages in storage and network I/O by using them. With these PV on HVM drivers, HVM guests can get the same, or better, performance than paravirtual guests.

- Operating system-level virtualization :
  * multiple isolated execution environments within a single operating system kernel.
  *  **features dynamic resource management.**
  * Examples: FreeBSD Jail , Solaris Zones/Containers ,Linux-VServer,OpenVZ and Virtuozzo.
