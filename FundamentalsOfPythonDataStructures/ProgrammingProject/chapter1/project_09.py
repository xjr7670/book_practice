# -*- coding:utf-8 -*-


class Book:

    def __init__(self, title, author, reader):
        self.title = title
        self.author = author
        self.reader = reader
        self.waiting_list = []

    def __str__(self):
        return '书名：%s，作者：%s' % (self.title, self.author)


class Patron:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '读者名称：%s' % self.name


if __name__ == "__main__":
    
    print('测试开始...')
    print('创建一本书：')
    book = Book('python从入门到精通', '作者是我', '没人借')
    print('成功创建了一本书：%s\n', book)

    print('创建一名读者：')
    reader = Patron('李大功')
    print('成功创建了一名读者：%s\n', reader)
    