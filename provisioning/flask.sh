echo "Provisioner is running ..."
sudo apt-get -y update
sudo apt-get -y install python3-pip
sudo apt-get -y install libpq-dev
sudo pip3 install -r /vagrant/requirements.txt
echo "Provisioner is done."
