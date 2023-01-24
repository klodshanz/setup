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

  - name: Creating a file with content
    copy:
      dest: "/etc/environment"
      content: |
        export http_proxy=http://proxy-server:8080
        export https_proxy=https://proxy-server:8080
        export no_proxy=localhost
~~~
