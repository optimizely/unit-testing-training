import unittest

import mock

import my_functions


# Run with: `python -m unittest discover` (or `nosetests`)

class MyFunctionsTest(unittest.TestCase):

  ################# add_three_to_value tests #################

  def test_add_three_to_value__with_seven(self):
    self.assertEqual(10, my_functions.add_three_to_value(7))

  def test_add_three_to_value__with_ten(self):
    self.assertEqual(13, my_functions.add_three_to_value(10))

  ################# get_my_number tests #################

  def test_get_my_number(self):
    mock_file = mock.Mock()

    mock_file.read.return_value = '8'

    with mock.patch('__builtin__.open', return_value=mock_file) as mock_open:
      self.assertEqual(8, my_functions.get_my_number())

    mock_open.assert_called_once_with('/test_number.txt', 'r')

    mock_file.read.assert_called_once_with()
    mock_file.close.assert_called_once_with()

  def test_get_my_number__whitespace_in_number(self):
    mock_file = mock.Mock()

    mock_file.read.return_value = '  8  0  '

    with mock.patch('__builtin__.open', return_value=mock_file) as mock_open:
      self.assertEqual(80, my_functions.get_my_number())

    mock_open.assert_called_once_with('/test_number.txt', 'r')

    mock_file.read.assert_called_once_with()
    mock_file.close.assert_called_once_with()

  def test_get_my_number__not_number(self):

    mock_file = mock.Mock()

    mock_file.read.return_value = 'abc'

    with self.assertRaises(my_functions.MyException) as cm:
      with mock.patch('__builtin__.open', return_value=mock_file) as mock_open:
        my_functions.get_my_number()

    self.assertEqual('give me a number, bro',
                     str(cm.exception))

    mock_open.assert_called_once_with('/test_number.txt', 'r')

    mock_file.read.assert_called_once_with()
    mock_file.close.assert_called_once_with()

  ################# multiply_my_number_by tests #################

  def test_multiply_my_number_by__with_seven(self):
    with mock.patch('my_functions.get_my_number', return_value=2) as mock_get_my_number:
      self.assertEqual(14, my_functions.multiply_my_number_by(7))

    mock_get_my_number.assert_called_once_with()


  def test_multiply_my_number_by__with_ten(self):
    with mock.patch('my_functions.get_my_number', return_value=2) as mock_get_my_number:
      self.assertEqual(20, my_functions.multiply_my_number_by(10))

    mock_get_my_number.assert_called_once_with()
