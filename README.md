Deployment
==========

1. Install ansible on Development machine
2. Add server's SSH keys to Development machine's `~/.ssh`
3. Add server's domain/ip to ansible's `/etc/ansible/hosts` file
4. Add `ansible_user` variable to
`/etc/ansible/host_vars/DOMAIN_NAME.yml` (set DOMAIN_NAME to your
site's domain name)
5. Add `django_secret_key` variable to
`/etc/ansible/host_vars/DOMAIN_NAME.yml`,  optionally encrypt it with
ansible-vault, see
http://docs.ansible.com/ansible/latest/playbooks_vault.html
4. Run `ansible deploy/ansible-deploy-production.yml`