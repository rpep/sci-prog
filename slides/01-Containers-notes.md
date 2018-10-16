# Lecture 01 - Containers

## What are containers?  Containers provide a mechanism for setting up
a development or production environment for software through
controlling dependency versions and by laying out the necessary
installation steps to set that environment up. The environments that
are used by different people vary enormously - two people who work on
a piece of sofware might differ in their operating system choice, the
version of that operating system, their compiler or interpreter
versions, or on many other things. Containers provide a means for them
to install and isolate all of the necessary components needed to run a
piece of software in a *reproducible* manner.

## Isn't this a bit like a virtual machine?

Virtual machines (VM) are basically the same principle to a user. In
fact, depending on your operating system, your container may run in a
(lightweight) virtual machine. However, there are many advantages of
containers over virtual machines, which is one of the reasons that
they've become ubiquitous in professional software development.

## Dictionary
Some terminology you'll need to learn...

* Host - the computer on which you are running a container/virtual
  machine.

* Image - A binary file containing all of the necessary files,
  dependencies, etc.  Container - A particular instance of an image.  

* Hypervisor - A piece of software/hardware which runs virtual machines 

* Kernel - Core parts of an operating system that controls memory,
  I/O, the CPU, etc.

## Why use a container over a VM?

First we need to consider what a virtual machine actually does. A VM
effectively emulates the entirety of a computer with software - every
piece of hardware, from the processor to the sound card is virtually
reconstructed in software. This is expensive if you try and do it
naively. Since the mid '00s, consumer processors have provided some
hardware assistance which reduces the cost of virtualisation. However,
how much you can take advantage of this depends on the hypervisor
which you are using. Most virtualisation hypervisors are commercial
and expensive products which are targeted at the server market. That
leaves many developers using the free but very slow VirtualBox as the
basis for their virtual machines.


On Linux, there are a variety kernel features which allow process
isolation, partition of CPU and memory resources (cgroups and kernel
namespaces) and provision of virtual filesystems (such as
OverlayFS). These technologies began to emerge in the mid to late
2000s, as a way of providing an interface to run programmes in
isolation - that is, they cannot see resources such as files or memory
outside of that allocated to it.

Development of these technologies has basically culminated in several
competing products based upon the operating system features. There are two that you should be aware of when developing scientific software:

* Docker - Docker is the most widely used container technology around. It is used in all types of software development, from backend Javascript server code to 

* Singularity - Singularity is a (not yet very mature) containerisation standard which is designed to allow containers to run on HPC systems. It requires root permissions to *create* a container, but does not require root permissions to run a container. This means that you can build a container locally, push it to a supercomputer, and run it without any issues.

They ways of creating them are very similar, and in fact, in most cases you can use a Docker container as the basis for a Singularity container.



