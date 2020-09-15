import time

from . import engine
from .modules import tools

e = engine.Engine()


def init():
    print()
    e.info('Era.js Engine Initializing...')
    e.info('├─ Fixing Path...')
    tools.fix_path()
    e.info('├─ Checking Data Integrity...')

    def on_folder_missing(event):
        e.warn('│  ├─ Folder [{}] Missing. Creating...'.format(event['value']))

    def on_file_missing(event):
        e.warn('│  ├─ File [{}] Missing. Creating...'.format(event['value']))
    e.on('folder_missing', on_folder_missing)
    e.on('file_missing', on_file_missing)
    e.check_file_system()
    e.off('folder_missing', on_folder_missing)
    e.off('file_missing', on_file_missing)
    e.info('│  └─ Data Integrity Checked!')
    e.info('├─ Scanning Configs...')
    configs_found = 0

    def on_config_found(event):
        nonlocal configs_found
        e.info('│  ├─ Config [{}] Found.'.format(event['value']))
        configs_found += 1
    e.on('config_found', on_config_found)
    e.scan_configs()
    e.off('config_found', on_config_found)
    e.info('│  └─ {} Configs Found!'.format(configs_found))
    e.info('├─ Loading Configs...')
    configs_loaded = 0

    def on_config_loaded(event):
        nonlocal configs_loaded
        e.info('│  ├─ Config [{}] Loaded.'.format(event['value']))
        configs_loaded += 1
    e.on('config_loaded', on_config_loaded)
    e.load_configs()
    e.off('config_loaded', on_config_loaded)
    e.info('│  └─ {} Configs Loaded!'.format(configs_loaded))
    e.info('├─ Connecting...')
    e.connect()
    e.info('│  └─ Connected!')
    e.info('├─ Scanning Data Files...')
    data_files_found = 0

    def on_data_file_found(event):
        nonlocal data_files_found
        e.info('│  ├─ Data File [{}] Found.'.format(event['value']))
        data_files_found += 1
    e.on('data_file_found', on_data_file_found)
    e.scan_data_files()
    e.off('data_file_found', on_data_file_found)
    e.info('│  └─ {} Data Files Found!'.format(data_files_found))
    e.info('├─ Loading Data Files...')
    data_files_loaded = 0

    def on_data_file_loaded(event):
        nonlocal data_files_loaded
        e.info('│  ├─ Data File [{}] Loaded.'.format(event['value']))
        data_files_loaded += 1
    e.on('data_file_loaded', on_data_file_loaded)
    e.load_data_files()
    e.off('data_file_loaded', on_data_file_loaded)
    e.info('│  └─ {} Data Files Loaded!'.format(data_files_loaded))
    e.info('├─ Sending Init Finished Signal...')
    e.send({'type': 'loaded'})
    e.info('│  └─ Done!')
    e.info('└─ Initialize Complete!')
    print()
    e.info('Executing Game Scripts...')


def config(data):
    e.set_config(data)


def entry(entry_func):
    e.register_entry(entry_func)


def start(host='0.0.0.0', port=80):
    e.listen(host, port)


def debug(text):
    e.debug(text)


def info(text):
    e.info(text)


def warn(text):
    e.warn(text)


def error(text):
    e.error(text)


def critical(text):
    e.critical(text)


def title(text):
    e.push('title', {'text': str(text)}, None)


def window(style):
    e.push('window', None, style)


def page(style):
    e.remove_all_listeners()
    e.push('page', None, style)


def clear(num):
    e.push('clear', {'num': num}, None)


def heading(text, rank, style):
    e.push('heading', {'text': str(text), 'rank': rank}, style)


def text(text, wait, style):
    if text == None or text == '':
        e.push('pass', None, None)
    else:
        e.push('text', {'text': text}, style)

    if wait and not e.lock_passed():
        e.lock()

        def on_click(event):
            if event['value'] == 1:  # 左键
                if e.is_locked():
                    e.unlock()
                    e.remove_listener('MOUSE_CLICK', on_click)
            elif event['value'] == 3:  # 右键
                if e.is_locked():
                    e.unlock_forever()
                    e.remove_listener('MOUSE_CLICK', on_click)
        e.on('MOUSE_CLICK', on_click)
        e.show_listener_list()
        e.wait_for_unlock()


