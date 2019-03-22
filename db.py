import shelve
import unittest

class DB:
  """Class for job with DB"""

  def write_in_db(self, db, data):
    db_use = shelve.open(db)
    for key in data:
      db_use[str(key)] = data[key]
    db_use.close()
  
  def read_in_db(self, db, key=None):
    db_use = shelve.open(db)

    if key == None:
      return db_use.keys()
    
    try:
      data = db_use[str(key)]
    except KeyError:
      data = 'KeyError'
    db_use.close()
    return data


class TestDB(unittest.TestCase):
  def setUp(self):
    self.db = DB()
  
  def test_read_in_db(self):
    self.assertEqual(self.db.read_in_db('db_users', 'a'), 'KeyError')