# task-desk-python

## Tecnologias
Eu faria em Python usando:

PySide6 (interface gráfica moderna baseada em Qt)
json (armazenamento inicial)
pathlib (manipulação de arquivos)
winshell ou winreg (inicialização com o Windows)
plyer ou winotify (notificações)
PyInstaller (gerar um .exe)

O PySide6 é uma ótima escolha porque produz interfaces mais profissionais do que Tkinter e é bastante usado em aplicações desktop.



## ANTES DE TUDO
Data
Adicionar:
Prazo:
12/07/2026
Não precisa validar a data no começo.

Pesquisa
Pesquisar: Python
Resultado:
[ ] Estudar Python
[ ] Fazer curso de Python

Ordenação
Ordenar por:
prioridade
ordem alfabética
concluídas primeiro
não concluídas primeiro

Estatísticas
Mostrar:
Total: 20
Concluídas: 14
Pendentes: 6
70% concluídas



## Ordem
Eu seguiria algo como esta ordem:

Refatorar o código
    Separar em arquivos (main.py, storage.py, tasks.py, settings.py, etc.). (FEITO)
    Criar funções pequenas e bem definidas.
    Evitar código repetido.

Adicionar funcionalidades
    Editar o título de uma tarefa.
    Desmarcar uma tarefa como concluída.
    Filtrar (todas, pendentes, concluídas).
    Pesquisar tarefas por nome.
    Ordenar tarefas.
    Confirmar antes de excluir.
    Validar entradas do usuário.

Melhorar a estrutura
    Criar um menu mais organizado.
    Separar lógica de negócio da interface de terminal.
    Usar tratamento de exceções (try/except).

Só depois disso eu partiria para uma interface gráfica.






## (IMCOMPLETO) Funcionalidades intermediárias
Depois que o básico estiver funcionando:

Prioridade ( 🔴 Alta 🟡 Média 🟢 Baixa )
Categorias ( Faculdade, Trabalho, Pessoal, Academia )
Data de vencimento - Entregar trabalho 15/07/2026
Barra de pesquisa
Ordenar por - prioridade - data - ordem de criação
Favoritos



## Funcionalidades legais
Essas deixam o aplicativo bem profissional.

Inicializar junto com o Windows
O programa inicia automaticamente quando o usuário faz login.
Você aprenderá a usar:

pasta Startup
Registro do Windows
ou Agendador de Tarefas



## Notificações
Se uma tarefa vencer:

⚠ Trabalho de Banco de Dados
Vence hoje às 18:00



## Tema claro e escuro 
Guardar a preferência do usuário.



## Atalhos
Ctrl + N
Nova tarefa

Ctrl + F
Pesquisar

Delete
Excluir

Ctrl + S
Salvar



## Estatísticas
Hoje
✔ 12 concluídas
❌ 3 pendentes

Taxa
80%



## Calendário
Visualizar tarefas por dia.



## Histórico
Concluídas

05/07
✔ Academia

06/07
✔ Comprar arroz

07/07
✔ Trabalho de Python





## Desafios extras

Quando terminar, você pode adicionar recursos que destacam bastante o projeto:

Sincronização com um servidor ou nuvem.
Contas de usuário.
Sincronização entre computador e celular.
Anexar arquivos às tarefas.
Repetição automática (diária, semanal, mensal).
Widget para a área de trabalho.
Temporizador Pomodoro integrado.
Backup automático.
Exportar e importar tarefas.
Tags personalizadas.
Interface com animações.

Esse projeto é excelente para montar portfólio, porque demonstra domínio de interface gráfica, persistência de dados, organização de código, recursos específicos do sistema operacional e empacotamento de aplicações. Se você documentar bem o projeto e publicá-lo no GitHub, ele passa uma imagem muito mais completa do que um simples CRUD de console.




## Commits

tipo: descrição
feat	    Nova funcionalidade	                            feat: add task completion
fix	        Corrigir um bug	                                fix: prevent empty tasks from being added
refactor	Melhorar o código sem mudar o comportamento	    refactor: simplify menu logic
style	    Apenas formatação (espaços, indentação)	        style: format code with black
docs	    Documentação                                    docs: add installation instructions
test	    Testes	                                        test: add unit tests for task manager
chore	    Coisas de manutenção                            chore: add .gitignore

Você criou o projeto
feat: initialize todo list project

Criou o menu principal
feat: add main menu

Implementou adicionar tarefas
feat: implement task creation

Agora salva as tarefas em arquivo
feat: save tasks to JSON file

Mudou toda a organização do código
refactor: separate menu into functions

Corrigiu um erro
Antes:
IndexError ao completar tarefa
Commit:
fix: handle invalid task index