from peewee import Model, CharField, FloatField, DateTimeField

class BaseModel(Model):
    class Meta:
        database = None

class Article(BaseModel):
    title = CharField()
    url = CharField(unique=True)
    author = CharField(null=True)
    date = DateTimeField(null=True)
    source = CharField(null=True)
    rank = FloatField(null=False)
