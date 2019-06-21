space_4 = '    '
space_8 = f'{space_4}{space_4}'


class BaseSchemaItem:

    SCHEMA_NAME = 'fields.String'

    def __init__(self, name, *, dump_to=None, load_from=None):
        self.name = name
        self.dump_to = dump_to
        self.load_from = load_from

    def code_gen(self):
        inner = []
        if self.dump_to:
            inner.append(f'dump_to={self.dump_to}')
        if self.load_from:
            inner.append(f'load_from={self.load_from}')
        inner_str = ', '.join(inner) if inner else ''
        return f'{self.name}={self.__class__.SCHEMA_NAME}({inner_str})'


class IntSchemaItem(BaseSchemaItem):

    SCHEMA_NAME = 'fields.Integer'


class BoolSchemaItem(BaseSchemaItem):

    SCHEMA_NAME = 'fields.Boolean'


class SchemaCodeGen:

    def __init__(self, name, item_list):
        self.name = name
        self.item_list = item_list

    def code_gen(self):
        inner_str = [f'class {self.name}(Schema):']
        for item in self.item_list:
            inner_str.append(f'{space_4}{item.code_gen()}')
        return '\n'.join(inner_str)


class NestSchemaItem():

    SCHEMA_NAME = 'fields.Nested'

    def __init__(self, name, sub_schema_code: SchemaCodeGen,
                 *, dump_to=None, load_from=None, many=True):
        self.name = name
        self.sub_schema_code = sub_schema_code
        self.dump_to = dump_to
        self.load_from = load_from
        self.many = many

    def code_gen(self):
        inner = [f'{self.sub_schema_code.name}']
        if self.dump_to:
            inner.append(f'dump_to={self.dump_to}')
        if self.load_from:
            inner.append(f'load_from={self.load_from}')
        inner.append(f'many={self.many}')
        inner_str = ', '.join(inner)
        return f'{self.name}={self.__class__.SCHEMA_NAME}({inner_str})'
