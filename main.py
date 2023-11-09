class ObjectRegistry:
    def __init__(self):
        self.object_list = []

    def add_object(self, obj):
        self.object_list.append(obj)

    def view_list(self):
        for obj in self.object_list:
            obj.info()
            print("")


class BaseObject:
    def __init__(self, name, date):
        self._name = name
        self._date = date

    @property
    def info_name(self):
        return self._name

    @property
    def info_date(self):
        return self._date

    def info(self):
        print(f"Название:", self.info_name)
        print(f"Дата:", self.info_date)


class Test(BaseObject):
    def __init__(self, name, date, questions):
        super().__init__(name, date)
        self._questions = questions

    @property
    def info_questions(self):
        return self._questions

    def info(self):
        super().info()
        print("Тип: Тест")
        print("Вопросы:")
        for question in self.info_questions:
            print(f"- {question}")


class Exam(BaseObject):
    def __init__(self, name, date, subject):
        super().__init__(name, date)
        self._subject = subject

    @property
    def subject_info(self):
        return self._subject

    def info(self):
        super().info()
        print(f"Тип: Экзамен")
        print(f"Предмет:", self.subject_info)


class GraduationExam(Exam):
    def __init__(self, name, date, subject, required_score):
        super().__init__(name, date, subject)
        self._required_score = required_score

    @property
    def req_score_info(self):
        return self._required_score

    def info(self):
        super().info()
        print(f"Подтип: Выпускной экзамен")
        print(f"Проходной балл:", self.req_score_info)


class TestTrial(BaseObject):
    def __init__(self, name, date, subject, difficulty):
        super().__init__(name, date)
        self._subject = subject
        self._difficulty = difficulty

    @property
    def subject_info(self):
        return self._subject

    @property
    def difficulty_info(self):
        return self._difficulty

    def info(self):
        super().info()
        print(f"Тип: Испытание")
        print(f"Предмет:", self.subject_info)
        print(f"Сложность:", self.difficulty_info)


def int_input(inpt):
    if inpt.replace(" ", "").isdigit():
        return int(inpt)
    return None


def test_name_date_input():
        print("Введите название\n")
        testName = input("...")
        print("Введите дату в формате 'ДД ММ ГГГГ'\n")
        date = input("...").split()

        if all(item.isdigit() for item in date):
            return testName, ".".join(date)
        else:
            return None, None


def create_test(registry):
    testName, date = test_name_date_input()
    if testName != None and date != None:
        quests = []
        print("Введите количество вопросов\n")
        num_of_quests = int_input(input("..."))
        if num_of_quests > 0:
            for _ in range(num_of_quests):
                quest = input(f"Вопрос {_+1}: ")
                quests.append(quest)
            return registry.add_object(Test(testName, date, quests))
        else:
            return print("Неккоректный ввод\n")
    else:
        return print("Неккоректный ввод\n")


def create_exam(registry):
    testName, date = test_name_date_input()
    if testName != None and date != None:
        print("Напишите предмет\n")
        subject = input("...")
        registry.add_object(Exam(testName, date, subject))
    else:
        return print("Неккоректный ввод\n")


def create_graduation_exam(registry):
    testName, date = test_name_date_input()
    if testName != None and date != None:
        print("Напишите предмет\n")
        subject = input("...")
        print("Напишите проходной балл\n")
        req_score = int_input(input("..."))
        if req_score != None:
            registry.add_object(GraduationExam(testName, date, subject, req_score))
        else:
            return print("Неккоректный ввод\n")
    else:
        return print("Неккоректный ввод\n")


def create_test_trial(registry):
    testName, date = test_name_date_input()
    if testName != None and date != None:
        print("Напишите предмет\n")
        subject = input("...")
        print("Напишите cложность\n")
        difficulty = input("...")
        registry.add_object(TestTrial(testName, date, subject, difficulty))
    else:
        return print("Неккоректный ввод\n")


def main():
    pass


if __name__ == '__main__':
    main()
