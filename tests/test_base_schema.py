from marsh_schema_piapia import base_schema


def test_string():
    a = base_schema.BaseSchemaItem('username')
    ret = a.code_gen()
    assert ret == 'username = fields.String()'
