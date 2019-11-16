class User:

    username=''
    userType=''
    name=''

    def __init__(self,UserObject):
        self.userType=UserObject['userType'];
        self.username=UserObject['username'];
        self.name=UserObject['name'];

    def createUser(self):
        #sql("",self.userType,self.username,self.name)
        output = 'succesfully created new user'
        return output

    def getLessonDate():
        return -1
