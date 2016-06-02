# -*- coding: utf-8 -*-
"""Entry point for the ``konch`` Flask CLI commmand."""
from flask.cli import with_appcontext
import click
import flask
import konch


DEFAULTS = dict(
    KONCH_FLASK_IMPORTS=True,
    KONCH_CONTEXT={},
    KONCH_SHELL='auto',
    KONCH_BANNER=None,
    KONCH_PROMPT=None,
    KONCH_CONTEXT_FORMAT=None,
    KONCH_IPY_AUTORELOAD=False,
    KONCH_IPY_EXTENSIONS=None,
    KONCH_PTPY_VI_MODE=False,
)


def get_flask_imports():
    ret = {}
    for name in [e for e in dir(flask) if not e.startswith('_')]:
        ret[name] = getattr(flask, name)
    return ret

@click.command()
@with_appcontext
def cli():
    """An improved shell command, based on konch."""
    from flask.globals import _app_ctx_stack
    app = _app_ctx_stack.top.app
    options = {
        key: app.config.get(key, DEFAULTS[key]) for key in DEFAULTS.keys()
    }
    base_context = {
        'app': app,
    }
    if options['KONCH_FLASK_IMPORTS']:
        base_context.update(get_flask_imports())

    context = dict(base_context)
    context.update(options['KONCH_CONTEXT'])

    def context_formatter(ctx):
        formatted_base = ', '.join(sorted(base_context.keys()))
        ret = '\n{FLASK}\n{base_context}\n'.format(
            FLASK=click.style('Flask:', bold=True),
            base_context=formatted_base
        )
        if options['KONCH_CONTEXT']:
            variables = ', '.join(sorted(options['KONCH_CONTEXT'].keys()))
            ret += '\n{ADDITIONAL}\n{variables}'.format(
                ADDITIONAL=click.style('Addtional variables:', bold=True),
                variables=variables
            )
        return ret

    context_format = options['KONCH_CONTEXT_FORMAT'] or context_formatter
    konch.start(
        context=context,
        shell=options['KONCH_SHELL'],
        banner=options['KONCH_BANNER'],
        prompt=options['KONCH_PROMPT'],
        ptpy_vi_mode=options['KONCH_PTPY_VI_MODE'],
        context_format=context_format,
        ipy_autoreload=options['KONCH_IPY_AUTORELOAD'],
    )
