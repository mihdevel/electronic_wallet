class Transaction():
  """Class transactions"""
  
  def send_money(self, from_id, to_id, count):
    self.max_money = 1000
    
    self.from_id = str(from_id)
    self.to_id = str(to_id)
    self.count = count
    result = self._check_count_money()
    if result:
      return print(result)
    
    user_from = self.read_in_db('db_users', self.from_id)
    user_to = self.read_in_db('db_users', self.to_id)

    user_from['money'] -= self.count
    user_to['money'] += self.count
    
    self.write_in_db('db_users', {self.from_id: user_from})
    self.write_in_db('db_users', {self.to_id: user_to})

    transactions = self.read_in_db('db_transactions', 'transactions')
    transactions = [] if transactions == 'KeyError' else transactions
    transactions.append({'from': self.from_id, 'to_id': self.to_id, 'count': self.count})
    self.write_in_db('db_transactions', {'transactions': transactions})
    
    return print('Удача! Чтобы проверить - используйте флаг -a')
  
  def _check_count_money(self):
    data_user_from = self.read_in_db('db_users', self.from_id)
    data_user_to = self.read_in_db('db_users', self.to_id)
    if data_user_from == 'KeyError' or data_user_to == 'KeyError':
      return 'В базе данных нету пользователей с такими ID'
    if data_user_from['money'] < self.count:
      return 'У пользователя с ID {} не достаточно колличество денег на счету. Операция отменена'.format(self.from_id)
    if data_user_to['money'] >= self.max_money:
      return 'У пользователя с ID {} имеется максимальное колличество денег на счету. Операция отменена'.format(self.to_id)
    else:
      return False