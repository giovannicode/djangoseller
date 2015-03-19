from fabric.api import local

#def test():
#    local("python manage.py test")

def prepare_server():
    local("ansible-playbook -u root ansible/playbook.yml")

def push():
    local("git push production master")

def restart_gunicorn():
    local("ansible-playbook -u root ansible/playbook2.yml")

def deploy():
#    test()
    prepare_server():
    push()
    restart_gunicorn():
