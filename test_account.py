import pytest
from account import *


class Test:
    def setup_method(self):
        self.account1 = Account('Jacob')

    def teardown_method(self):
        del self.account1

    def test_init(self):
        assert self.account1.get_name() == 'Jacob'
        assert self.account1.get_balance() == 0

    def test_deposit(self):
        assert self.account1.deposit(10) is True
        assert self.account1.get_balance() == 10
        assert self.account1.deposit(-1) is False
        assert self.account1.deposit(0) is False

    def test_withdraw(self):
        self.account1.deposit(10)
        assert self.account1.withdraw(5) is True
        assert self.account1.get_balance() == 5
        assert self.account1.withdraw(-1) is False
        assert self.account1.withdraw(0) is False
        assert self.account1.withdraw(10) is False


if __name__ == '__main__':
    new_test = Test()
    new_test.setup_method()
    new_test.test_init()
    new_test.test_deposit()
    new_test.test_withdraw()
    new_test.teardown_method()
