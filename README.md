## 根据一个json文件生成对应的marshmallow的schema文件

### 安装方法

```
pip install marsh_schema_piapia
```

### 使用实例

tmp.json文件内容如下
```
{
    "user_name": "liujinliu",
    "user_age": {
        "real": 33,
        "pub": [
            {"p0": 11, "p1": 12},
            {"p0": 11, "p1": 12}
        ]
    },
    "user_vip": true
}
```

将上述文件转化为对应的schema代码
```
json2marshschema --jsonfile=tmp.json --name=data --load=true
```

得到对应的代码如下:
```
class Pub(Schema):
    p0 = fields.Integer(load_from='p0')
    p1 = fields.Integer(load_from='p1')

class UserAge(Schema):
    pub = fields.Nested(pub, load_from='pub', many=True)
    real = fields.Integer(load_from='real')

class Data(Schema):
    user_age = fields.Nested(user_age, load_from='userAge', many=True)
    user_name = fields.String(load_from='userName')
    user_vip = fields.Integer(load_from='userVip')
```
