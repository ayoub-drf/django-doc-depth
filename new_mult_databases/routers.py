class MyRouter:
    def db_for_read(self, model, **hints):
        """
        This method is called for read operations (queries). It decides which database 
        to use for reading.
        """
        if model._meta.app_label == 'new_mult_databases':
            return 'secondary'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        This method is called for write operations (insert, update, delete). It decides 
        which database to use for writing.
        """
        if model._meta.app_label == 'new_mult_databases':
            return 'secondary'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        This method checks if a relation between two models is allowed.
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        This method decides which database to use for migrations.
        """
        if db == 'secondary':
            return app_label == 'new_mult_databases'
        return db == 'default'
