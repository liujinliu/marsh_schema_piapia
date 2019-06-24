from marsh_schema_piapia import base_schema


def test_string():
    a = base_schema.BaseSchemaItem('username')
    ret = a.code_gen()
    assert ret == 'username = fields.String()'


def test_int():
    a = base_schema.IntSchemaItem('user_age', dump_to='userAge')
    ret = a.code_gen()
    assert ret == "user_age = fields.Integer(dump_to='userAge')"  # NOQA


def test_bool():
    a = base_schema.BoolSchemaItem('user_vip', dump_to='userVip')
    ret = a.code_gen()
    assert ret == "user_vip = fields.Boolean(dump_to='userVip')"  # NOQA


def test_schema_code_gen():
    a = base_schema.BaseSchemaItem('username')
    b = base_schema.IntSchemaItem('user_age', dump_to='userAge')
    c = base_schema.BoolSchemaItem('user_vip', dump_to='userVip')
    item_list = [a, b, c]
    schema_code_gen = base_schema.SchemaCodeGen('UserInfo', item_list)
    assert(schema_code_gen.code_gen() ==
           ('class UserInfo(Schema):\n'
            '    username = fields.String()\n'
            "    user_age = fields.Integer(dump_to='userAge')\n"
            "    user_vip = fields.Boolean(dump_to='userVip')"))


def test_nested_schema():
    item0 = base_schema.BaseSchemaItem('username')
    item1 = base_schema.IntSchemaItem('user_age', dump_to='userAge')
    schema_code_gen = base_schema.SchemaCodeGen('UserInfo', [item0, item1])
    a = base_schema.NestSchemaItem('retInfo', schema_code_gen, many=False)
    assert(a.code_gen() == 'retInfo = fields.Nested(UserInfo, many=False)')
