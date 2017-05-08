"""Renders a jinja template to a particular file"""
import os.path
import argparse
import gettext
import sys
from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateSyntaxError


def __build_parser():
    parser = argparse.ArgumentParser(
        description='Render template using jinja2'
    )
    parser.add_argument(
        'template',
        metavar='template',
        type=str,
        help='template to render'
    )
    parser.add_argument(
        '--language',
        dest='language',
        help='Langage to translate',
        choices=['es', 'en'],
        required=True
    )
    parser.add_argument(
        '--output',
        dest='output',
        help='Output File',
        required=True
    )
    return parser


def __build_jinja_env(language):
    template_path = os.path.join(os.path.dirname(__file__), '..', 'templates')
    locale_path = os.path.join(os.path.dirname(__file__), '..', 'locale')
    translations = gettext.translation(
        'messages',
        locale_path,
        languages=[language]
    )

    env = Environment(
        loader=FileSystemLoader(template_path),
        extensions=['jinja2.ext.i18n']
    )

    env.install_gettext_translations(translations)

    return env


def __main():
    parser = __build_parser()
    args = parser.parse_args()
    env = __build_jinja_env(args.language)

    try:
        template = env.get_template(args.template)
    except TemplateSyntaxError as ex:
        print(
            "SyntaxError on template {}: Line {}: {}".format(
                ex.name,
                ex.lineno,
                ex.message
            ),
            file=sys.stderr
        )
        sys.exit(1)

    with open(args.output, 'w') as outfile:
        outfile.write(template.render())


if __name__ == '__main__':
    __main()
