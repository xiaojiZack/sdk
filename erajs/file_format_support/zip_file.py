import json
import zipfile


def read(file_path):
    with zipfile.ZipFile(file_path) as z:
        data = {}
        for file_name in z.namelist():
            with z.open(file_name) as f:
                data[
                    '.'.join(file_name.split('.')[0:-1])
                ] = json.loads(f.read())
    return data


def write(file_path, data):
    with zipfile.ZipFile(file_path, 'w', zipfile.ZIP_LZMA) as z:
        for key in data:
            z.writestr(
                '{}.json'.format(key),
                json.dumps(
                    data[key], ensure_ascii=False
                )
            )
