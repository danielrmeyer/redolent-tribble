***This Repository is for experimenting with flask, vagrant and virtualenv***

To get hello_world flask app up clone this repo and cd to the redolent-tribble directory.
```
vagrant up
```
When that is complete,
```
vagrant ssh

sudo /home/vagrant/flask_env/bin/python /vagrant/app/hello_world.py
```

In your local browser visit:
```
http://localhost:5050/
```

To practice developing open up your editor in the root directory.
With,
```
app.debug = True
```
in the hello_world.py app you can make modifications to the code in your
editor and see those changes come live automagically as the flask
server will detect changes to the code and automatically restart the server.
This allow one to do lots of experimentation quickly.
