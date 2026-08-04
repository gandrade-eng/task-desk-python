# Aqui eu faria as classes do projeto.

# Depois pode adicionar:
# data de criação
# prioridade
# categoria
# prazo
# descrição

class Task:
    def __init__(self, id, title, completed, date, time, description):
        self.id = id
        self.title = title
        self.completed = completed
        self.date = date
        self.time = time
        self.description = description