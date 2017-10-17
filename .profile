# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
	. "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

clear
# create the mount point if it doesn't exist
if [ ! -d "/media/pi/POLLEN" ] ; then
    sudo mkdir /media/pi/POLLEN
fi
sudo mount -t vfat /dev/sda1 /media/pi/POLLEN
# if the mount was successful
if [ -d "/media/pi/POLLEN/presentation" ] ; then
    pollinator/main
else
    echo "could not find /media/pi/POLLEN/presentation directory"
fi
