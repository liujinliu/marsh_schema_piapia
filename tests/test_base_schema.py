from marsh_schema_piapia import base_schema


def test_string():
    a = base_schema.BaseSchemaItem('username')
    ret = a.code_gen()
    assert ret == 'username = fields.String()'


def test_int():
    a = base_schema.IntSchemaItem('user_age', dump_to='userAge')
    ret = a.code_gen()
    assert ret == "user_age = fields.Integer(dump_to='userAge')"  # NOQA
