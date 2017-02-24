from sloth.conf.default_config import LABELS
'''
put all the code to the end of the sloth.conf.default_config except "from sloth.conf.default_config import LABELS"
http://sloth.readthedocs.io/en/latest/configuration.html#labels
'''

MYLABELS = (
    {
        'attributes':{
            'class':    'a',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     'sloth.items.RectItem',
        'hotkey':   'a',
        'text':     'A', 
    },
    {
        'attributes':{
            'class':    'b',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     'sloth.items.RectItem',
        'hotkey':   'b',
        'text':     'B', 
    },
    {
        'attributes':{
            'class':    'c',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     'sloth.items.RectItem',
        'hotkey':   'c',
        'text':     'C', 
    },
    {
        'attributes':{
            'class':    'd',
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     'sloth.items.RectItem',
        'hotkey':   'd',
        'text':     'D', 
    },
)

LABELS += MYLABELS
