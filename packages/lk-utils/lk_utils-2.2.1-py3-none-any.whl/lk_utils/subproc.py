import os
import subprocess
from functools import wraps
from textwrap import dedent
from threading import Thread


__thread_pool = {}  # dict[hashable func_id, Thread]


def new_thread(daemon=True, singleton=False):
    """ New thread decorator. """
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs) -> Thread:
            if singleton:
                if t := __thread_pool.get(id(func)):
                    if t.is_alive():
                        return t
            thread = __thread_pool[id(func)] = Thread(
                target=func, args=args, kwargs=kwargs
            )
            thread.daemon = daemon
            thread.start()
            return thread
        
        return wrapper
    
    return decorator


def run_new_thread(target, args=None, kwargs=None, daemon=True) -> Thread:
    """ Run function in a new thread at once. """
    thread = Thread(target=target, args=args or (), kwargs=kwargs or {})
    thread.daemon = daemon
    thread.start()
    return thread


# ------------------------------------------------------------------------------

def run_cmd_shell(cmd: str, multi_lines=False, ignore_errors=False):
    """
    References:
        https://docs.python.org/zh-cn/3/library/subprocess.html
    """
    if multi_lines:
        # https://stackoverflow.com/questions/20042205/calling-multiple-commands
        #   -using-os-system-in-python
        cmd = dedent(cmd).strip().replace('\n', ' & ')
        #   TODO:
        #       replaced with '&' for windows
        #       replaced with ';' for linux (not implemented yet)
    
    try:
        '''
        subprocess.run:params
            shell=True  pass in a string, call the command as a string.
            shell=False pass in a list, the first element of the list is used
                        as the command, and the subsequent elements are used as
                        the parameters of the command.
            check=True  check return code, if finish with no exception
                        happened, the code is 0; otherwise it is a non-zero
                        number, and raise an error called `subprocess
                        .CalledProcessError`.
            capture_output=True
                        capture and retrieve stream by:
                            ret = subprocess.run(..., capture_output=True)
                            ret.stdout.read()  # -> bytes ...
                            ret.stderr.read()  # -> bytes ...
        '''
        ret = subprocess.run(
            cmd, shell=True, check=True, capture_output=True
        )
        ret = ret.stdout.decode(encoding='utf-8', errors='replace').strip()
    except subprocess.CalledProcessError as e:
        ret = e.stderr.decode(encoding='utf-8', errors='replace').strip()
        if not ignore_errors:
            raise Exception(dedent(f'''
                Command shell error happend:
                    cmd: {cmd}
                    err: {ret}
            '''))
    return ret


def run_cmd_args(*args, ignore_errors=False):
    return run_cmd_shell(' '.join(format_cmd(*args)),
                         ignore_errors=ignore_errors)


def run_bat_script(file, *args, **kwargs):
    return run_cmd_args(*format_cmd(file, *args, **kwargs))


def format_cmd(*args, **kwargs):
    out = []
    
    def _is_unwrapped(arg):
        # assert len(arg) > 0
        if ' ' in arg and not (arg[0] == '"' or arg[-1] in '"'):
            return True
        else:
            return False
    
    for i in args:
        if i is None:
            continue
        if (i := str(i).strip()) == '':
            continue
        if _is_unwrapped(i):
            i = f'"{i}"'
        out.append(i)
    
    if kwargs:
        # assert all(bool(' ' not in k) for k in kwargs)
        for k, v in zip(map(str, kwargs.keys()), map(str, kwargs.values())):
            # if k.startswith('_'):
            #     prefix = re.match(r'^_+', k).group()
            #     k = prefix.replace('_', '-') + k
            k = k.strip().replace('_', '-')
            v = v.strip()
            if v:
                if _is_unwrapped(v):
                    v = f'"{v}"'
                out.append(f'{k}={v}')
            else:
                out.append(k)
    
    return out


# ------------------------------------------------------------------------------

def mklink(src_path, dst_path, exist_ok=False):
    """

    References:
        https://blog.walterlv.com/post/ntfs-link-comparisons.html
    """
    assert os.path.exists(src_path), src_path
    if os.path.exists(dst_path):
        if exist_ok:
            return dst_path
        else:
            raise FileExistsError(dst_path)
    
    if os.path.isdir(src_path):
        run_cmd_shell(f'mklink /J "{dst_path}" "{src_path}"')
    elif os.path.isfile(src_path):
        run_cmd_shell(f'mklink /H "{dst_path}" "{src_path}"')
    else:
        raise Exception(src_path)
    
    return dst_path


def mklinks(src_dir, dst_dir, names=None, exist_ok=False):
    out = []
    for n in (names or os.listdir(src_dir)):
        out.append(mklink(f'{src_dir}/{n}', f'{dst_dir}/{n}', exist_ok))
    return out
