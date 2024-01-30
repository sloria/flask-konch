"""Entry point for the ``konch`` Flask CLI commmand."""

from flask.cli import with_appcontext
import click
import flask
import konch


DEFAULTS = dict(
    KONCH_FLASK_IMPORTS=True,
    KONCH_FLASK_SHELL_CONTEXT=True,
    KONCH_CONTEXT={},
    KONCH_SHELL="auto",
    KONCH_BANNER=None,
    KONCH_PROMPT=None,
    KONCH_OUTPUT=None,
    KONCH_CONTEXT_FORMAT=None,
    KONCH_IPY_AUTORELOAD=False,
    KONCH_IPY_EXTENSIONS=None,
    KONCH_IPY_COLORS=None,
    KONCH_IPY_HIGHLIGHTING_STYLE=None,
    KONCH_PTPY_VI_MODE=False,
)


def get_flask_imports():
    ret = {}
    for name in [e for e in dir(flask) if not e.startswith("_")]:
        ret[name] = getattr(flask, name)
    return ret


@click.command()
@with_appcontext
def cli():
    """An improved shell command, based on konch."""
    app = flask.current_app
    options = {key: app.config.get(key, DEFAULTS[key]) for key in DEFAULTS.keys()}
    base_context = {"app": app}
    if options["KONCH_FLASK_IMPORTS"]:
        base_context.update(get_flask_imports())

    context = dict(base_context)

    if options["KONCH_FLASK_SHELL_CONTEXT"]:
        flask_context = app.make_shell_context()
        context.update(flask_context)

    context.update(options["KONCH_CONTEXT"])

    def context_formatter(ctx):
        formatted_base = ", ".join(sorted(base_context.keys()))
        ret = "\n{FLASK}\n{base_context}\n".format(
            FLASK=click.style("Flask:", bold=True), base_context=formatted_base
        )
        if options["KONCH_FLASK_SHELL_CONTEXT"]:
            variables = ", ".join(sorted(flask_context.keys()))
            ret += "\n{ADDITIONAL}\n{variables}\n".format(
                ADDITIONAL=click.style(
                    "Flask shell context (see shell_context_processor()):", bold=True
                ),
                variables=variables,
            )
        if options["KONCH_CONTEXT"]:
            variables = ", ".join(sorted(options["KONCH_CONTEXT"].keys()))
            ret += "\n{ADDITIONAL}\n{variables}".format(
                ADDITIONAL=click.style(
                    "Additional variables (see KONCH_CONTEXT):", bold=True
                ),
                variables=variables,
            )
        return ret

    context_format = options["KONCH_CONTEXT_FORMAT"] or context_formatter
    konch.start(
        context=context,
        shell=options["KONCH_SHELL"],
        banner=options["KONCH_BANNER"],
        prompt=options["KONCH_PROMPT"],
        output=options["KONCH_OUTPUT"],
        ptpy_vi_mode=options["KONCH_PTPY_VI_MODE"],
        context_format=context_format,
        ipy_extensions=options["KONCH_IPY_EXTENSIONS"],
        ipy_autoreload=options["KONCH_IPY_AUTORELOAD"],
        ipy_colors=options["KONCH_IPY_COLORS"],
        ipy_highlighting_style=options["KONCH_IPY_HIGHLIGHTING_STYLE"],
    )
