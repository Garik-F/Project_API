def create(self, env_dir):
        env_dir = os.path.abspath(env_dir)
        context = self.ensure_directories(env_dir)
        self.create_configuration(context)
        self.setup_python(context)
        if not self.upgrade:
            self.setup_scripts(context)
            self.post_setup(context)
class ImprovedEnvBuilder(venv.EnvBuilder):
    
    def create(self, env_dir):
        """Overwrite create method (add more hooks)"""
        env_dir = path.abspath(env_dir)
        context = self.ensure_directories(env_dir)
        self.create_configuration(context)
        self.setup_python(context)
        if not self.upgrade:
            self.setup_scripts(context)
            self.post_setup(context)
        else:
            self.post_upgrade(context)

    def post_upgrade(self, context):
        pass