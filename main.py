import sys
import shelve
from optparse import OptionParser

from person import Person


class Main(Person):
    """Main class for communications with user"""
    
    def __init__(self):
        # Получение аргументов коммандной строки
        parser_opt = OptionParser()
        parser_opt.add_option('-c', '--create-user',
                              dest='create_user_no_interactive',
                              help='Создать пользователя: --name=[NAME] --money=[MONEY]',
                              action='store_true')

        parser_opt.add_option('-a', '--all-users',
                              dest='get_users_no_interactive',
                              help='Получить данные всех пользователей',
                              action='store_true')

        parser_opt.add_option('-s', '--send-money',
                              dest='send_money_no_interactive',
                              help='Отправить деньги пользователю --from-id=[FROM_ID] --to-id=[TO_ID] --money=[MONEY]',
                              action='store_true')

        parser_opt.add_option('-n', '--name',
                              dest='name',
                              help='Имя: --name [NAME]',
                              action="store",
                              type = "string")

        parser_opt.add_option('-m', '--money',
                              dest='money',
                              help='Колличество денег (float)',
                              action="store",
                              type = "float")

        parser_opt.add_option('-f', '--from-id',
                              dest='from_id',
                              help='ID пользователя',
                              type = "int")

        parser_opt.add_option('-t', '--to-id',
                              dest='to_id',
                              help='ID пользователя',
                              type = "int")
        (self.options, args) = parser_opt.parse_args()
        
        if self.options.create_user_no_interactive:
            name = self.options.name
            money = self.options.money
            result = self.create_user(name, money)
            print(result)
            sys.exit(0)

        if self.options.get_users_no_interactive:
            db_use = shelve.open('db_users')
            for key in db_use:
                if key == 'last_id': continue
                print(dict(id=key ,data=db_use[key]))
            sys.exit(0)

        if self.options.send_money_no_interactive:
            from_id = self.options.from_id
            to_id = self.options.to_id
            count = self.options.money
            self.send_money(from_id, to_id, count)
            sys.exit(0)
    
if __name__ == '__main__':
    Main()