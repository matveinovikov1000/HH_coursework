from abc import ABC, abstractmethod


class ActionsWithFile(ABC):
    """Класс для добавления вакансий в файл, чтения данных из файла, удаления данных из файла"""
    @abstractmethod
    def add_data(self):
        """Метод для добавления данных в файл"""
        pass

    @abstractmethod
    def get_data(self):
        """Метод для получения данных из файла"""
        pass

    @abstractmethod
    def delete_data(self):
        """Метод для удаления данных из файла"""
        pass
