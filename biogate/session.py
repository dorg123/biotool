import logging
import os
import json
import functools
from biogate.configuration import session as session_cfg


def ensure_dir_exists(dirpath):
    def decorator(func):
        @functools.wraps(func)
        def out(*args, **kwargs):
            if not os.path.exists(dirpath) or not os.path.isdir(dirpath):
                os.mkdir(dirpath)
            return func(*args, **kwargs)
        return out
    return decorator


def ensure_session_dir_exists(func):
    @ensure_dir_exists(session_cfg.session_dir)
    @ensure_dir_exists(session_cfg.autosave_dir)
    @ensure_dir_exists(session_cfg.named_session_dir)
    @functools.wraps(func)
    def out(*args, **kwargs):
        return func(*args, **kwargs)
    return out


@ensure_session_dir_exists
def save_session(session_id, session, *, autosave=False):
    session_dir = session_cfg.autosave_dir if autosave else session_cfg.named_session_dir
    try:
        with open(os.path.join(session_dir, f'{session_id}.json'), 'w') as session_file:
            json.dump(session, session_file)
        logging.info(f'Session saved ({session_id}).')
    except TypeError:
        logging.exception(f'Session {session_id} cannot be saved.')


@ensure_session_dir_exists
def load_session(session_id, *, autosave=False):
    session_dir = session_cfg.autosave_dir if autosave else session_cfg.named_session_dir
    try:
        with open(os.path.join(session_dir, f'{session_id}.json'), 'r') as session_file:
            return json.load(session_file)
    except IOError:
        logging.error(f'Session {session_id} cannot be found.')
    except json.JSONDecodeError:
        logging.error(f'Session {session_id} cannot be loaded.')
    return {}
