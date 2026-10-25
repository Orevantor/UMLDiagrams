class Make_diagram():
    def __init__(self, name, attribute, methods):
        self.__name = name
        self.__attribute = attribute
        self.__methods = methods

    def split_words(self):
        self.__attribute = self.__attribute.split()
        self.__methods = self.__methods.split()
        
    def make_diagram(self):
        self.split_words()
        bufer = ""
        max = 0

        for word in self.__attribute:
            if len(word) > max:
                max = len(word)
        for word in self.__name:
            if len(word) > max:
                max = len(word) 
        for word in self.__methods:
            if len(word) > max:
                max = len(word) 

        bufer += "+" + "-" * max + "+" + "\n"
        space = max - len(self.__name)
        bufer += "|" + self.__name + space * " " + "|" + "\n"
        bufer += "+" + "-" * max + "+" + "\n"
        for word in self.__attribute:
           space = max - len(word)
           bufer += "|" + word + space * " " + "|" + "\n"
        bufer += "+" + "-" * max + "+" + "\n"
        for word in self.__methods:
           space = max - len(word)
           bufer += "|" + word + space * " " + "|" + "\n"
        bufer += "+" + "-" * max + "+" + "\n"
       
        return bufer
