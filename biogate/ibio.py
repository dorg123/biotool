import IPython
import argparse
from traitlets.config.loader import Config
import biogate
import uuid
import sys
from biogate import session


def parse_terminal_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--session', help='Resume a session using a session id')
    args = parser.parse_args()
    sys.argv = sys.argv[:1]
    return args


def get_ibio_locals():
    return {}


def start_ibio(ibio_locals, session_variables):
    session_variables.update(ibio_locals)
    IPython.start_ipython(
        user_ns=session_variables,
        config=Config(TerminalInteractiveShell={'banner1': f'iBiogate version {biogate.__version__}'})
    )
    _locals = ['In', 'Out', 'get_ipython', 'exit', 'quit', 'session_id',
               'ibio_locals', 'session_variables'] + list(ibio_locals.keys())
    return {key: value for key, value in locals().items() if key not in _locals and not key.startswith('_')}


def main():
    autosave = True
    session_variables = {}
    args = parse_terminal_arguments()
    ibio_locals = get_ibio_locals()
    if args.session:
        session_variables = session.load_session(args.session)
        autosave = False
    session_id = args.session or uuid.uuid4()
    ibio_locals['session_id'] = session_id
    session_variables = start_ibio(ibio_locals, session_variables)
    session.save_session(session_id, session_variables, autosave=autosave)


if __name__ == '__main__':
    main()
