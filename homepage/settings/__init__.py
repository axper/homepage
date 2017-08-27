from split_settings.tools import optional, include

# This file contains default settings, development environment should "just work" without any changes
include(
    'components/base.py',
    # In production environment, we symlink 'available/production.py' to 'components/production.py'
    optional('components/production.py'),

    # Local settings, just in case we need something custom
    optional('local_settings.py'),

    scope=locals()
)
