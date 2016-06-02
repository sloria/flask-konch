# -*- coding: utf-8 -*-
"""Entry point for the ``konch`` Flask CLI commmand."""
from flask.cli import with_appcontext
import click
import flask
import konch


DEFAULTS = dict(
    KONCH_CONTEXT={},
    KONCH_FLASK_IMPORTS=True,
    KONCH_BANNER=None,
    KONCH_SHELL='auto',
    KONCH_IPY_AUTORELOAD=False,
    KONCH_CONTEXT_FORMAT=None,
    # TODO
    KONCH_PROMPT=None,
)

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
        for name in [e for e in dir(flask) if not e.startswith('_')]:
            base_context[name] = getattr(flask, name)

    context = dict(base_context)
    context.update(options['KONCH_CONTEXT'])

    def context_formatter(ctx):
        formatted_base = ', '.join(sorted(base_context.keys()))
        ret = '\nFlask:\n{base_context}\n'.format(base_context=formatted_base)
        if options['KONCH_CONTEXT']:
            additional = ', '.join(sorted(options['KONCH_CONTEXT'].keys()))
            ret += '\nAdditional variables:\n{additional}'.format(additional=additional)
        return ret

    context_format = options['KONCH_CONTEXT_FORMAT'] or context_formatter
    konch.start(
        context=context,
        shell=options['KONCH_SHELL'],
        banner=options['KONCH_BANNER'],
        context_format=context_format,
        ipy_autoreload=options['KONCH_IPY_AUTORELOAD'],
    )
