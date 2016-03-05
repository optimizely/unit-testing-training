class MyException(Exception):
  pass


def add_three_to_value(value):
  return value + 3


def get_my_number():
  number_file = open('/test_number.txt', 'r')
  file_contents = number_file.read()
  number_file.close()

  try:
    return int(file_contents.replace(' ', ''))
  except ValueError:
    raise MyException('give me a number, bro')


def multiply_my_number_by(multiplier):
  return multiplier * get_my_number()
