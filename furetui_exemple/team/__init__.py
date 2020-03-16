"""Blok declaration example
"""
from anyblok.blok import Blok
from anyblok_io.blok import BlokImporter


class Team(Blok, BlokImporter):
    """Team's Blok class definition
    """
    version = "0.1.0"
    author = "Your name"
    required = [
        'anyblok-core',
        'furetui',
        'auth-password',
        'anyblok-io-xml'
    ]
    furetui = {
        # 'i18n': {
        #     'en': en,
        #     'fr': fr,
        # },
        'templates': [
            'templates/team.tmpl',
        ],
    }

    @classmethod
    def import_declaration_module(cls):
        """Python module to import in the given order at start-up
        """
        from . import model  # noqa

    @classmethod
    def reload_declaration_module(cls, reload):
        """Python module to import while reloading server (ie when
        adding Blok at runtime
        """
        from . import model  # noqa
        reload(model)

    def update(self, latest):
        """Update blok"""
        self.import_file_xml('Model.FuretUI.Space', 'data', 'spaces.xml')
        self.import_file_xml('Model.FuretUI.Resource', 'data', 'resources.xml')
        self.import_file_xml('Model.FuretUI.Menu', 'data', 'menus.xml')

        self.import_file_xml('Model.Team', 'data', 'team.xml')
