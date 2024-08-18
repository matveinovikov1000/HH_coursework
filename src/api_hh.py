from abc import ABC, abstractmethod

import requests


class Parser(ABC):
    """Класс для работы с API HeadHunter"""

    @abstractmethod
    def get_vacancies(self, keyword, quantity):
        """Метод для получения вакансий с API HeadHunter"""
        pass


class VacanciesHH(Parser):
    """Класс для работы с API HeadHunter"""

    def get_vacancies(self, keyword, quantity):
        """Метод для получения вакансий с API HeadHunter"""
        url_hh = "https://api.hh.ru/vacancies"
        vacancies_hh = requests.get(
            url_hh, params={"text": keyword, "currency": "RUR", "host": "hh.ru"}
        ).json()
        vacancies_hh_list = []
        for i in range(0, quantity):
            try:
                vacancy = {
                    "name": vacancies_hh["items"][i]["name"],
                    "payment_from": vacancies_hh["items"][i]["salary"]["from"],
                    "payment_to": vacancies_hh["items"][i]["salary"]["to"],
                    "town": vacancies_hh["items"][i]["area"]["name"],
                    "requirement": vacancies_hh["items"][i]["snippet"]["requirement"],
                }
            except TypeError:
                vacancy = {
                    "name": vacancies_hh["items"][i]["name"],
                    "payment_to": 0,
                    "payment_from": 0,
                    "town": vacancies_hh["items"][i]["area"]["name"],
                    "requirement": vacancies_hh["items"][i]["snippet"]["requirement"],
                }
            vacancies_hh_list.append(vacancy)
        return vacancies_hh_list


if __name__ == "__main__":
    hh = VacanciesHH()
    print(hh.get_vacancies("Бухгалтер", 20))
