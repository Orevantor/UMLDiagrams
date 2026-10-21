import pickle
import project
import diagram

def main():
    
    FILENAME = "projects.dat"
    QUIT = False

    OPEN = "1"
    GET_ALL = "2"
    MAKE = "3"
    REMOVE = "4"
    RENAME = "5"
    EXIT = "6"

    projects = project.Project(FILENAME)

    #Создать файл, в случае его отсутсвия
    try:
        file = open(FILENAME, "rb")
        file.close()
    except FileNotFoundError:
        file = open(FILENAME, "wb")
        pickle.dump({}, file)
        file.close()

    while QUIT != True:
        
        choice = str(input(
            "Открыть проект - 1\n" \
            "Просмотреть все проекты - 2\n" \
            "Создать проект - 3\n" \
            "Удалить проект - 4\n" \
            "Переименовать проект - 5\n" \
            "Выйти из программы - 6\n" \
        ))

        if choice == OPEN:
            project_file = input("Введите имя проекта: ")
            diagrams = diagram.Diagram(FILENAME, project_file)

            QUIT2 = False

            while QUIT2 != True:

                choice = str(input(
                "Открыть диаграмму - 1\n" \
                "Просмотреть все диаграммы - 2\n" \
                "Создать диаграмму - 3\n" \
                "Удалить диаграмму - 4\n" \
                "Изменить диаграмму - 5\n" \
                "Выйти из проекта - 6\n"))

                if choice == OPEN:
                    name = input("Введите имя диаграммы: ")
                    print(diagrams.get_diagram(name))

                elif choice == GET_ALL:
                    print(diagrams.get_all_diagram())
                
                elif choice == MAKE:
                    name = input("Введите имя диаграммы: ")
                    attribute = input("Введите аттрибуты данных: ")
                    methods = input("Введите методы: ")
                    diagrams.make_diagram(name, attribute, methods)

                elif choice == REMOVE:
                    name = input("Введите имя диаграммы: ")
                    diagrams.remove_diagram(name)

                elif choice == RENAME:
                    old_name = input("Введите имя диаграммы: ")
                    name = input("Введите новое имя диаграммы: ")
                    attribute = input("Введите новые аттрибуты данных: ")
                    methods = input("Введите новые методы: ")
                    diagrams.change_diagram(old_name, name, attribute, methods)

                elif choice == EXIT:
                    QUIT2 = True
                    
        elif choice == GET_ALL:
            print(projects.get_all_projects())

        elif choice == MAKE:
            name = input("Введите имя проекта: ")
            projects.make_project(name)

        elif choice == REMOVE:
            name = input("Введите имя проекта: ")
            projects.remove_project(name)

        elif choice == RENAME:
            old_name = input("Введите имя проекта: ")
            name = input("Введите новое имя проекта: ")
            projects.rename_project(old_name, name)

        elif choice == EXIT:
            QUIT = True


if __name__ == "__main__":
    main()


