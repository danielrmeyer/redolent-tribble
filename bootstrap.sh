echo "Provisioner is running ..."
sudo apt-get -y update
sudo apt-get -y install python3-pip
sudo apt-get install -y python3-virtualenv
sudo pip3 install virtualenv
source /home/vagrant/test/bin/activate
pip install -r /vagrant/requirements
echo "Provisioner is done."

