from netmiko import ConnectHandler
import time
device_type = "linux"

# command
cmd_1 = "apt install php -y "
cmd_2 = "apt install apache2 -y"
cmd_3 = "mkdir /var/www/html/loganalyzer"
cmd_4 = "wget http://download.adiscon.com/loganalyzer/loganalyzer-4.1.10.tar.gz"
cmd_5 = "tar -xzvf loganalyzer-4.1.10.tar.gz"
cmd_6 = "cp -r loganalyzer-4.1.10/src/* /var/www/html/loganalyzer"
cmd_7 = "cp -r loganalyzer-4.1.10/src/* /var/www/html/loganalyzer"
cmd_8 = "touch /var/www/html/loganalyzer/config.php "
cmd_9 = "chmod 666 /var/www/html/loganalyzer/config.php "
cmd_10 = "chmod 666 /var/log/syslog"
cmd_11 = "systemctl restart apache2 "

def script():
    print("Must login as root")
    time.sleep(2)
    print("script is only for debain base linux")
    username = input("username of device? ")
    password = input("Password of device? ")
    ip = input("Ip of device? ")
    ssh = ConnectHandler(ip=ip,username=username,device_type=device_type,password=password)
    am_iroot = "whoami"
    send_1 = ssh.send_command_timing(am_iroot)
    if  not "root" in send_1:
        print("you are not root, leaving script. ")
        ssh.disconnect()
    else:
        yes_no = input("Executing script, are you sure you want to run this script y/n ? ")
        if "n" in yes_no:
            print("leaving script")
            ssh.disconnect()
        else:
            for cmd in [cmd_1,cmd_2,cmd_3,cmd_4,cmd_5,cmd_6,cmd_7,cmd_8,cmd_9,cmd_10,cmd_11]:
                ssh.send_command_timing(cmd)
                time.sleep(.5)
        print("Finished installing syslog server.")





script()
