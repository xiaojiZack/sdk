#coding with utf-8
import erajs.api as a
#此处存放所有事件基类、基类数据生产函数、

class Manager_events:
    NO = 0
    data = {
        'name':'',
        'description':'',
        'enable':False
    }
    def __init__(self, *args):
        Manager_events.NO += 1
        self.NO = Manager_events.NO
            