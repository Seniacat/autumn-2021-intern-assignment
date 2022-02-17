class ErrorResponse:
    """Класс для описания ошибок, возникающих при работе приложения"""

    INCORRECT_SUM = "Введите корректную сумму"
    INCORRECT_OPERATION = "Введите операцию из допустимого списка"
    ID_REQUIRED = "Требуется ввести ID пользователя"
    INCORRECT_ID = "Требуется ввести корректное значение ID"
    INCORRECT_TRANSFER_DATA = "Получатель и отправитель совпадают, проверьте вводимые данные"
    NOT_ENOUGH_FUNDS = 'Недостаточно средств на счете'
    NO_BANK_ACCOUNT = "У данного пользователя нет денежного счета"
    NO_TRANSACTIONS = "История операций пуста"
    USER_DOES_NOT_EXIST = "Такого пользователя не существует, проверьте вводимые данные"


class UserDoesNotExist(Exception):
    """Исключение, вызываемое при отсутствии в БД
    записей о пользователе с указанным ID"""

    pass


class BalanceDoesNotExist(Exception):
    """Исключение, вызываемое при отсутствии в БД
    записей о балансе пользователя с указанным ID"""

    def __str__(self):
        return f"USER DOES NOT HAVE A BANK ACCOUNT"
