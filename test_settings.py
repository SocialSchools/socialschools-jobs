#!/usr/bin/env python
# -*- coding: utf-8 -*-


class DisableMigrations(dict):

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return "notmigrations"

gettext = lambda s: s

HELPER_SETTINGS = {
    'TIME_ZONE': 'Europe/Zurich',
    'INSTALLED_APPS': [
        'aldryn_apphooks_config',
        # needed for tests, since we need to reload server after apphook has
        # been added to a page, otherwise we cannot get a correct url.
        'aldryn_apphook_reload',
        'aldryn_boilerplates',
        'aldryn_categories',
        'aldryn_reversion',
        'aldryn_common',
        'aldryn_jobs',
        'bootstrap3',
        'reversion',
        'appconf',
        'filer',
        'parler',
        'sortedm2m',
        'easy_thumbnails',
        'djangocms_text_ckeditor',
        'adminsortable2',
    ],
    'THUMBNAIL_PROCESSORS': (
        'easy_thumbnails.processors.colorspace',
        'easy_thumbnails.processors.autocrop',
        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
        'easy_thumbnails.processors.filters',
    ),
    'LANGUAGES': (
        ('en', 'English'),
        ('de', 'German'),
    ),
    'PARLER_LANGUAGES': {
        1: (
            {'code': 'en'},
            {'code': 'de'},
        ),
        'default': {
            'hide_untranslated': False,
        }
    },
    'CMS_LANGUAGES': {
        'default': {
            'public': True,
            'hide_untranslated': False,
            'fallbacks': ['en']

        },
        1: [
            {
                'public': True,
                'code': 'en',
                'hide_untranslated': False,
                'name': gettext('en'),
                'redirect_on_fallback': True,
            },
            {
                'public': True,
                'code': 'de',
                'hide_untranslated': False,
                'name': gettext('de'),
                'redirect_on_fallback': True,
            },
        ],
    },
    'ALDRYN_BOILERPLATE_NAME': 'legacy',
    # add aldryn_apphook_reload so that pages would be restored on apphook
    # reload.
    'MIDDLEWARE_CLASSES': [
        'aldryn_apphook_reload.middleware.ApphookReloadMiddleware',
        'django.middleware.http.ConditionalGetMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.doc.XViewMiddleware',
        'django.middleware.common.CommonMiddleware',
        'cms.middleware.language.LanguageCookieMiddleware',
        'cms.middleware.user.CurrentUserMiddleware',
        'cms.middleware.page.CurrentPageMiddleware',
        'cms.middleware.toolbar.ToolbarMiddleware'
    ],
    'STATICFILES_FINDERS': [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        # important! place right before django.contrib.staticfiles.finders.AppDirectoriesFinder  # NOQA
        'aldryn_boilerplates.staticfile_finders.AppDirectoriesFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    ],
    'TEMPLATE_CONTEXT_PROCESSORS': (
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.i18n',
        'django.core.context_processors.debug',
        'django.core.context_processors.request',
        'django.core.context_processors.media',
        'django.core.context_processors.csrf',
        'django.core.context_processors.tz',
        'sekizai.context_processors.sekizai',
        'django.core.context_processors.static',
        'cms.context_processors.cms_settings',
        'aldryn_boilerplates.context_processors.boilerplate'
    ),
    'TEMPLATE_LOADERS': (
        'django.template.loaders.filesystem.Loader',
        # important! place right before django.template.loaders.app_directories.Loader  # NOQA
        'aldryn_boilerplates.template_loaders.AppDirectoriesLoader',
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.eggs.Loader'
    )
    # 'EMAIL_BACKEND': 'django.core.mail.backends.locmem.EmailBackend',
}


def run():
    from djangocms_helper import runner
    runner.cms('aldryn_jobs')

if __name__ == "__main__":
    run()
