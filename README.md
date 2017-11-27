# ANSIBLE crash-course project:

![alt text][logo1]
 ![alt text][logo2]

## WHO: 

Red Hat product with commercial support;  
SW core is free and opensource  

[logo1]: https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Ansible_logo.svg/50px-Ansible_logo.svg.png "Logo Title Text 2"
[logo2]: https://upload.wikimedia.org/wikipedia/en/thumb/6/6c/RedHat.svg/150px-RedHat.svg.png "RedHatLinux logo"


## WHERE:

check roles and basics ["IT Automation LEGO blocks"] >> (http://galaxy.ansible.com)



## WHAT: 

* **configuration management tool (CM)**
* **set up** and **configure** servers (*webservers*, *dbservers*, *desktop workstations* etc.)
* **provisioning** and **status cecking** for *bare-metal*, *VMs*, etc.
* versioning files (CM, IaaS,)
* **managing** different _environments_ and their _statuses_
* used to **deploy** _web apps_, _configurations_ and even _full applications_
* **service orchestrations**
* ...



## HOW: 

`control host` >`nodes`  access is via **ssh**

* running "playbooks"
* assigning roles
* defining and orchestrating deployment steps through tasks
* using _modules_ 
* _substituting variables_ for maximum flexibility of code

---

##### CHECK ANSIBLE MODULES:

* cloud
* clustering
* commands
* databases
* files
* inventory
* messaging
* monitoring
* network
* notifications
* packaging
* source control (git, hg, subversion)
* system modules (mod authorized_key, cron, user, group, hostname)
* utilities modules
* web infrastructure modules
* ...

---


### MAIN FOLDER TREE-STRUCTURE (SKELETON)

`/etc/ansible`  

**HINT :** To manage multiple machines via _single controller_, use copies of the skeleton:

`$ cp /etc/ansible ~/my_new_project`  


### GENERAL PROJECT TREE STRUCTURE

`ansible.cfg` 		config file  
`playbook.yml`		playbookfile (not important its filename)  
`hosts`				files of hosts (fqdn or IPs)  
---
---


* `roles/`  
 * `/basic/{tasks,files}`  
 * `/role1/{tasks,files}`  
 * `/role2/{tasks,files}`  
    * `/tasks/main.yml`  
---
---

some alternative commands to quickly set up needed files:  

`$ mkdir -pv project_01/roles/{basic,role1,role2}/{tasks,files,handlers}`  
`$ touch project_01/{ansible.cfg,playbook.yml,hosts}`  
`$ touch project_01/roles/{basic,role1,role2}/{tasks,handlers}/main.yml`  
---

**ROLE** = list of commands executed on target host(s) in a given order  
**PLAYBOOK** = used to determine which role must apply to which host



### Setup controller-link in Linux 

`$ ssk-heygen`  
`$ ssh-copy-id <webserver>`  
`$ ssh <webserver>`  

### Add ansible repo to get latest version

`$ apt-add-repository ppa:ansible/ansible`  
`$ apt-get update`  
`$ apt-get install ansible`  




