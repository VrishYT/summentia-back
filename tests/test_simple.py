import unittest
from falcon import HTTP_200
import hug
from context import index

class APITest(unittest.TestCase):
  def test_hello_get_call(self):
    response = hug.test.get(index, 'slides/hello')
    assert response.status == HTTP_200
    assert response.data is not None
    print(response.data)
    
if __name__ == '__main__':
  unittest.main()