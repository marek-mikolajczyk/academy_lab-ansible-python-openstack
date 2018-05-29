#!/usr/bin/python
import sys
import os
import subprocess
import signal
from subprocess import Popen, PIPE, STDOUT



def print_menu():       ## Your menu design here
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. connect tst001"
    print "2. connect tst002"
    print "3. connect tst003"
    print "4. connect tst004"
    print "5. connect tst005"
    print "6. connect tst006"
    print "7. switch to root"
    print "8. connect ilo"
        #    print "9. Exit"
        #    print  * "-"


loop=True

while loop:          ## While loop which will keep going until loop = False
   print_menu()    ## Displays menu
   choice = input('Enter your choice [1-5]: ')

   if choice==1:
        subprocess.call(['ssh', '-i', 'openstack_demo', '-l', 'centos', 'tst001'])
        #subprocess.call(['ssh', '-i', '/home/xxx/openstack_demo', '-l', 'centos', 'tst001'])
   elif choice==2:
        subprocess.call(['ssh', '-i', '/home/xxx/openstack_demo', '-l', 'centos', 'tst002'])
   elif choice==3:
            subprocess.call(['ssh', '-i', '/home/xxx/openstack_demo', '-l', 'centos', 'tst003'])
   elif choice==4:
                subprocess.call(['ssh', '-i', '/home/xxx/openstack_demo', '-l', 'centos', 'tst004'])
   elif choice==5:
                subprocess.call(['ssh', '-i', '/home/xxx/openstack_demo', '-l', 'centos', 'tst005'])
   elif choice==6:
                subprocess.call(['ssh', '-i', '/home/xxx/openstack_demo', '-l', 'centos', 'tst006'])
   elif choice==7:
            subprocess.call(['su', '-', 'root'])
   elif choice==8:
                subprocess.call(['ssh', '-l', 'admin', 'gen82'])
   else:
                raw_input("Wrong option selection. Enter any key to try again..")
