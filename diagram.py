import pickle
import make_diagram

class Diagram():
    def __init__(self, filename, project_file):
        self.__project_file = project_file
        self.__filename = filename

    def get_diagram(self, name):
        file = open(self.__filename, "rb")
        data = pickle.load(file)
        file.close
        diagram = data[self.__project_file][name]
        return diagram

    def get_all_diagram(self):
        file = open(self.__filename, "rb")
        diagrams = pickle.load(file)
        file.close()
        return list(diagrams[self.__project_file].keys())

    def make_diagram(self, name, attribute, methods):
        file = open(self.__filename, "rb")
        data = pickle.load(file)
        file.close()
        diagram = make_diagram.Make_diagram(name, attribute, methods)      
        data[self.__project_file][name] = diagram.make_diagram()
        file = open(self.__filename, "wb")
        pickle.dump(data, file)
        file.close()

    def change_diagram(self, old_name, name, attribute, methods):
        self.remove_diagram(old_name)
        self.make_diagram(name, attribute, methods)

    def remove_diagram(self, name):
        file = open(self.__filename, "rb")
        data = pickle.load(file)
        file.close()
        del data[self.__project_file][name]
        file = open(self.__filename, "wb")
        pickle.dump(data, file)
        file.close()
