# -*- coding: utf-8 -*-

class Ssql:
    def __init__(self, keys):
        self.sql = 'select * from properties_assets where '
        self.conver = self.unicode_to_ascii
        self.task_list = []
        for attr in keys:
            if isinstance(attr.get('val')[1], tuple):
                tmp = self.fuzzy_match(attr['val'], attr['key'])
                self.task_list.append(tmp)
                continue
            if attr.get('val'):
                tmp = self.exact_fit(attr['val'], attr['key'])
                self.task_list.append(tmp)
        self.sql += ' and '.join(self.task_list)
        self.sql = self.sql.decode('utf-8')

    # 范围搜索(模糊搜索)
    def fuzzy_match(self, arg, t):
        json_k, json_v = arg
        if json_v:
            tp_sql = '''{0[0]}->'$.{0[1]}'>={0[2]} and {0[0]}->'$.{0[1]}'<={0[3]}'''
            format_val = [t, json_k, json_v[0], json_v[1]]
            return tp_sql.format(self.conver(format_val))

    # 精确匹配
    def exact_fit(self, arg, t):
        json_k, json_v = arg
        format_val = [t, json_k, json_v]
        return '''{0[0]}->'$.{0[1]}'={0[2]}'''.format(self.conver(format_val))

    def _format(self, ele):
        if isinstance(ele, unicode):
            if ele == u'parms' or ele == u'instruction':
                ele = ele.encode('utf-8')
            else:
                ele = '"' + ele.encode('utf-8') + '"'
        return ele

    def unicode_to_ascii(self, ul):
        if isinstance(ul, list):
            res = map(self._format, ul)
            return res