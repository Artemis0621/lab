class Account:
    """
    Class representing details for an account object
    """
    def __init__(self, name: str) -> None:
        """
        Constructor to create initial state of an account object.
        :param name: Account's name.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Method to deposit money into account.
        :param amount: Amount of money to deposit.
        :return: Success value of deposit operation.
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Method to withdraw money from account.
        :param amount: Amount of money to withdraw.
        :return: Success value of withdraw operation.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Method to access an account's balance.
        :return: Account's current balance.
        """
        return float(self.__account_balance)

    def get_name(self) -> str:
        """
        Method to access an account's name.
        :return: Account's name.
        """
        return self.__account_name
