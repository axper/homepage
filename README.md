Deployment
==========

0. Install ansible
1. Add server's SSH keys to your `~/.ssh`
2. Add server's domain/ip to ansible's `/etc/ansible/hosts` file
3. Add `django_secret_key` and `ansible_user` variables to
`/etc/ansible/host_vars/DOMAIN_NAME.yml` (set DOMAIN_NAME to your site's domain name)
4. Run `ansible deploy/ansible-deploy.yml`