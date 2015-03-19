from fabric.api import local

#def test():
#    local("python manage.py test")

def prepare_server():
    local("ansible-playbook -u root ansible/playbook.yml")

def push():
    local("git push production master")

def deploy():
#    test()
    prepare_server():
    push()
