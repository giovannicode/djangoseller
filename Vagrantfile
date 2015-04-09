Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "vagrant_setup/playbook.yml"
  end
  config.vm.provision "shell", path: "vagrant_setup/shell_script.sh"

  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.synced_folder "./", "/home/vagrant/www/website"
end

