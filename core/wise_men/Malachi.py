class Malachi:
    def execute(self, task):
        return {'status': 'ok', 'result': f'Malachi processed: {task}'}

    def health_check(self):
        return True
