from django.db import models
# from django.db.models import Lookup
# from django.db.models.fields import Field

from django.db.models import Lookup, Field, IntegerField


@Field.register_lookup
class NotEqualLookUP(Lookup):
    lookup_name = "not_equal"

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params

        return "%s <> %s" % (lhs, rhs), params
    
    
class CustomLike(Lookup):
    lookup_name = "custom_like"
    def __init__(self, lhs, rhs):
        # print(lhs)
        super().__init__(lhs, rhs)

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params

        sql = "%s LIKE %s" % (lhs, rhs)

        return sql, params
    
Field.register_lookup(CustomLike)


class Book(models.Model):
    name = models.CharField(max_length=100)
    num = models.IntegerField(default=-100)


    def __str__(self):
        return f"{self.name}"
    