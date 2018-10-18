# Installation Instructions

You will need administrator priveleges on whatever computer you bring to the
workshop. Please do not bring a computer where you do not have this!

If you have any issues with the following, please e-mail me at:
   ryan.pepper@soton.ac.uk

You must install everything *before* attending the workshop as we will not have time to
do so during the workshop - we have a lot of material to cover! If you get stuck, 
please do contact me well in advance - the install procedure for Docker in particular
can be quite involved, and if you e-mail me the night before it is unlikely I will be
able to help. Do not turn up to the workshop and try try to install things there!


# Lecture 01 Requirements - Containerisation

Everything we will do in this workshop will require the use of Docker, so this
is a key requirement.

## Docker Install Instructions

1. Please update your Operating System before attending installing any software. Please
   make sure you are using Windows 10 / macOS 10.13 or 10.14 / an up to date Linux distro.

2. Follow the installatio instructions for your operating system:
   
   Windows: https://docs.docker.com/docker-for-windows/install/
   	    
   MacOS: https://docs.docker.com/docker-for-mac/

   Linux: 
   	  Ubuntu: https://docs.docker.com/install/linux/docker-ce/ubuntu/
   	  CentOS: https://docs.docker.com/install/linux/docker-ce/centos/
   	  Debian: https://docs.docker.com/install/linux/docker-ce/debian/
   	  Fedora: https://docs.docker.com/install/linux/docker-ce/fedora/

3. Check that the install works by typing on the command line:

   >   docker run ubuntu:18.04

   This will download a minimal version of Ubuntu 18.04 in which we will
   work for many of the exercises. If this doesn't work, or you get stuck,
   please e-mail me!

# Lecture 02 Requirements - Version Control
  
  Linux: Check that Git is installed, and if not install through your package manager

  MacOS: Git is not installed by default, but running the command 'git' in the terminal
  	 prompts you to download XCode which containers C/C++ compilers and Git.
	 Install XCode as prompted. Try the command 'git' again. If that doesn't work,
	 contact me with the message you get.

  Windows: Install Git for Windows from here: https://gitforwindows.org/
  
	 Alternatively, if you are a Windows Subsystem for Linux
	 just install git through the package manager.


# Lecture 03 Requirements - Continuous integration and testing
  
  There are no requirements other than those listed above, or they will be installed
  during the workshop.

# Lecture 04 Documentation - Requirements
  
  There are no requirements other than those listed above, or they will	be installed
  during the workshop.

