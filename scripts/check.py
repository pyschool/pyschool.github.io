"""Checks the syntax of a jinja template"""
import os.path
import argparse
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
        help='template to check'
    )
    return parser


def __build_jinja_env():
    template_path = os.path.join(os.path.dirname(__file__), '..', 'templates')
    return Environment(loader=FileSystemLoader(template_path))


def __main():
    parser = __build_parser()
    args = parser.parse_args()
    env = __build_jinja_env()

    try:
        env.get_template(args.template)
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


if __name__ == '__main__':
    __main()
