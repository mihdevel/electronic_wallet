import unittest

from transaction import Transaction
from db import DB


class Person(Transaction, DB):
  """Class for job with users"""
  
  def create_user(self, name, money=0.0):
    self.id = self._gen_id()
    self.name = name
    self.money = float(money)
    self.write_in_db('db_users', {self.id: dict(name=self.name, money=self.money)})
    return 'Пользователь создан\nID: {} \nName: {} \nДенег: {}'.format(self.id, self.name, self.money)
  
  def _gen_id(self):
    last_id = self.read_in_db('db_users', 'last_id')
    id = 0 if last_id == 'KeyError' else last_id
    id += 1
    self.write_in_db('db_users', {'last_id': id})
    
    return str(id)


class TestPerson(unittest.TestCase):
  def setUp(self):
    self.user = Person()
    self.user.create_user('Bob')

  def test_name(self):
    self.assertEqual(self.user.name, 'Bob')
    
  def test_money(self):
    self.assertEqual(self.user.money, 0.0)