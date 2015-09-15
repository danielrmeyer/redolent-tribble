***This Repository is for experimenting with flask, vagrant and virtualenv***

To get hello_world flask app up clone this repo and cd to the redolent-tribble directory.
```
vagrant up
```
When that is complete,
```
vagrant ssh flask

sudo python3 /vagrant/app.py
```

In your local browser visit:
```
http://localhost:5050/
```
Initially you will see an empty string in the browser.

To practice developing open up your editor in the root directory.
With,
```
app.debug = True
```
in the hello_world.py app you can make modifications to the code in your
editor and see those changes come live automagically as the flask
server will detect changes to the code and automatically restart the server.
This allow one to do lots of experimentation quickly.


To post things to the app install httpie on your dev machine:
```
pip install httpie
```

Now do some posts:

```
http --form POST http://localhost:5050/add title='foo' text='foobar'
```

To see what got added to the database visit the root page in your browser:
```
http://localhost:5050/

[(1, 'foo', 'foobar')]
```

As an exercise make the response proper json.
