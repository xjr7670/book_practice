# -*- coding:utf-8 -*-


class Paginater:
    def __init__(self, url_address, cur_page_num, total_rows, one_page_lines=10, page_maxtag=9):
        self.url_address = url_address
        self.page_maxtag = page_maxtag
        total_page, remainder = divmod(total_rows, one_page_lines)
        if remainder:
            total_page += 1
        self.total_page = total_page
        try:
            cur_page_num = int(cur_page_num)
            if cur_page_num > total_page:
                cur_page_num = total_page
            if cur_page_num == 0:
                cur_page_num = 1
        except Exception as e:
            cur_page_num = 1

        self.cur_page_num = cur_page_num
        self.rows_start = (cur_page_num-1) * one_page_lines
        self.rows_end = cur_page_num * one_page_lines

        if total_page < page_maxtag:
            page_maxtag = total_page

        half_page_maxtag = page_maxtag // 2
        page_start = cur_page_num - half_page_maxtag
        page_end = cur_page_num + half_page_maxtag

        if page_start <= 1:
            page_start = 1
            page_end = page_maxtag

        if page_end >= total_page:
            page_end = total_page
            page_start = total_page - page_maxtag + 1
            if page_start <= 1:
                page_start = 1

        self.page_start = page_start
        self.page_end = page_end

    def html_page(self):
        html_page = [f'<li><a href="{self.url_address}?page=1">Home</a></li>']

        if self.cur_page_num <= 1:
            html_page.append('<li class="disabled"><a href="#"><span aria-hidden="true">&laquo;</span></a></li>')
        else:
            html_page.append(
                f'<li><a href="{self.url_address}?page={self.cur_page_num-1}><span aira-hidden="true">&laquo;</span></a></li>')

        for i in range(self.page_start, self.page_end + 1):
            if i == self.cur_page_num:
                html_temp = f'<li class="active"><a href="{self.url_address}?page={i}">{i}</a></li>'
            else:
                html_temp = f'<li><a href="{self.url_address}?page={i}">{i}</a></li>'
            html_page.append(html_temp)

        if self.cur_page_num >= self.total_page:
            html_page.append('<li class="disabled"><a href="#"><span aira-hidden="true">&raquo;</span></a></li>')
        else:
            html_page.append(
                f'<li><a href="{self.url_address}?page={self.cur_page_num+1}"><span aria-hidden="true">&raquo;</span></a></li>')

        html_page.append(f'<li><a href="{self.url_address}?page={self.total_page}">Last</a></li>')
        page_nav = "".join(html_page)
        return page_nav

    @property
    def data_start(self):
        return self.rows_start

    @property
    def data_end(self):
        return self.rows_end
