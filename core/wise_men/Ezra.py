class Ezra:
    def execute(self, task):
        return {'status': 'ok', 'result': f'Ezra handled: {task}'}

    def health_check(self):
        return True
