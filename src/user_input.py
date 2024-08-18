from src.api_hh import VacanciesHH


def search_vacancies():
    """Функция пользовательского ввода для поиска вакансий"""
    keyword = input("Введите ключевое слово для поиска вакансий: \n")
    quantity = int(input("Введите количество вакансий для поиска (не более 20): \n"))
    hh = VacanciesHH()
    vacancies = hh.get_vacancies(keyword, quantity)
    return vacancies


def search_top_salary(vacancies_top):
    """Функция для сортировки топа вакансий по зарплате"""
    num_top = int(
        input("Укажите количество вакансий, которые войдут в ТОП по зарплате: \n")
    )
    top_n_vacancy_list = []
    salary_list = []

    for vacancy in vacancies_top:
        salary_list.append(vacancy.get("payment_to"))

    set_top = set(salary_list)
    set_top.discard(None)
    sort_salary_list = sorted(set_top)

    for vacancy in vacancies_top:
        if vacancy["payment_to"] in sort_salary_list[-(num_top):]:
            top_n_vacancy_list.append(vacancy)

    return top_n_vacancy_list


if __name__ == "__main__":
    print(search_top_salary(vacancies_top=search_vacancies()))
