from datetime import date
import calendar


DIGITS = {
    "0": [" *** ", "*   *", "*   *", "*   *", " *** "],
    "1": ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
    "2": [" *** ", "*   *", "   * ", "  *  ", "*****"],
    "3": ["**** ", "    *", " *** ", "    *", "**** "],
    "4": ["*  * ", "*  * ", "*****", "   * ", "   * "],
    "5": ["*****", "*    ", "**** ", "    *", "**** "],
    "6": [" *** ", "*    ", "**** ", "*   *", " *** "],
    "7": ["*****", "   * ", "  *  ", " *   ", "*    "],
    "8": [" *** ", "*   *", " *** ", "*   *", " *** "],
    "9": [" *** ", "*   *", " ****", "    *", " *** "],
    " ": ["   ", "   ", "   ", "   ", "   "],
}

WEEKDAYS = [
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье",
]


def get_birth_date():
    """Запрашивает дату рождения и проверяет корректность введённой даты."""
    while True:
        try:
            day = int(input("Введите день рождения: "))
            month = int(input("Введите месяц рождения: "))
            year = int(input("Введите год рождения: "))

            birth_date = date(year, month, day)

            if birth_date > date.today():
                print("Дата рождения не может быть в будущем. Попробуйте ещё раз.\n")
                continue

            return birth_date
        except ValueError:
            print("Введена некорректная дата. Попробуйте ещё раз.\n")


def get_weekday(birth_date):
    """Возвращает название дня недели для указанной даты."""
    return WEEKDAYS[birth_date.weekday()]


def is_leap_year(year):
    """Определяет, является ли год високосным."""
    return calendar.isleap(year)


def calculate_age(birth_date):
    """Вычисляет полный возраст пользователя на текущую дату."""
    today = date.today()
    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age


def print_star_date(birth_date):
    """Печатает дату рождения цифрами, составленными из звёздочек."""
    date_string = birth_date.strftime("%d %m %Y")
    print("\nДата рождения в формате электронного табло:\n")

    for row in range(5):
        line = "  ".join(DIGITS[symbol][row] for symbol in date_string)
        print(line)


def main():
    print("Программа работы с датой рождения")
    print("-" * 36)

    birth_date = get_birth_date()
    print(f"\nДень недели: {get_weekday(birth_date)}")

    if is_leap_year(birth_date.year):
        print(f"{birth_date.year} год был високосным.")
    else:
        print(f"{birth_date.year} год не был високосным.")

    print(f"Возраст пользователя: {calculate_age(birth_date)}")
    print_star_date(birth_date)


if __name__ == "__main__":
    main()
