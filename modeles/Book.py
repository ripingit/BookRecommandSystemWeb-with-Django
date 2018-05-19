class Book(object):
    def __init__(self,ISBN='',
                 bookName='',
                 bookUrl='',
                 author='',
                 content='',
                 publishYear='',
                 bookIndex='',
                 publisher='',
                 catalog='',
                 systemNumber='',
                 douBanId='',
                 doubanRating=0,
                 doubanRatingPerson=0,
                 seriesTitle='',
                 doubanSummary='',
                 ratingGraphic=[]):
        # ratingGraphic：一个数组，里面每个元素都是一个列表，[id,true]，类似这样的，表示id为x的五角星是否填充满
        self.ISBN = ISBN
        self.bookName = bookName
        self.bookUrl = bookUrl
        self.author = author
        self.content = content
        self.publishYear = publishYear
        self.bookIndex = bookIndex
        self.publisher = publisher
        self.catalog = catalog
        self.systemNumber = systemNumber
        self.douBanId = douBanId
        self.doubanRating = doubanRating
        self.doubanRatingPerson = doubanRatingPerson
        self.seriesTitle = seriesTitle
        self.doubanSummary = doubanSummary
        self.ratingGraph = ratingGraphic
    def getRatingGraphic(self):
        return self.ratingGraph