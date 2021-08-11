def get_basic_data(data):
    entity = {
        'name': data['properties']['title'],
        'description': get_description(data['description']),
        'profile_image': get_profile_depiction(data['depictions']),
        'begin': get_date(data['when']['timespans'], 'start'),
        'end': get_date(data['when']['timespans'], 'end')
    }
    return entity


def get_description(data):
    if not data:
        return None
    desc = [i['value'] for i in data]
    return desc[0]


def get_profile_depiction(data):
    if not data:
        return None
    return [img['url'] for img in data if img['title'].startswith('profile_')]


def get_date(data, time):
    if not data:
        return None
    timestamp = [timespan[time]['earliest'] for timespan in data]
    return timestamp[0]


def get_relation_by_type(data, type):
    if not data:
        return None
    return [titles['label'] for titles in data if
            titles['type'] == type]


def get_relation_by_system_class(data, system_class):
    if not data:
        return None
    return [titles['label'] for titles in data if
            titles['relationSystemClass'] == system_class]


def get_type_label_by_hierarchy(data, hierarchy):
    if not data:
        return None
    return [titles['label'] for titles in data if
            titles['hierarchy'] == hierarchy]
    # Problem: what is, if Title is changed? I have no ID to get by
