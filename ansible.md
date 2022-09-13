Minimal Ansible File

~~~YAML
---
- name: Sample Ansible File
  hosts: webservers
  remote_user: root

  tasks:

  - debug: Debug Messages Like This
    msg: "System {{ inventory_hostname }} has gateway {{ ansible_default_ipv4.gateway }}"

  - shell: /usr/bin/uptime
    register: result

  - debug: Printing Debug Information
    var: result
    verbosity: 2
~~~
