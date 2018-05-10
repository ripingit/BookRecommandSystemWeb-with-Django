class BorrowBook(object):
    def __init__(self,name='',author='',publishYear='',branchLibray='',index='',inputKey='',
                 repayYear='',remainingDay=''):
        self.name = name
        self.author = author
        self.publishYear = publishYear
        self.repayYear = repayYear
        self.branchLibrary = branchLibray
        self.index = index
        self.inputKey = inputKey
        self.remainingDay = remainingDay
    def __str__(self):
        return 'name[{name},{author},{publishYear},{repayYear}' \
               ',{branchLibary},{index},{inputKey},{remainingDay}]' \
               ''.format(name=self.name,author=self.author,publishYear=self.publishYear,
                         repayYear=self.repayYear,branchLibary=self.branchLibrary,
                         index=self.index,inputKey=self.inputKey,remainingDay=self.remainingDay)
