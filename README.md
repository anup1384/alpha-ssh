# SSH Attempt Report

It contain ansible roles to setup simple web application that show the ssh attempt on the client machines.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
Ansible 2.7.5
python3
mysql
nginx
```

### Installing

Initalize and configure the ansible role to setup entire application.
```
ansible-galaxy init alpha-client --init-path=./roles --offline

```
Ansible cases valid only for ubuntu-18.04.

Python - at client end, to send the report of ssh attempt to server.

## How To Use

Ansible execution - We can pass inventory with -i option or can configure inventory file. We can limit the execution with -l
To configure server end configuration:

```
ansible-playbook alpha-server.yml  -e "target_host=tag_service_alpha_server" --vault-id ./ansible_vault   -vv
```

To configure client end configuration.

```
ansible-playbook alpha-client.yml -e "target_host=tag_service_alpha_client"  -vv
```


## Testing

To test the working of the app, you need to attempt ssh login to clients.

```
ssh username@client_ip
```

To view ssh attempt report, hit the IP of the Server.

## Authors

* **Anup Dubey** - *work* - [github](https://github.com/anup1384)

