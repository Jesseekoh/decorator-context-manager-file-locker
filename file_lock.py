import os
from file_access import FileAccess
if os.name == 'nt':  # windows
    import msvcrt
else:
    import fcntl  # unix/linux


def file_lock(func):
    """Decorator to implement file locking

    Args:
        func (_type_): _description_
    """
    def wrapper(filepath='', mode='r', *args, **kwargs):
        with FileAccess(filepath, mode) as file:
            filesize = os.fstat(file.fileno()).st_size
            try:
                if os.name == 'nt':  # windows platform
                    if mode[0] == 'a':
                        file.seek(0)
                        msvcrt.locking(
                            file.fileno(), msvcrt.LK_NBLCK, filesize)
                        file.seek(0, os.SEEK_END)
                    else:
                        msvcrt.locking(
                            file.fileno(), msvcrt.LK_NBLCK, filesize)
                else:  # unix/linux
                    fcntl.flock(file,
                                fcntl.LOCK_NB | fcntl.LOCK_EX)

                # lock file
                kwargs['file'] = file

                return func(filepath, mode, *args, **kwargs)

            finally:
                # unlock file
                if os.name == 'nt':
                    file.seek(0)
                    msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, filesize)
                else:
                    fcntl.flock(file, fcntl.LOCK_NB | fcntl.LOCK_UN)

    return wrapper
