import os
import flaskr
import unittest
import tempfile
import flask

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)  # close file descriptor (for low level IO)
        os.unlink(flaskr.app.config['DATABASE'])  # Remove a file

    # Notice that our test functions begin with the word test; this allows unittest to automatically identify the method as a test to run.
    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password,
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('admin', 'default')
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login('adminx', 'default')
        assert 'Invalid username' in rv.data
        rv = self.login('admin', 'defaultx')
        assert 'Invalid password' in rv.data

    def test_messages(self):
        rv = self.login('admin', 'default')
        assert 'You were logged in' in rv.data
        rv = self.app.post('/add', data=dict(
            title='<Hello>',
            text='<strong>HTML</strong> allowed here'
        ), follow_redirects=True)
        assert 'No entries so far' not in rv.data
        assert '&lt;Hello&gt;' in rv.data
        assert '<strong>HTML</strong> allowed here' in rv.data

# Besides using the test client as shown above, there is also the test_request_context() method that can be used in combination with the with statement to activate a request context temporarily. With this you can access the request, g and session objects like in view functions. Here is a full example that demonstrates this approach:

app = flask.Flask(__name__)

with app.test_request_context('/?name=Peter'):
    # Note however that if you are using a test request context, the before_request() functions are not automatically called same for after_request() functions. However teardown_request() functions are indeed executed when the test request context leaves the with block. If you do want the before_request() functions to be called as well, you need to call preprocess_request() yourself:
    app.preprocess_request()

    print '\n'*10, "Context TEST", '\n'*10
    assert flask.request.path == '/'
    assert flask.request.args['name'] == 'Peter'


if __name__ == '__main__':
    unittest.main()
