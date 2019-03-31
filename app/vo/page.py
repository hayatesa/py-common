# -*- coding: utf-8 -*-
class Page:

    def __init__(self, total, page_size, total_page, page_num, rows):
        """
        :param total: 总记录数
        :param page_size: 页大小
        :param total_page: 总页数
        :param page_num: 当前页
        :param rows: 数据
        :param prevPage: 上一页页码
        :param nextPage: 下一页页码
        """
        self.total = total
        self.pageSize = page_size
        self.totalPage = total_page
        self.pageNum = page_num
        self.rows = rows
        self.prevPage = page_num - 1 if page_num > 1 else 1
        self.nextPage = page_num + 1 if page_num < total_page else total_page
