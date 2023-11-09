class ObjectRegistry:
    pass


class BaseObject:
    pass


class Test(BaseObject):
    pass


class Exam(BaseObject):
   pass


class GraduationExam(Exam):
    pass


class TestTrial(BaseObject):
    pass


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
