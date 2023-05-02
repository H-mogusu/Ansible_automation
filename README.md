# Ansible_automation
created 5 servers on cleura
==>Bastion
==>HAproxy
==>devA
==>devB
==>devC

Gave Bastion and HAproxy floating IP -enable external access
devA//devB//devC -no external IP. acccessed from outside through JUmp server


configured SSH Login and assigned the configure path to private key
configured site.yaml file ---==playbook
configured .cfg to linking inventory to out hosts configs
created a hosts file (our inventory)
configured the HAproxy file and assigned it roundrobin type of load balancing
create flask app in python3

run ansible command,  $ansible-playbook site.yaml -i hosts

Activities:

Install Python3-pip 
Install flask for Python3 using the 'pip3' executable
uploading the application2.py application on devA/devB/devC (webservers)
Install  HAproxy 
uploading HAproxy configuration on the HAproxy server





