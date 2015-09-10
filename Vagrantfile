# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrant.configure(2) do |config|
#   config.vm.box = "ubuntu/trusty64"
#   config.vm.network :forwarded_port, guest: 80, host: 5050
#   config.vm.provision :shell, path: "bootstrap.sh"
# end
Vagrant.configure("2") do |config|
  config.vm.define "postgres" do |postgres|
    postgres.vm.box = "ubuntu/trusty64"
    postgres.vm.host_name = "postgresql"
    postgres.vm.provision :shell, :path => "provisioning/postgres.sh"
    postgres.vm.provider :virtualbox do |v|
        postgres.vm.network "private_network", ip: "10.0.0.10"
        postgres.vm.network "forwarded_port", guest: 5432, host: 15432
        v.name = "postgresql"
    end
    postgres.vm.provider :aws do |aws, override|
        aws.access_key_id = ENV['AWS_KEY']
        aws.secret_access_key = ENV['AWS_SECRET']
        aws.keypair_name = ENV['AWS_KEYNAME']
        aws.ami = "ami-af868e9f"
        aws.region = "us-west-2"
        aws.instance_type = "t2.medium"
        aws.security_groups = ["db_vagrant"]
        override.vm.box = "dummy"
        override.ssh.username = "ubuntu"
        override.ssh.private_key_path = ENV['AWS_KEYPATH']
    end
  end
  config.vm.define "flask" do |flask|
    flask.vm.box = "ubuntu/trusty64"
    flask.vm.host_name = "flask"
    flask.vm.provision :shell, :path => 'provisioning/flask.sh'
    flask.vm.provider :virtualbox do |v|
        flask.vm.network "private_network", ip: "10.0.0.11"
        flask.vm.network "forwarded_port", guest: 80, host: 5050
        v.name = "flaskapp"
    end
    flask.vm.provider :aws do |aws, override|
        aws.access_key_id = ENV['AWS_KEY']
        aws.secret_access_key = ENV['AWS_SECRET']
        aws.keypair_name = ENV['AWS_KEYNAME']
        aws.ami = "ami-af868e9f"
        aws.region = "us-west-2"
        aws.instance_type = "t2.micro"
        aws.security_groups = ["webapp_vagrant"]
        override.vm.box = "dummy"
        override.ssh.username = "ubuntu"
        override.ssh.private_key_path = ENV['AWS_KEYPATH']
    end
  end
end
