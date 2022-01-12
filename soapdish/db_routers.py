class BlogRouter:
    """
    A router to control all database operations on models in the
    blog application.
    """
    route_app_labels = {'blog'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read blog models go to blog_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'blog_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write blog models go to blog_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'blog_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the blog app is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the blog app only appear in the
        'blog_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'blog_db'
        return None