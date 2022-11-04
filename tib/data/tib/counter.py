from flask_babel import lazy_gettext as _l

counter = {
    'tib_volumes': {
        'count': 13,
        'description': _l('TIB Volumes Published'),
        'icon': 'bi-book-fill'
    },
    'tib_making': {
        'count': 5,
        'description': _l('TIB Volumes in Progress'),
        'icon': 'bi-pencil-fill'
    },
    'article': {
        'count': 136,
        'description': _l('Articles published since 2004'),
        'icon': 'bi-body-text'
    },
    'presentations': {
        'count': 235,
        'description': _l('Presentations held since 2006'),
        'icon': 'bi-chat-left-text-fill'
    },
    'books': {
        'count': 16,
        'description': _l('Books published since 2006'),
        'icon': 'bi-book-half'
    },
    'pictures': {
        'count': 100000,
        'description': _l('and more pictures shot since 1966'),
        'icon': 'bi-camera-fill'
    },
    'travels': {
        'count': 68,
        'description': _l('and more travels accomplished'),
        'icon': 'bi-send-fill'
    }
}
