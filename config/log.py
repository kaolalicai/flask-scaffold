import os
import logging
import logging.config
from logging.handlers import TimedRotatingFileHandler
logConfig = {
    'version': 1,
    'formatters': {
        'simpleFormatter': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s.%(msecs)d|#|<%(levelname)s>|#|%(filename)s.%(module)s.%(lineno)d|#|%(funcName)s|#|%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'consoleHandlerFlaskError': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'WARNING',
            'formatter': 'simpleFormatter',
            'filename': './log/' + os.environ.get('PROJECT_NAME', 'flask-docker-scaffold')+'_flask_error.log',
            'when': 'D',
        },
        'consoleHandlerError': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'WARNING',
            'formatter': 'simpleFormatter',
            'filename': './log/' + os.environ.get('PROJECT_NAME', 'flask-docker-scaffold')+'_error.log',
            'when': 'D',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
        },
        'consoleHandlerFlaskBasic': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'INFO',
            'formatter': 'simpleFormatter',
            'filename': './log/' + os.environ.get('PROJECT_NAME', 'flask-docker-scaffold')+'_flask_basic.log',
            'when': 'D',
        },
        'consoleHandlerBasic': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'INFO',
            'formatter': 'simpleFormatter',
            'filename': './log/' + os.environ.get('PROJECT_NAME', 'flask-docker-scaffold')+'_basic.log',
            'when': 'D',
        },
    },
    'loggers': {
        'gunicorn.error': {
            'propagate': 1,
            'handlers': ['consoleHandlerError'],
            'qualname': 'gunicorn.error'
        },
        'gunicorn.access': {
            'propagate': 0,
            'handlers': ['consoleHandlerBasic'],
            'qualname': 'gunicorn.access'
        },
        'flask.error': {
            'propagate': 1,
            'handlers': ['consoleHandlerFlaskError'],
            'qualname': 'gunicorn.error'
        },
        'flask.base': {
            'propagate': 0,
            'handlers': ['consoleHandlerFlaskBasic'],
            'qualname': 'flask.base'
        },
        'root': {
            'handlers': ['console']
        },
    },
    'root': {
        'level': 'DEBUG',
        'loggers': ['root', 'gunicorn.access', 'flask.base', 'gunicorn.error', 'flask.error']
    },
}
