""" The apps configuration file for the projects app. """

from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    """ The configuration class for the projects app. """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.projects'
