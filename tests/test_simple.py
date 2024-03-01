import unittest
from falcon import HTTP_200
import hug
from context import index

self_api = hug.API(__name__)

class APITest(unittest.TestCase):
  def test_hello_get_call(self):
    response = hug.test.get(index, 'slides/hello')
    assert response.status == HTTP_200
    assert response.data is not None
    print(response.data)
    
  def test_exception_handling(self):
    """Test to ensure built in exception types errors are handled as expected"""
    def raise_error(value):
        raise KeyError('Invalid value')

    @hug.get()
    def test_error(data: raise_error):
        return True

    response = hug.test.get(self_api, 'test_error', data=1)
    assert 'errors' in response.data
    assert response.data['errors']['data'] == 'Invalid value'
    
if __name__ == '__main__':
  unittest.main()