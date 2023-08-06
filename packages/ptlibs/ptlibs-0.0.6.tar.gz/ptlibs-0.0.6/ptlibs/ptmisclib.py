import itertools
import datetime
import random
import signal
import struct
import sys
import string
import re
import ipaddress

import requests
from . import ptdefs

try:
    import fcntl, termios
except:
    pass


strip_ANSI_escape_sequences_sub = re.compile(r"""
    \x1b     # literal ESC
    \[       # literal [
    [;\d]*   # zero or more digits or semicolons
    [A-Za-z] # a letter
    """, re.VERBOSE).sub


def print_banner(scriptname, version, condition=None, space=1):
    if not condition:
        print(rf"""
 ____            _                        _____           _
|  _ \ ___ _ __ | |_ ___ _ __ ___ _ __   |_   _|__   ___ | |___
| |_) / _ \ '_ \| __/ _ \ '__/ _ \ '_ \    | |/ _ \ / _ \| / __|
|  __/  __/ | | | ||  __/ | |  __/ |_) |   | | (_) | (_) | \__ \
|_|   \___|_| |_|\__\___|_|  \___| .__/    |_|\___/ \___/|_|___/
                                 |_|{" "*(26-len(scriptname+version)-1)}{scriptname} v{version}
                                       https://www.penterep.com""")
        print("\n"*space)


def randomIP():
    ip = ''
    ip += str(random.randint(1, 255))   # first octet
    for i in range(3):
        ip += '.'   # dot between octets
        ip += str(random.randint(0, 255))   # octet 2-4
    return ip


def randomPort():
    port = random.randint(1, 65535)
    return port


def help_calc_column_width(lines):
    if isinstance(lines[0], list):
        max_cols_len =  [0 for x in range(10)]
        for row in lines:
            for index, column in enumerate(row):
                x = len(column)
                if (x > max_cols_len[index]) and not index+1 == len(row):
                    max_cols_len[index] = x
        return max_cols_len


def help_print(help_object, scriptname, version):
    print_banner(scriptname, version)
    for help_item in help_object:
        print( out_title(f"{list(help_item.keys())[0].capitalize().replace('_', ' ')}:", show_bullet=False))
        lines = list(help_item.values())[0]
        cols_width = help_calc_column_width(lines)
        for line in lines:
            if isinstance(line, list):
                for index, column in enumerate(line):
                    if not index:
                        print("   ", end="")
                    print(column, end=(cols_width[index]-len(column)+2)*' ')
                print("")
            else:
                print(f"   {line}")
        print("")


def signal_handler(sig, frame):
    ptprint(f"\r", clear_to_eol=True)
    ptprint( out_if(f"{ptdefs.colors['ERROR']}Script terminated{ptdefs.colors['TEXT']}", "ERROR"), clear_to_eol=True)
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


def check_connectivity(proxies=[]):
    try:
        requests.request("GET", "https://www.google.com", proxies=proxies, verify=False, allow_redirects=False)
    except:
        print()
        ptprint( out_if(f"{ptdefs.colors['ERROR']}Missing net connectivity{ptdefs.colors['TEXT']}", "ERROR"))
        sys.exit(0)


def is_valid_ip_address(ip: str) -> bool:
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def check_url_availability(url, proxies=[]):
    try:
        requests.request("GET", url, proxies=proxies, verify=False, allow_redirects=False)
    except Exception as e:
        ptprint( out_if(f"{ptdefs.colors['ERROR']}URL is not available: {e}{ptdefs.colors['TEXT']}", "ERROR"))
        sys.exit(0)


def bullet(bullet_type=None):
    if bullet_type and ptdefs.chars.get(bullet_type):
        return f"{ptdefs.colors[bullet_type]}[{ptdefs.chars[bullet_type]}]{ptdefs.colors['TEXT']} "
    else:
        return ""


def out_if(string="", bullet_type=None, condition=True, colortext=False):
    if condition:
        if colortext:
            return f"{bullet(bullet_type)}{ptdefs.colors[bullet_type]}{string}{ptdefs.colors['TEXT']}"
        else:
            return f"{bullet(bullet_type)}{string}"


def out_ifnot(string="", bullet_type=None, condition=False, colortext=False):
    if not condition:
        if colortext:
            return f"{bullet(bullet_type)}{ptdefs.colors[bullet_type]}{string}{ptdefs.colors['TEXT']}"
        else:
            return f"{bullet(bullet_type)}{string}"
    else:
        return ""


def out_title(string, show_bullet=True):
    if show_bullet:
        return f"{bullet('TITLE')}{ptdefs.colors['TITLE']}{string}{ptdefs.colors['TEXT']}"
    else:
        return f"{ptdefs.colors['TITLE']}{string}{ptdefs.colors['TEXT']}"


