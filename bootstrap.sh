echo "Provisioner is running ..."
sudo apt-get -y update
sudo apt-get -y install python3-pip
sudo pip3 install virtualenv
virtualenv /home/vagrant/flask_env
source /home/vagrant/flask_env/bin/activate
pip install -r /vagrant/requirements.txt
echo "Provisioner is done."

