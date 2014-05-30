Table

:name: saikrishna
:Topic: openstack notes

.. contents:: **Table of contents**

.. sectnum::
   :suffix: .
   
   
   
Installation
============
devstack - clone - ./stack.sh

working with the commands
=========================
+ For openstack commands to work , when installed with devstack:
+ source openrc admin admin
+ source openrc demo demo

Get the cloud image
===================

+ `images`_  Chapter 2. Get images
.. _`images`: http://docs.openstack.org/image-guide/content/ch_obtaining_images.html

Launching a VM
==============
+ add a ssh key to vm:
   - Do this on my local machene : ssh-keygen -t rsa -f OPenstack_MAchine
   - copy the key to dashboard while creating if it is being done from dashboard.

+ add a image to openstack: glance image-create --name ubuntu_qcow --disk-format qcow2 --container-format bare --file /home/openstack/Downloads/precise-server-cloudimg-amd64-disk1.img 
+ boot a vm from nova:  nova boot --flavor 2 --key_name OPenstack_MAchine --image dd47f229-5769-4265-96bf-f085282f77fb myinstance
+ once instance is **Active** in nova-list, login with ssh -i cloud.key.pub ubuntu@10.0.0.3