def out_title_if(string="", condition=True, show_bullet=True):
    if condition:
        return out_title(string, show_bullet)
    else:
        return ""


def out_title_ifnot(string="", condition=False, show_bullet=True):
    if not condition:
        return out_title(string, show_bullet)
    else:
        return ""


def ptprint_(string, end="\n", flush=False, clear_to_eol=False, filehandle=False):
    """Legacy solution."""
    if string:
        if clear_to_eol:
            string = string + (' ' * (terminal_width() - len_string_without_colors(string)))
        print(string, end=end, flush=flush)
        if filehandle:
                string = re.sub("\033\[\d+m", "", string)
                filehandle.write(string.lstrip()+end)


def ptprint(string, bullet_type=None, condition=None, end="\n", flush=False, colortext=False, clear_to_eol=False, newline_above=False, filehandle=False):
    if string:
        if bullet_type:
            bullet_type = bullet_type.upper()
        if condition is None:
            if bullet_type:
                if colortext:
                    string = get_colored_text(string, bullet_type)
                string = bullet(bullet_type)+string
        elif condition and condition is not None:
            string = out_if(string, bullet_type, condition, colortext)
        else:
            return
        if newline_above:
            string = "\n" + string
        if clear_to_eol:
            string = string + (' ' * (terminal_width() - len_string_without_colors(string)))
        print(string, end=end, flush=flush)
        if filehandle:
            string = re.sub("\033\[\d+m", "", string)
            filehandle.write(string.lstrip()+end)


def get_colored_text(string, color):
    return f"{ptdefs.colors[color]}{string}{ptdefs.colors['TEXT']}"


def clear_line(end="\n"):
        print(' '*terminal_width(), end=end)


def clear_line_ifnot(end="\n", condition=True):
    if condition:
        clear_line(end)


def clear_line_ifnot(end="\n", condition=False):
    if not condition:
        clear_line(end)


def len_string_without_colors(string):
    return len(strip_ANSI_escape_sequences_sub("", string))


def add_spaces_to_eon(string, minus=0):
    return string + (' ' * (terminal_width() - len_string_without_colors(string) - minus))


def end_error(message, json_no, json_object, condition):
    ptprint( out_ifnot(f"Error: {message}", "ERROR", condition) )
    json_object.set_status(json_no, "error", message)
    ptprint( out_if(json_object.get_all_json(), None, condition) )
    sys.exit(1)


def read_file(file):
    with open(file, "r") as f:
        domain_list = [line.strip("\n") for line in f]
        return domain_list


def get_request_headers(args):
    request_headers = {}
    if args.user_agent:
        request_headers.update({"User-Agent": args.user_agent})
    if args.cookie:
        if isinstance(args.cookie, list):
            request_headers.update({"Cookie": '; '.join(args.cookie)})
        elif isinstance(args.cookie, str):
            request_headers.update({"Cookie": args.cookie})
    if args.headers:
        for header in args.headers:
            request_headers.update({header.split(":")[0]: header.split(":")[1]})
    return request_headers


def pairs(pair):
    if len(pair.split(":")) == 2:
        return pair
    else:
         raise ValueError('Not a pair')


def get_combinations(charset, min, max):
    pool = tuple(charset)
    n = len(pool)
    for len_str in range (min, max+1):
        for indices in itertools.product(range(n), repeat=len_str):
            yield "".join(tuple(pool[i] for i in indices))


def get_keyspace(charset, len_min, len_max, multiple=1):
    c = len(charset)
    keyspace = 0
    for l in range(len_min, len_max + 1):
        keyspace += c ** l
    return keyspace * multiple


def get_wordlist(file_handler, begin_with=""):
    while True:
        data = file_handler.readline().strip()
        if not data:
            break
        if data.startswith(begin_with):
            yield data

def get_charset(charsets):
    result = []
    for i in charsets:
        if i == "lowercase":
            result += [char for char in string.ascii_lowercase]
        elif i == "uppercase":
            result += [char for char in string.ascii_uppercase]
        elif i == "numbers":
            result += [char for char in string.digits]
        elif i == "specials":
            result += [char for char in "!#$%&'()@^`{}"]
        else:
            result += [char for char in i if char not in result]
    return result


def add_slash_to_end_url(url):
    if url.find("*") == -1 and not url.endswith("/"):
        return url+"/"
    else:
        return url


def remove_slash_from_end_url(url):
    if url.find("*") == -1 and url.endswith("/"):
        return url[:-1]
    else:
        return url


def terminal_size():
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th

def terminal_width():
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw

def terminal_height():
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return th


def time2str(time):
    return str(str(datetime.timedelta(seconds=time))).split(".")[0]