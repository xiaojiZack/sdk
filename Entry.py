import erajs.api as a
# import mw.EraItem.EraItem


def cover():
    a.title('EraDemo')
    a.dat()['123'] = 1
    print(a.dat())
    a.page()
    a.mode('grid', 1)
    a.h('EraDemo')
    a.t()
    a.t()
    a.b('新的游戏', a.goto, new_game)
    a.t()
    a.t()
    a.b('继续游戏')
    a.t()
    a.t()
    a.b('游戏设置')
    a.t()
    a.t()
    a.b('退出游戏')


def new_game():
    a.page()
    a.t('“啪”，你从床上掉了下去。', True)
    a.debug('!!!!!!!!!!!!!')
    a.t()
    a.t('“唔~”，好疼。', True)
    a.t()
    a.t('一直睡觉你都不安分，今天也如往常一样，你从床上掉了下来。', True)
    a.t()
    a.t('………………', True)
    a.t()
    a.t('…………', True)
    a.t()
    a.t('……', True)
    a.t()
    a.t('但似乎今天情况有些不同。', True, style={'color': 'red'})
    a.page()
    a.t('“咳咳咳……”', True, style={'shake_duration': 3})
    a.t()
    a.t('“你剧烈地咳嗽起来。”', True)
    a.t()
    a.t('你跌落在地所激起的大量灰尘随着你的呼吸进入你的鼻腔。', True)
    a.t()
    a.t('“怎么回事！咳咳咳……为什么我房间里面会有这么多灰尘！”', True)
    a.t()
    a.t('你挣扎着爬起来，却发现', True)
    a.t()
    a.t('『陌生的天花板』', True)
    a.t()
    a.t('这是哪里？！', True, style={'color': 'red'})
    a.goto(center)


aa = True
bb = True
cc = True


def center():
    global aa, bb, cc
    a.page()
    a.t('现在你打算怎么做？')
    a.t()
    a.t()
    if aa:
        a.b('观察环境', a.goto, look)
        a.t('　')
    if bb:
        a.b('四处摸索', a.goto, touch)
        a.t('　')
    if cc:
        a.b('侧耳细听', a.goto, listen)
    if not aa and not bb and not cc:
        a.b('思考', a.goto, think)


def look():
    global aa, bb, cc
    a.page()
    aa = False
    a.t('你四处张望，只有门缝下透着些许幽暗的光芒。', True)
    a.t()
    a.t('你看到自己站在床边，屋内还有一把椅子。', True)
    a.t()
    a.t('椅子上仿佛有个')
    a.t('黑影', style={'color': 'red'})
    a.t('。')
    a.t()
    a.t()
    a.b('继续', a.back)


def touch():
    global aa, bb, cc
    a.page()
    bb = False
    a.t('你四处摸索，床是一张普通的床', True)
    a.t()
    a.t('屋内还有一把椅子。', True)
    a.t()
    a.t('椅子上有一个软软绵绵的东西', True)
    a.t()
    a.t('这种触感……', True)
    a.t('好熟悉……', style={'color': 'red'})
    a.t()
    a.t()
    a.b('继续', a.back)


def listen():
    global aa, bb, cc
    a.page()
    cc = False
    a.t('你侧耳倾听，四周都静悄悄的。', True)
    a.t()
    a.t('几乎什么都听不见。', True)
    a.t()
    a.t('但屋内有着微弱且均匀的呼吸声……', True)
    a.t()
    a.t('是从')
    a.t('椅子', style={'color': 'red'})
    a.t('那边传过来的！', True)
    a.t()
    a.t('是')
    a.t('活物', style={'color': 'red'})
    a.t('！')
    a.t()
    a.t()
    a.b('继续', a.back)


def think():
    a.page()
    a.t('你稍加思索，很快便得出了结论。', True)
    a.t()
    a.t('那椅子上的活物，没有错的话，', True)
    a.t()
    a.t('应该是一位熟睡的')
    a.t('少女', style={'color': 'red'})
    a.t('。', True)
    a.t()
    a.t('因为你触碰到了她的身体，闻到了少女特有的香气。', True)
    a.t()
    a.t('你继续进行着调查，发现自己的推论完全正确。', True)
    a.t()
    a.t('甚至还有更加惊人的发现……', True)
    a.t()
    a.t('这个少女是被绑在了椅子上！', True)
    a.t()
    a.t('而且她的神智似乎也要渐渐恢复了。', True)
    a.t()
    a.t('这时候，你选择……', True)
    a.t()
    a.page()
    a.mode('grid', 1)
    a.t()
    a.t()
    a.t('未完待续……')
    a.t()
    a.t()
    a.b('打群主！', a.goto, bit)


def bit():
    a.page()
    a.mode('grid', 1)
    a.t()
    a.t()
    a.t('群主：“哎呀哎呀别打啦！”')
    a.t()
    a.t()
    a.b('好吧，饶你一命', a.goto, goon)


def goon():
    a.page()
    a.t('………………', True)
    a.t()
    a.t('…………', True)
    a.t()
    a.t('……', True)
    a.t()
    a.t('“唔……”', True)
    a.t()
    a.t('少女皱着眉头，艰难地抬起了眼。', True)
    a.t()
    a.t('房间仅剩的那一扇门下泛出的微弱黄光，刚好能让你和少女看见彼此的轮廓。', True)
    a.t()
    a.t('毕竟房间里也没有另一个东西方便你躲藏了。', True)
    a.t()
    a.t('于是很显然地，少女意识到了你的存在。', True)
    a.t()
    a.t('但她')
    a.t('并没有吱声', style={'color': 'red'})
    a.t('。', True)
    a.t()
    a.t('仅仅是看着你（的轮廓）。', True)
    a.t()
    a.t('这时候你……')
    a.t()
    a.t()
    a.b('轻柔礼貌地自我介绍', action, 'polite')
    a.t(' ')
    a.b('直接交谈', action, 'direct')
    a.t(' ')
    a.b('粗♂鲁♂而♂直♂接地交流', action, 'rude')


def action(type):
    a.page()
    if type == 'polite':
        a.t('你轻声说：“你好，请不要紧张，我不会伤害你的。”', True)
        a.t()
        a.t('少女疑惑地睁大了双眼：“你有病吧？快来干我！”', True)
        a.t()
        a.t('你：“？？？（黑人问号）”', True)
        a.page()
        a.mode('grid', 1)
        a.t()
        a.t()
        a.h('你死了')
        a.t()
        a.t()
        a.t('获得成就：《？？？》')
        a.t()
        a.t()
        a.b('重新开始', a.back, 5)
    elif type == 'direct':
        a.t('你说：“嘘……', True)
        a.t('想活命的话就别出声，', True)
        a.t('明白吗？”', True)
        a.t()
        a.t('少女迷茫地看着你，似乎', True)
    elif type == 'rude':
        a.t('你一个箭步冲上去，用手捂住她的嘴，在她还没反应过来之前就完全控制住了她。”', True)
        a.t()
        a.t('迷の少女：')
        a.t('“唔！”', True, style={'shake_duration': 3})
        a.t()
        a.t('少女惊恐地睁大了双眼，不停地挣扎着，但身体被绑得结结实实，只能在原地不停的扭动。', True)
        a.t()
        a.t('纤细的腰肢在尽力地挣扎，但似乎收效不大。', True)
        a.t()
        a.t('你仅仅是堵住了她的嘴。', True)
        a.t()
        a.t('然后你就被扶她透了。被一群', True)


def load_game():
    pass


def game_setting():
    pass


def exit_game():
    pass


if __name__ == "__main__":
    # print(a.dat().keys())
    a.init()
    a.goto(cover)
