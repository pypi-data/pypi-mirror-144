# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['camerahub',
 'schema',
 'schema.management.commands',
 'schema.migrations',
 'schema.templatetags']

package_data = \
{'': ['*'],
 'schema': ['static/css/*',
            'static/favicon/*',
            'static/logos/*',
            'static/svg/*',
            'templates/*',
            'templates/schema/*',
            'templates/watson/includes/*']}

install_requires = \
['Django>=3,<4',
 'awesome-slugify>=1.6.5,<2.0.0',
 'django-autocomplete-light>=3.8.1,<4.0.0',
 'django-autosequence>=0,<1',
 'django-bootstrap-datepicker-plus>=4,<5',
 'django-choices>=1.7.0,<2.0.0',
 'django-clear-cache>=0.3,<0.4',
 'django-countries>=7,<8',
 'django-crispy-forms>=1.9.0,<2.0.0',
 'django-currentuser>=0.5,<0.6',
 'django-dbbackup>=3.3.0,<4.0.0',
 'django-filter',
 'django-fullurl>=1,<2',
 'django-geoposition-2>=0.3.11,<0.4.0',
 'django-health-check>=3.16.3,<4.0.0',
 'django-leaflet>=0.27.1,<0.28.0',
 'django-money>=1.2,<2.0',
 'django-prometheus>=2.0.0,<3.0.0',
 'django-registration>=3.0,<4.0',
 'django-sendgrid-v5',
 'django-settings-export>=1.2.1,<2.0.0',
 'django-simple-history>=3,<4',
 'django-social-share>=2.0.0,<3.0.0',
 'django-speedinfo>=2.0.2,<3.0.0',
 'django-star-ratings==0.9.0',
 'django-tables2>=2.1.1,<3.0.0',
 'django-taggit>=2,<3',
 'django-versatileimagefield>=2.0,<3.0',
 'django-watson>=1.5.5,<2.0.0',
 'django3-collectionfield>=1,<2',
 'djangorestframework>=3.12.1,<4.0.0',
 'drf-generators>=0.5.0,<0.6.0',
 'drf-multiple-serializer>=0.2.3,<0.3.0',
 'numpy>=1.19.1,<2.0.0',
 'platformdirs>=2.5.1,<3.0.0',
 'poetry-version>=0.2.0,<0.3.0',
 'python-memcached>=1.59,<2.0',
 'pytz',
 'pyyaml>=6,<7',
 'uWSGI>=2.0.0,<3.0.0',
 'uritemplate>=4,<5']

extras_require = \
{'pgsql': ['psycopg2-binary>=2.8,<3.0']}

setup_kwargs = {
    'name': 'camerahub',
    'version': '0.36.4',
    'description': 'App for cataloguing vintage cameras, lenses, films, negatives & prints',
    'long_description': "# CameraHub\n\nCameraHub is a web app for film photography that can be used to track cameras, lenses, accessories, films, negatives and prints, to fully\ncatalogue a collection of photographic equipment as well as the pictures that are made with them.\n\nIt replaces an earlier command-line project, called [PhotoDB](https://github.com/djjudas21/photodb-perl), which has now been deprecated.\n\n## Installing CameraHub\n\nThere are several ways of installing CameraHub, depending on your needs:\n\n* With Pip\n* [From source](docs/operations/source.rst)\n* [With Docker](docs/operations/docker.rst)\n* [With Kubernetes](docs/operations/kubernetes.rst)\n\n## Configuring CameraHub\n\nCameraHub requires almost no additional config to run with default settings. However it is insecure in this configuration so at least `CAMERAHUB_SECRET_KEY` and\n`CAMERAHUB_PROD` must be set if you are running in production.\n\nThe following environment variables are supported:\n\n### `CAMERAHUB_ADMIN_EMAIL`\n\nEmail address for the `admin` account\nDefault: `admin@example.com`\n\n### `CAMERAHUB_ADMIN_PASSWORD`\n\nPassword for the `admin` account\nDefault: `admin`\n\n### `CAMERAHUB_DB_ENGINE`\n\n[Database engine](https://docs.djangoproject.com/en/3.0/ref/settings/#engine)\nDefault: `django.db.backends.sqlite3`\n\n### `CAMERAHUB_DB_HOST`\n\n[Database hostname or IP address](https://docs.djangoproject.com/en/3.0/ref/settings/#host) if an engine other than SQLite is configured\n\n### `CAMERAHUB_DB_NAME`\n\n[Database schema or path to SQLite db](https://docs.djangoproject.com/en/3.0/ref/settings/#name)\n`db/db.sqlite3`\n\n### `CAMERAHUB_DB_PASS`\n\n[Database password](https://docs.djangoproject.com/en/3.0/ref/settings/#password) if an engine other than SQLite is configured\n\n### `CAMERAHUB_DB_PORT`\n\n[Database port](https://docs.djangoproject.com/en/3.0/ref/settings/#port) if an engine other than SQLite is configured\n\n### `CAMERAHUB_DB_USER`\n\n[Database username](https://docs.djangoproject.com/en/3.0/ref/settings/#user) if an engine other than SQLite is configured\n\n### `CAMERAHUB_PROD`\n\nEnable [Django production mode](https://docs.djangoproject.com/en/3.0/ref/settings/#debug)\nDefault: `false`\n\n### `CAMERAHUB_SECRET_KEY`\n\nRandom secret value. The default string is for testing only and is insecure in production. Generate a new one [here](https://miniwebtool.com/django-secret-key-generator/)\nDefault: `OverrideMe!`\n\n### `CAMERAHUB_EMAIL_BACKEND`\n\n[Email backend](https://docs.djangoproject.com/en/3.1/topics/email/#email-backends)\nDefault: `django.core.mail.backends.filebased.EmailBackend`\n\n### `CAMERAHUB_SENDGRID_KEY`\n\nAPI key for Sendgrid email backend\n\n### `CAMERAHUB_EMAIL_USE_TLS`'\n\nEnable TLS for SMTP\n\n### `CAMERAHUB_EMAIL_USE_SSL`'\n\nEnable TLS for SMTP\n\n### `CAMERAHUB_EMAIL_HOST`\n\nSMTP server hostname\n\n### `CAMERAHUB_EMAIL_HOST_USER`\n\nSMTP server username\n\n### `CAMERAHUB_EMAIL_HOST_PASSWORD`\n\nSMTP server password\n\n### `CAMERAHUB_EMAIL_PORT`\n\nSMTP server port number\n\n### `CAMERAHUB_FROM_EMAIL`\n\n[From email address](https://docs.djangoproject.com/en/3.0/ref/settings/#default-from-email)\nDefault: `noreply@camerahub.info`\n\n### `CAMERAHUB_DOMAIN`\n\n[Site domain](https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts)\nDefault: `camerahub.info`\n\n### `CAMERAHUB_MEMCACHED`\n\nEnable [Memcached caching](https://docs.djangoproject.com/en/3.0/topics/cache/)\nDefault: `false`\n\n### `CAMERAHUB_MEMCACHED_HOST`\n\nMemcached hostname or IP address\nDefault: `127.0.0.1`\n\n### `CAMERAHUB_MEMCACHED_PORT`\n\nMemcached port\nDefault: `11211`\n\n### `CAMERAHUB_STATUS_URL`\n\nURL for a status page\n\n## See also\n\n* [Changelog](https://github.com/camerahub/camerahub/releases)\n* [Docs](docs/index.rst)\n",
    'author': 'Jonathan Gazeley',
    'author_email': 'camerahub@jonathangazeley.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://camerahub.info/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
