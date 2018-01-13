"""
参数验证: https://github.com/alecthomas/voluptuous
"""

from voluptuous import Schema, Required, All, Length


home_schema = Schema({
    Required('name'): All(str, Length(min=1))
})
