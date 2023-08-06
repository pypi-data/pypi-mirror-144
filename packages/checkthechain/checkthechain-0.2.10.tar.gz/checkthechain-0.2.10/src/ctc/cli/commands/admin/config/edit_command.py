import os
import subprocess

import ctc.config


def get_command_spec():
    return {
        'f': edit_config_command,
        'help': 'edit config values',
    }


def edit_config_command():
    editor = os.environ.get('EDITOR')
    if editor is None or editor == '':
        editor = 'editor'
        print('$EDITOR env var not set, attempting to use default editor')

    config_path = ctc.config.get_config_path()

    print('editing config in editor')
    print('- editor:', editor)
    print('- config_path:', config_path)
    print()
    subprocess.call([editor, config_path])
    print('done editing config')

