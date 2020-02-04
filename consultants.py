class consultant:
    "consultant class"
    def __init__(self,name="",skill="",exp=0):
        self.__name = name
        self.__skill = skill
        self.__exp = exp
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def setSkill(self,skill):
        self.__skill=skill
    def getSkill(self):
        return self.__skill
    def setExp(self,exp):
        self.__exp=exp
    def getExp(self):
        return self.__exp
    def __str__(self):
        return self.__name+" "+str(self.__skill)+" "+str(self.__exp)
    def find(self):
        if self.__skill=="java" or self.__skill=="python":
            if self.__exp>=5 and self.__exp<10:
                print(self.__name," Your wage is 12000")
            else:
                print("sorry you have less experience")
        elif self.__skill=="python" or self.__skill=="ai":
            if self.__exp>=3 and self.__exp<8:
                print(self.__name," Your wage is 7000")
            else:
                print("sorry you have less experience")
        elif self.__skill=="java" or self.__skill=="c" or self.__skill=="c++" or self.__skill=="python":
            if self.__exp >= 4 and self.__exp < 10:
                print(self.__name," Your wage is 5000")
            else:
                print("sorry you have less experience")
one=consultant("Kaushal","java",9)
one.find()
two=consultant("Alan","c",5)
two.find()
three=consultant("Turing","ai",5)
three.find()
four=consultant("Bob","c++",10)
four.find()
