import erajs.api as a
#此处存放物品相关基本类
test = True

false = False
true = True

class Manager_Item:
    #编号
    NO = 0
    #物品名字
    name = ""
    #物品类型
    kind = 0
    #描述
    description = ""
    #能否装备
    equip_able = False
    #是否一次性
    disposable = False
    #是否可堆叠
    stackable = False
    #已拥有数量
    num = 0
    #其他数据
    data = {}
    '''可片段创建新对象属性，也可通过new_item={}创建所有属性'''
    def __init__(self, new_item={}, name="", kind=0, description="", equip_able=False,
                 disposable=False, stackable=False, num=0, data={}):
        if new_item != {}:
            name = new_item["name"]
            kind = new_item["kind"]
            description = new_item["description"]
            equip_able = new_item["equip_able"]
            disposable = new_item["disposable"]
            stackable = new_item["stackable"]
            num = new_item["num"]
            data = new_item["data"]

        self.name = name
        self.kind = kind
        self.description = description
        self.equip_able = equip_able
        self.disposable = disposable
        self.stackable = stackable
        self.num = num
        self.data = data
        Manager_Item.NO += 1
        self.No = Manager_Item.NO

    '''片段更新'''
    def patch(self, key, value):
        exec('self.{} = {}'.format(key, value))

    '''替换更新'''
    def renew(self, new_item):
        name = new_item["name"]
        kind = new_item["kind"]
        description = new_item["description"]
        equip_able = new_item["equip_able"]
        disposable = new_item["disposable"]
        stackable = new_item["stackable"]
        num = new_item["num"]
        data = new_item["data"]

        self.name = name
        self.kind = kind
        self.description = description
        self.equip_able = equip_able
        self.disposable = disposable
        self.stackable = stackable
        self.num = num
        self.data = data
    
    '''道具使用'''
    def use(self):
        if self.num > 0:
            if self.disposable == true:
                self.num -= 1
        else:
            return "no more"

    @classmethod
    def all_item_list(cls):
        '''列出所有角色'''
        return a.data['item']

    @classmethod
    def filter_as(cls, key, value):
        for item in a.data['item']:
            exec('if item.{} == {}: return role'.format(key, value))


if test == True:
    item_1 = {
        "name":"test",
        "kind":0,
        "description":"",
        "data":{"test" : True},
        "equip_able":False,
        "disposable":False,
        "stackable":False,
        "num":0
    }
    item_2 = Manager_Item()
    new_item = Manager_Item(item_1)
    print(new_item)