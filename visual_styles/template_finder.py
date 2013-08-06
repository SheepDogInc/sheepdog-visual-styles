import os
import os.path

from django.conf import settings


def find_templates_in_prefix(*directory_parts):
    """Returns a list of all template names that start with the given
    directory parts (ex. `get_templates_in_apps('visual_style', 'snippets')`
    retrieves all templates that start with 'visual_style/snippets'.)

    This function can only search the templates accessed by the `filesystem`
    and `app_directories` loaders, and does not respect the `TEMPLATE_LOADERS`
    setting. This is not an inherent limitation, just a time constraint.

    """

    directory_name = os.path.join(*directory_parts)
    template_dirs = list(settings.TEMPLATE_DIRS)
    templates = []

    for app in settings.INSTALLED_APPS:
        module = __import__(app)
        module_init_file = os.path.abspath(module.__file__)
        package_directory = os.path.dirname(module_init_file)
        template_directory = os.path.join(package_directory, 'templates')
        template_dirs.append(template_directory)

    for template_directory in template_dirs:
        prefixed_directory = os.path.join(template_directory, directory_name)
        if os.path.exists(prefixed_directory):
            for filename in os.listdir(prefixed_directory):
                templates.append(os.path.join(directory_name, filename))

    return templates
