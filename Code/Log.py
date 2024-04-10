
class Log:
    def __init__(self):
        self.log = True
    def Info(self,info):
        print(f'{info}')


log = None
if log == None:
    log = Log()