from split_settings.tools import optional, include

# This file contains default settings, development environment should "just work" without any changes
# In production environment, we symlink 'available/production.py' to 'components/production.py'
include(
    'components/*.py',

    # Local settings, just in case we need somethign custom
    optional('local_settings.py'),

    scope=locals()
)
