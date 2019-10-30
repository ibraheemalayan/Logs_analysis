# Logs Analysis - Udacity
### Full Stack Web Development ND
_______________________
## Prerequisites
* Python 3 > [https://realpython.com/installing-python/]
* Vagrant [https://www.vagrantup.com/docs/installation/]
* VirtualBox 3 [https://www.virtualbox.org/wiki/Downloads]
* psycopg2 [http://initd.org/psycopg/docs/install.html]

## Owner
Ibraheem Alyan

## Questions that the code will answer:
* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors? 

## Setup Instructions

### Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Ubuntu users: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

### Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from vagrantup.com. Install the version for your operating system.

Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

### Download the VM configuration
There are a couple of different ways you can download the VM configuration.

You can download and unzip this file: FSND-Virtual-Machine.zip
> (https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

Note: If you are using Windows OS you will find a Time Out error, to fix it use the new Vagrant file configuration
> (https://s3.amazonaws.com/video.udacity-data.com/topher/2019/March/5c7ebe7a_vagrant-configuration-windows/vagrant-configuration-windows.zip)
to replace you current Vagrant file.

Alternately, you can use Github to fork and clone the repository 
> (https://github.com/udacity/fullstack-nanodegree-vm)

Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory

### Start the virtual machine
From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.
When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!

### Logged in!
If you are now looking at a shell prompt that starts with the word vagrant (as in the above screenshot), congratulations — you've gotten logged into your Linux VM.

### The files for this project
Inside the VM, change directory to /vagrant and look around with ls.

The files you see here are the same as the ones in the vagrant subdirectory on your computer (where you started Vagrant from). Any file you create in one will be automatically shared to the other. This means that you can edit code in your favorite text editor, and run it inside the VM.

Files in the VM's /vagrant directory are shared with the vagrant folder on your computer. But other data inside the VM is not. For instance, the PostgreSQL database itself lives only inside the VM.

### Running the database
The PostgreSQL database server will automatically be started inside the VM. You can use the psql command-line tool to access it and run SQL statements

### Logging out and in
If you type exit (or Ctrl-D) at the shell prompt inside the VM, you will be logged out, and put back into your host computer's shell. To log back in, make sure you're in the same directory and type vagrant ssh again.

If you reboot your computer, you will need to run vagrant up to restart the VM

_______________________
## After installions

> make sure to install all the prerequisites above before continuing.
> the program python code is written in "code.py" file .
> before running "code.py" make sure to create the required views by running the SQL code in "views.sql" file .

## Code description
 I put my effort to do all the process in the DB engine with SQL, the python code is so simple, it only prints the output of the SQL code.

* for the first question, first the (articles_view_count) view will get the views fo each path that leads to an article then the first hard-coded query in the python code will obtain the top 3 articles from the view and print them.

* for the second question, (articles_views_authors) view will use the previous view with the author id added to it ,then the python hard-coded query will group the results by the author name summing for each author the views his articles got and it will print the authors list sorted by popularity.

* for the third question, (views_in_each_day) view calculates the number of requests in each day, and the (errors_in_each_day) view will count the requests the lead to errors each day, after that the python hard-coded query will divid the answers from (views_in_each_day)&(errors_in_each_day) to get the percentage of errors in each day and prints the ones above 1%.

## HOPE it works with you ... 

