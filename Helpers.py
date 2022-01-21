from math import ceil
import decimal
from queue import Queue
import sys
import os
import time
import json


dir_path = 'test'


class My_Exchange():
    def __init__(self, name, **kwargs):
        super(My_Exchange, self).__init__()
        self.prices = {}
        self.bal = {}
        self.name = name


class KivyQueue(Queue):
    notify_func = None

    def __init__(self, notify_func, **kwargs):
        Queue.__init__(self, **kwargs)
        self.notify_func = notify_func

    # def put(self, key, val):
    def put(self, thing):
        '''
        Adds a (key, value) tuple to the queue and calls the callback function.
        '''
        # Queue.put(self, (key, val), False)
        Queue.put(self, thing, False)
        return self.notify_func()

    def get(self):
        '''
        Returns the next items in the queue, if non-empty, otherwise a
        :py:attr:`Queue.Empty` exception is raised.
        '''
        return Queue.get(self, False)


def resource_path():
    '''Returns path containing content - either locally or in pyinstaller tmp file'''
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS)

    return os.path.join(os.path.abspath(""))


def file_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("")
    # return os.path.join('~/Applications/HappyHour', relative_path)
    return os.path.join(base_path, relative_path)


def get_store(kind):
    store_path = dir_path + kind + '.json'

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    if not os.path.exists(store_path):
        blank = {}
        with open(store_path, 'w') as jsonFile:
            json.dump(blank, jsonFile)

    try:
        with open(store_path, 'r') as f:
            store = json.load(f)

        return store
    except Exception as e:
        print('Error in Opening', kind, '. Archiving and creating fresh copy.')
        print(e)
        archive_store(kind)
        try:
            blank = {}
            with open(store_path, 'w') as jsonFile:
                json.dump(blank, jsonFile)
            with open(store_path, 'r') as f:
                store = json.load(f)
            return store
        except Exception as e:
            print('another error', e)
            return False


def save_store(kind, data):
    store_path = dir_path + kind + '.json'

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    try:
        with open(store_path, 'w') as f:
            json.dump(data, f)

    except Exception as e:
        print('Error in Saving', kind, '. Archiving and creating fresh copy.')
        archive_store(kind)
        try:
            with open(store_path, 'w') as f:
                json.dump(data, f)
        except Exception as e:
            print('another save error', e)
            return False


def archive_store(kind):
    store_path = dir_path + kind + '.json'
    a_store_path = dir_path + '/Archive/' + kind + '_' + time.strftime('%I%M%S%p_%m%d%y') + '.json'
    a_dir_path = dir_path + '/Archive/'

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    if not os.path.exists(a_dir_path):
        os.makedirs(a_dir_path)

    if os.path.exists(store_path):
        os.replace(store_path, a_store_path)


def delete_store(kind):
    store_path = dir_path + kind + '.json'
    os.remove(store_path)


def is_float(stng):
    try:
        stng = str(stng).strip('x')
        stng = stng.replace('/', '')
        float(stng)
        if float(stng) == 0:
            return False
        return True
    except:
        return False


def copy_prec(x, y, *args):
    x = f'{float(x):.20f}'
    y = str(y)
    if not '.' in y:
        return x.split('.')[0]

    if '.' in x and '.' in y:
        num_y = len(y) - y.index('.') - 1
        num_x = len(x) - x.index('.') - 1
        if args:
            num_y += args[0]
        if num_x < num_y:
            # int_dec = x.split('.')
            # int_dec[1] = int_dec[1].ljust(num_y, '0')
            # x = int_dec[0] + '.' + int_dec[1]
            return x
        else:
            int_dec = x.split('.')
            x = int_dec[0] + '.' + int_dec[1][:num_y]
            return x.rstrip('0')


def roundUp(n, d):
    d = int('1' + ('0' * d))
    return ceil(n * d) / d


def num_after_point(x):
    width = 15
    precision = 15
    # s = str(decimal.Decimal(x))
    s = f'{x:{width}.{precision}}'
    print('decimal', str(decimal.Decimal(x)))
    print('other', f'{x:{width}.{precision}}')
    if not '.' in s:
        return 0
    # if (len(s) - s.index('.') - 1) > 10:
    #     return 10
    # else:
    return len(s) - s.index('.') - 1


def format_number(num):
    try:
        dec = decimal.Decimal(num)
    except:
        return 'bad'
    tup = dec.as_tuple()
    delta = len(tup.digits) + tup.exponent
    digits = ''.join(str(d) for d in tup.digits)
    if delta <= 0:
        zeros = abs(tup.exponent) - len(tup.digits)
        val = '0.' + ('0' * zeros) + digits
    else:
        val = digits[:delta] + ('0' * tup.exponent) + '.' + digits[delta:]
    val = val.rstrip('0')
    if val[-1] == '.':
        val = val[:-1]
    if tup.sign:
        return '-' + val
    return val


def sym_to_cp(symbol):
    if '/' in symbol:
        return symbol.split('/')[0], symbol.split('/')[1]

    if 'USDT' in symbol:
        return symbol.split('USDT')[0], 'USDT'

    if 'USD' in symbol:
        return symbol.split('USD')[0], 'USD'

    if 'EUR' in symbol:
        return symbol.split('EUR')[0], 'EUR'

    return symbol[0:-3], 'USD'


def get_list_combo(lst, appd):
    if lst:
        lst = lst.split(',')
        lst = [x.strip(' ') for x in lst]
    else:
        lst = [0]

    if not 0 in lst and appd:
        lst.append(0)

    return lst


def get_num_combo(lst, appd):
    if lst:
        lst = lst.split(',')
        lst = [x.strip(' ') for x in lst]
    else:
        lst = [0]
    if not 0 in lst and appd:
        lst.append(0)
    return lst


if __name__ == '__main__':
    pass


