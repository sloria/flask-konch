# -*- coding: utf-8 -*-
import pytest
from flask import Flask
from flask.cli import ScriptInfo
from click.testing import CliRunner

from flask_konch.cli import cli

##### Fixtures #####

@pytest.fixture
def make_app():
    def maker(config):
        app = Flask('testapp')
        app.config['KONCH_SHELL'] = 'py'
        app.config.update(config)

        # Register shell context
        def shell_context_processor():
            return {
                'shellctx': 'shellctx-value',
                'shellctx_overriden_by_konch_context': 'not-overridden'
            }
        app.shell_context_processor(shell_context_processor)

        return app

    return maker

@pytest.fixture(scope='session')
def runner():
    return CliRunner()

@pytest.fixture
def run_command(runner, make_app):
    def run(args=None, config=None, **kwargs):
        app = make_app(config=config or {})
        obj = ScriptInfo(create_app=lambda info: app)
        return runner.invoke(cli, args or [], obj=obj, **kwargs)
    return run

##### Tests #####

def test_no_args(run_command):
    result = run_command()
    assert result.exit_code == 0
    # Flask imports
    assert 'Blueprint, Config, Flask,' in result.output

def test_no_flask_imports(run_command):
    result = run_command(config={'KONCH_FLASK_IMPORTS': False})
    assert 'Blueprint, Config, Flask,' not in result.output

def test_additional_context(run_command):
    result = run_command(
        config={
            'KONCH_CONTEXT': {
                'foo': 'foo-value',
                'bar': 'bar-value'
            }
        },
        input='bar'
    )
    assert 'Additional variables (see KONCH_CONTEXT):' in result.output
    assert 'bar, foo' in result.output
    assert '>>> \'bar-value\'' in result.output

def test_flask_shell_context_processors(run_command):
    result = run_command(
        config={
            'KONCH_CONTEXT': {
                'shellctx_overriden_by_konch_context': 'overridden-by-konch'
            }
        },
        input='shellctx\nshellctx_overriden_by_konch_context'
    )
    # raise Exception(result.output)
    assert 'Flask shell context (see shell_context_processor()):' in result.output
    assert '>>> \'shellctx-value\'' in result.output
    assert '>>> \'overridden-by-konch\'' in result.output

def test_banner(run_command):
    result = run_command(config={'KONCH_BANNER': 'foobarbaz'})
    assert 'foobarbaz' in result.output

def test_prompt(run_command):
    result = run_command(config={'KONCH_PROMPT': 'foo>>>>'})
    assert 'foo>>>>' in result.output

def test_context_format(run_command):
    def format_ctx(ctx):
        return 'foobarbaz'
    result = run_command(config={'KONCH_CONTEXT_FORMAT': format_ctx})
    assert 'foobarbaz' in result.output
