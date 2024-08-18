import json
from abc import ABC, abstractmethod


class ActionsWithFileABC(ABC):
    """Класс для добавления вакансий в файл, чтения данных из файла, удаления данных из файла"""

    @abstractmethod
    def add_data(self, vacancies_data):
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


class ActionsWithFile(ActionsWithFileABC):
    """Класс для добавления вакансий в файл, чтения данных из файла, удаления данных из файла"""

    def __init__(self, filename="data/vacancies.json"):
        self.filename = filename

    def add_data(self, vacancies_data):
        """Метод для добавления данных в файл"""
        with open(self.filename, "a", encoding="utf8") as file:
            json.dump(vacancies_data, file, ensure_ascii=False)

    def get_data(self):
        """Метод для получения данных из файла"""
        with open(self.filename, encoding="utf8") as file:
            data = json.load(file)
            print(data)

    def delete_data(self):
        """Метод для удаления данных из файла"""
        with open(self.filename, "w") as file:
            json.dump(None, file)
