# -*- coding:utf-8 -*-


from project_09 import Book, Patron


class Library:

    book_list = []
    reader_list = []
    # def __init__(cls):
    #     cls.book_list = []
    #     cls.reader_list = []

    @classmethod
    def add_book(cls, title, author, reader=None):
        """添加一本书"""
        book = Book(title, author, reader)
        cls.book_list.append(book)
        
        print('书本 %s 添加成功！' % book)

    @classmethod
    def del_book(cls, title, author):
        """删除一本书"""

        target_book = None
        for book in cls.book_list:
            if book.title == title and book.author == author:
                target_book = book
                break
        
        if target_book:
            cls.book_list.remove(target_book)
            print('书本 %s 删除成功！' % title)
        else:
            print('书本 %s 不存在！' % title)

    @classmethod
    def find_book(cls, title, author=None):
        """根据书名查找一本书
        如果不存在则返回 -1，存在则返回 1"""
        titles = [b.title for b in cls.book_list]
        if title in titles:
            print('书本：%s 已找到!' % title)
            return 1
        else:
            print('书本：%s 找不到!' % title)
            return -1

    @classmethod
    def add_reader(cls, name):
        """添加一个读者"""
        reader = Patron(name)
        cls.reader_list.append(reader)

        print('读者 %s 添加成功！' % reader)

    @classmethod
    def del_reader(cls, name):
        """删除一个读者"""
        target_reader = None
        for reader in cls.reader_list:
            if reader.name == name:
                target_reader = reader
                break
        if target_reader:
            cls.reader_list.remove(target_reader)
            print('读者 %s 删除成功！' % target_reader)
        else:
            print('该读者不存在！')

    @classmethod
    def find_reader(cls, name):
        """根据读者名称查找一个读者
        如果找到则返回 1，找不到则返回 -1"""
        names = [r.name for r in cls.reader_list]
        
        if name in names:
            print('读者：%s 已找到!' % name)
            return 1
        else:
            print('读者：%s 找不到!' % name)
            return -1


if __name__ == '__main__':

    lib = Library()
    lib.add_book('python数据结构', '李军译', 'Cavin')
    lib.add_book('Spring实战第4版', 'MANNING', 'Cavin')
    lib.add_book('机器学习实战', 'Peter Harrington', 'Cavin')
    lib.find_book('机器学习实战')
    lib.del_book('Spring实战第4版', 'MANNING')
    print()
    lib.add_reader('柴剑波')
    lib.add_reader('Peter Harrington')
    lib.add_reader('John Smith')
    lib.add_reader('钟无艳')
    lib.find_reader('John Smith')
    lib.del_reader('钟无艳')
