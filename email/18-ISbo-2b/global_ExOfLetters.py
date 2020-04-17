# coding=utf-8
import global_User as User
import global_Letter as Letter

def create_letters():
    letters = []
    student = User.User("Максим Расторгуев", "18-ИСбо-2", "rastorguev10@gmail.com", True)
    body = "Доброго времени суток, Юрий Викторович!\n"
    "Отправляю вам ссылку на репозиторий с выполненной 1-ой лабораторной:\n"
    "https://github.com/Progoger/TasksForStudents/tree/master/18-ИСбо-2/ЛР01\n"
    "С Уважением,\n"
    "Расторгуев Максим, студент группы 18-ИСбо-2б"
    letter = Letter.Letter(student, "ТРПО ЛР01", body, 1, 1)
    letters.append(letter)

    student = User.User("Валерий Бублин", "18-ИСбо-2", "valerabubla44@gmail.com", True)
    body = "Доброго времени суток, Юрий Викторович!\n"
    "Отправляю вам ссылку на репозиторий с выполненной 1-ой лабораторной:\n"
    "https://github.com/Progoger/TasksForStudents/tree/master/18-ИСбо-2/ЛР01\n"
    "С Уважением,\n"
    "Валерий Бублин, студент группы 18-ИСбо-2б"
    letter = Letter.Letter(student, "ТРПО ЛР02", body, 1, 1)
    letters.append(letter)

    student = User.User("Софья Безбрежанова", "18-ИСбо-2", "sofiebezcoast@gmail.com", False)
    body = "Доброго времени суток, Юрий Викторович!\n"
    "Отправляю вам ссылку на репозиторий с выполненной 1-ой лабораторной:\n"
    "https://github.com/Progoger/TasksForStudents/tree/master/18-ИСбо-2/ЛР01\n"
    "С Уважением,\n"
    "Софья Безбрежанова, студент группы 18-ИСбо-2б"
    letter = Letter.Letter(student, "ТРПО ЛР01", body, 1, 1)
    letters.append(letter)

    student = User.User("Григорий Васверидзе", "18-ИСбо-2", "grishaakvasya@gmail.com", False)
    body = "Доброго времени суток, Юрий Викторович!\n"
    "Отправляю вам ссылку на репозиторий с выполненной 1-ой лабораторной:\n"
    "https://github.com/Progoger/TasksForStudents/tree/master/18-ИСбо-2/ЛР01\n"
    "С Уважением,\n"
    "Григорий Васверидзе, студент группы 18-ИСбо-2б"
    letter = Letter.Letter(student, "ТРПО ЛР01", body, 1, 1)
    letters.append(letter)

    student = User.User("Сантьяго Цеместес", "18-ИСбо-2", "santozemesjago@gmail.com", True)
    body = "Доброго времени суток, Юрий Викторович!\n"
    "Отправляю вам ссылку на репозиторий с выполненной 2-ой лабораторной:\n"
    "https://github.com/Progoger/TasksForStudents/tree/master/18-ИСбо-2/ЛР02\n"
    "С Уважением,\n"
    "Сантьяго Цеместес, студент группы 18-ИСбо-2б"
    letter = Letter.Letter(student, "ТРПО ЛР01", body, 1, 1)
    letters.append(letter)

    student = User.User("Сантьяго Цеместес", "18-ИСбо-2", "santozemesjago@gmail.com", True)
    body = "Доброго времени суток, Юрий Викторович!\n"
    "Отправляю вам ссылку на репозиторий с выполненной 2-ой лабораторной:\n"
    "https://github.com/Progoger/TasksForStudents/tree/master/18-ИСбо-2/ЛР02\n"
    "С Уважением,\n"
    "Сантьяго Цеместес, студент группы 18-ИСбо-2б"
    letter = Letter.Letter(student, "ТРПО ЛР02", body, 2, 2)
    letters.append(letter)

    student = User.User("Борис Кипарис", "18-ИСбо-2", "kiparisforboris@gmail.com", True)
    body = "Хаюшки, мистер ЮрВикт!\n"
    "Отправляю вам ссылку на репозиторий с выполненной 2-ой лабораторной:\n"
    "https://github.com/Progoger/TasksForStudents/tree/master/18-ИСбо-2/ЛР01\n"
    "С Уважением,\n"
    "Борис Кипарис, студент группы 18-ИСбо-2б"
    letter = Letter.Letter(student, "ТРПО ЛР02", body, 2, 2)
    letters.append(letter)

    student = User.User("Сантьяго Цеместес", "18-ИСбо-2", "santozemesjago@gmail.com", True)
    body = "Доброго времени суток, Юрий Викторович!\n"
    "Отправляю вам ссылку на репозиторий с выполненной 2-ой лабораторной:\n"
    "А нет, не отправляю\n"
    "С Уважением,\n"
    "Сантьяго Цеместес, студент группы 18-ИСбо-2б"
    letter = Letter.Letter(student, "ТРПО ЛР02", body, 2, 2)
    letters.append(letter)

    student = User.User("Санто Цеметретос", "18-ИСбо-2", "santozement322@gmail.com", True)
    body = "Доброго времени суток, Юрий Викторович!\n"
    "Отправляю вам ссылку на репозиторий с выполненной 2-ой лабораторной:\n"
    "https://github.com/Progoger/TasksForStudents/tree/master/18-ИСбо-2/ЛР02\n"
    "С Уважением,\n"
    "Здесь пригодилась бы подпись"
    letter = Letter.Letter(student, "ТРПО ЛР02", body, 2, 2)
    letters.append(letter)

    student = User.User("Максим Расторгуев", "18-ИСбо-2", "rastorguev10@gmail.com", True)
    body = "Доброго времени суток, Юрий Викторович!\n"
    "Отправляю вам ссылку на репозиторий с выполненной 1-ой лабораторной:\n"
    "https://github.com/Progoger/TasksForStudents/tree/master/18-ИСбо-2\n"
    "С Уважением,\n"
    "Расторгуев Максим, студент группы 18-ИСбо-2б"
    letter = Letter.Letter(student, "ТРПО ЛР01", body, 1, 1)
    letters.append(letter)

    return letters