def button(text, callback, *arg, **kw):
    data = {
        'text': str(text),
        'hash': tools.random_hash()
    }
    data['disabled'] = False
    if 'disabled' in kw.keys():
        if kw['disabled']:
            data['disabled'] = True
        kw.pop('disabled')
    if callback == None:
        data['disabled'] = True
    if 'popup' in kw.keys():
        data['popup'] = str(kw['popup'])
        kw.pop('popup')
    else:
        data['popup'] = ''
    style = None
    if 'style'in kw:
        style = kw['style']
    e.push('button', data, style)

    def on_click(e):
        if e['target'] == data['hash']:
            callback(*arg, **kw)
    e.on('BUTTON_CLICK', on_click, data['hash'])
    e.unlock()


def link(text, callback, style, *arg, **kw):
    data = {
        'text': str(text),
        'hash': tools.random_hash()
    }
    data['disabled'] = False
    if 'disabled' in kw.keys():
        if kw['disabled']:
            data['disabled'] = True
        kw.pop('disabled')
    if callback == None:
        data['disabled'] = True
    if 'popup' in kw.keys():
        data['popup'] = str(kw['popup'])
        kw.pop('popup')
    else:
        data['popup'] = ''
    e.push('link', data, style)

    def on_click(e):
        if e['target'] == data['hash']:
            callback(*arg, **kw)
    e.on('LINK_CLICK', on_click, data['hash'])
    e.unlock()


def progress(now=0, max=100, style=None):
    if style is None:
        style = [{}, {}]
    e.push('progress', {'now': now, 'max': max}, style)


def rate(now=0, max=5, callback=None, style=None):
    data = {
        'now': now,
        'max': max,
        'hash': tools.random_hash()
    }
    data['disabled'] = False
    if callback == None:
        data['disabled'] = True
    if style is None:
        style = {}
    e.push('rate', data, style)
    node = {'value': now}

    def on_click(e):
        # print(e)
        if e['target'] == data['hash']:
            node['value'] = e['value']
            callback(e['value'])
    e.on('RATE_CLICK', on_click, data['hash'])
    return node


def check(text, callback, default, style):
    data = {
        'text': str(text),
        'default': default,
        'hash': tools.random_hash()
    }
    data['disabled'] = False
    if callback == None:
        data['disabled'] = True
    if style is None:
        style = {}
    e.push('check', data, style)
    node = {'value': default}

    def on_click(e):
        if e['target'] == data['hash']:
            node['value'] = e['value']
            callback(e['value'])
    e.on('CHECK_CHANGE', on_click, data['hash'])
    return node


def radio(text_list, callback, default_index, style):
    data = {
        'text_list': text_list,
        'default_index': default_index,
        'hash': tools.random_hash()
    }
    data['disabled'] = False
    if callback == None:
        data['disabled'] = True
    if style is None:
        style = {}
    e.push('radio', data, style)
    node = {'value': default_index}

    def on_click(e):
        if e['target'] == data['hash']:
            node['value'] = e['value']
            callback(e['value'])
    e.on('RADIO_CHANGE', on_click, data['hash'])
    return node


def input(callback, default, is_area, placeholder, style):
    data = {
        'default': default,
        'is_area': is_area,
        'placeholder': placeholder,
        'hash': tools.random_hash()
    }
    data['disabled'] = False
    if callback == None:
        data['disabled'] = True
    if style is None:
        style = {}
    e.push('input', data, style)
    node = {'value': default}

    def on_click(e):
        if e['target'] == data['hash']:
            node['value'] = e['value']
            callback(e['value'])
    e.on('INPUT_CHANGE', on_click, data['hash'])
    return node


def dropdown(text_list, callback, default_index, search, multiple, placeholder, allowAdditions, style):
    data = {
        'text_list': text_list,
        'default_index': default_index,
        'search': search,
        'multiple': multiple,
        'placeholder': placeholder,
        'allowAdditions': allowAdditions,
        'hash': tools.random_hash()
    }
    data['disabled'] = False
    if callback == None:
        data['disabled'] = True
    if style is None:
        style = {}
    e.push('dropdown', data, style)
    node = {'value': default_index}

    def on_click(e):
        if e['target'] == data['hash']:
            node['value'] = e['value']
            callback(e['value'])
    e.on('DROPDOWN_CHANGE', on_click, data['hash'])
    return node


def divider(text, style):
    e.push('divider', {'text': text}, style)


def get_data():
    return e.dat()


def goto(ui_func, *arg, **kw):
    e.goto(ui_func, *arg, **kw)


def back(num, *arg, **kw):
    e.back(num, *arg, **kw)


def mode(type, *arg, **kw):
    e.push('mode', {'type': type, 'arg': arg}, None)


def dangerously_get_engine_core():
    return e


def cfg(dot_path):
    return e.cfg(dot_path)


def dat(dot_path):
    return e.dat(dot_path)


def sav():
    return e.sav()


def new_hash(level=4):
    return tools.random_hash(level)
