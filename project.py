import pickle

class Project():

    def __init__(self, filename):
        self.__filename = filename
    
    def get_all_projects(self):
        file = open(self.__filename, "rb")
        project = pickle.load(file)
        projects = list(project.keys())
        file.close()
        return projects

    def make_project(self, name):
        file = open(self.__filename, "rb")
        project = pickle.load(file)
        project[name] = {}
        file.close()
        file = open(self.__filename, "wb")
        pickle.dump(project, file)
        file.close()

        
    def remove_project(self, name):
        file = open(self.__filename, "rb")
        project = pickle.load(file)
        file.close()
        file = open(self.__filename, "wb")
        del project[name]
        pickle.dump(project, file)
        file.close()

    def rename_project(self, old_name, name):
        file = open(self.__filename, "rb")
        project = pickle.load(file)
        file.close()
        file = open(self.__filename, "wb")
        project[name] = project.pop(old_name)
        pickle.dump(project, file)
        file.close()
