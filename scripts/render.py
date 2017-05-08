import os.path
import argparse
import gettext
from jinja2 import Environment, FileSystemLoader


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
        default='en',
        help='Langage to translate',
        choices=['es', 'en']
    )
    return parser


def __build_jinja_env(language):
    template_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        'templates'
    )

    locale_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        'locale'
    )

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


def main():
    parser = __build_parser()
    args = parser.parse_args()
    env = __build_jinja_env(args.language)

    template = env.get_template(args.template)
    print(template.render())


if __name__ == '__main__':
    main()
