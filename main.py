from src.actions_vacancies import ActionsWithFile
from src.user_input import search_top_salary, search_vacancies


def user_interaction():
    """Функция для взаимодействия с пользователем"""
    user_input_one = input(
        "Необходимо ли получить ТОП вакансий по сумме зарплаты? (Да/Нет) \n"
    ).lower()

    if user_input_one == "нет":
        data_vacancies = search_vacancies()
    elif user_input_one == "да":
        data_vacancies = search_top_salary(vacancies_top=search_vacancies())

    user_input_two = int(
        input(
            "Укажите цифру, соответствующую необходимому действию:\n 1 - сохранить вакансии в файл;"
            "\n 2 - показать вакансии из файла;"
            "\n 3 - удалить вакансии из файла\n"
        )
    )

    if user_input_two == 1:
        awf = ActionsWithFile("data/vacancies.json")
        awf.add_data(data_vacancies)
    elif user_input_two == 2:
        awf = ActionsWithFile("data/vacancies.json")
        awf.get_data()
    elif user_input_two == 3:
        awf = ActionsWithFile("data/vacancies.json")
        awf.delete_data()


if __name__ == "__main__":
    print(user_interaction())
