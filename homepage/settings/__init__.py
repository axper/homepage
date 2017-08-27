from split_settings.tools import optional, include

# This file contains default settings, development environment should "just work" without any changes

include(
    'components/*.py',
    # In production environment, we symlink 'available/production.py' to 'components/production.py'
    optional('components/production.py'),
    # Local settings, just in case we need somethign custom
    optional('local_settings.py'),

    scope=locals()
)
