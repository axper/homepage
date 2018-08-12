Deployment
==========

1. Install ansible on Development machine
2. Add server's SSH keys to Development machine's `~/.ssh`
3. Add server's domain/ip to ansible's `/etc/ansible/hosts` file
4. Add `ansible_user` variable to
`/etc/ansible/host_vars/DOMAIN_NAME.yml` (set DOMAIN_NAME to your
site's domain name)
5. Add the following variables to to
`/etc/ansible/host_vars/DOMAIN_NAME.yml`,  optionally encrypt it with
ansible-vault, see
http://docs.ansible.com/ansible/latest/playbooks_vault.html
    1. `django_secret_key`
    2. `aws_access_key_id`
    3. `aws_secret_access_key`
6. To speed up ansible optionally set `pipelining = True` in
`/etc/ansible/ansible.cfg`.
7. Run `ansible-playbook deploy/ansible-deploy-production.yml`
8. Ssh to server and run certbot by letsencrypt.org