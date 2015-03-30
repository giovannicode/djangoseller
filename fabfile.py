from fabric.api import local
from fabric.context_managers import lcd

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
    prepare_server()
    push()
    restart_gunicorn()


#css stuff
def movecss():
    with lcd('./main/static/css'):
        local('sass main.scss main.css')
        local('sass mango.scss mango.css')
    local('python manage.py collectstatic --noinput')
