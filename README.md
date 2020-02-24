# SSH Attempt Report Application 

This Project contains python code and ansible roles to setup simple web application which shows the ssh attempt on the client machines.
This setup is explained in below steps:-

1. Alpha Client - It is a Python script [alphaclient.py](https://github.com/anup1384/alpha-ssh/blob/master/roles/alpha-client/templates/alphaclient.py) which runs on client machines as a systemd service. Script fetches the SSH attempts on machines and sends to Alpha Server on port 8080. Script logs are logged at /var/log/alpha-client/alphaclient.log.

2. Alpha Server - On Server I have used a socket connection which uses port 8080 on machine and gets the data from client machines and store it in db using script [alphaserver.py](https://github.com/anup1384/alpha-ssh/blob/master/roles/alpha-server/templates/alphaserver.py) which runs as systemd service and log the action logs at /var/log/alpha-server/alphaserver.log. Also, scripts creates a db and table if it doesn't exists.

3. Database Server - To store the data of SSH attempt count made on client machines. Database is runing on same server where alphaserver.py is running i.e Alpha Server Machine.

4. App Server - Read data from DB and visualizes the SSH attempt count on browser using script [app.py](https://github.com/anup1384/alpha-ssh/blob/master/roles/alpha-server/templates/app.py) which runs on port 8090 on machine as a systemd service and logs are logged at /var/log/alpha-server/applogs.log

5. Nginx - It is used as a proxy for app.py.

## Getting Started:-

Clone the repository and Execute the below mentioned steps.

Ansible cases valid only for Ubuntu 18.04.3 LTS.

### Prerequisites:-

```
Ubuntu 18 machine with below packages installed
* Ansible 2.7.5
* python3
```

## How To Use:-

Ansible execution - An Ansible inventory file named hosts which have the IP/hostname, User, Private Key of the client and server.I have updated the default static inventory in ansible.cfg conf. Different inventory can be used with -i option which will override the default inventory. 

Execute below steps for Server end configuration. Mysql will be installed in the Ansible role of Alpha Server as the application is dependent on DB. Ansible Vault is used for encryption of mysql password.

```
ansible-vault encrypt_string --vault-id ./ansible_vault  'Paste your mysql password here' --name 'mysql_root_password’
```
Update all required varibales in group_vars for alpha-server configuration at [group_vars/tag_service_alpha_server](https://github.com/anup1384/alpha-ssh/blob/master/group_vars/tag_service_alpha_server)

```
ansible-playbook alpha-server.yml  -e "target_host=tag_service_alpha_server" --vault-id ./ansible_vault   -vv
```

Execute below steps to configure Alpha Client.

Update all the required varibales in group_vars for alpha-client configuration at [group_vars/tag_service_alpha_client](https://github.com/anup1384/alpha-ssh/blob/master/group_vars/tag_service_alpha_client)

```
ansible-playbook alpha-client.yml -e "target_host=tag_service_alpha_client"  -vv
```


## Testing:-

To test the app, you need to attempt ssh login to client machines.

```
ssh username@client_ip
```

To view ssh attempt report, hit the IP of the Alpha Server.

![alphaserver-app](https://github.com/anup1384/alpha-ssh/blob/master/alphaserver.png)


## Authors

* **Anup Dubey** - *work* - [github](https://github.com/anup1384)

