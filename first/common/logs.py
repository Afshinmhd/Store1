import logging


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':{
        'verbose':{
            'foramt':'{asctime} {project} {levelname} FILE {pathname}, line {lineno},'
                      '{message}',
            'style': '{'
    },
    },
        
    'handlers': {
        'console':{
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        }
    },
    'root':{
        'handler': ['console'],
        'level': 'INFO',
    }

}