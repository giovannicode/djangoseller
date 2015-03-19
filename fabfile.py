from fabric.api import local

#def test():
#    local("python manage.py test")

def push():
    local("git push production master")

def deploy():
#    test()
    push()
