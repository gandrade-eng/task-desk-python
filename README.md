# task-desk-python

Tecnologias

Eu faria em Python usando:

PySide6 (interface gráfica moderna baseada em Qt)
json (armazenamento inicial)
pathlib (manipulação de arquivos)
winshell ou winreg (inicialização com o Windows)
plyer ou winotify (notificações)
PyInstaller (gerar um .exe)

O PySide6 é uma ótima escolha porque produz interfaces mais profissionais do que Tkinter e é bastante usado em aplicações desktop.





(INCOMPLETO) Funcionalidades básicas (MVP) 
Comece com algo pequeno.

- Adicionar tarefa
- Remover tarefa
- Marcar tarefa como concluída
- Salvar automaticamente
- Carregar as tarefas ao abrir o programa



Funcionalidades intermediárias
Depois que o básico estiver funcionando:

Prioridade ( 🔴 Alta 🟡 Média 🟢 Baixa )
Categorias ( Faculdade, Trabalho, Pessoal, Academia )
Data de vencimento - Entregar trabalho 15/07/2026
Barra de pesquisa
Ordenar por - prioridade - data - ordem de criação
Favoritos



Funcionalidades legais
Essas deixam o aplicativo bem profissional.

Inicializar junto com o Windows
O programa inicia automaticamente quando o usuário faz login.
Você aprenderá a usar:

pasta Startup
Registro do Windows
ou Agendador de Tarefas



Minimizar para a bandeja (System Tray)
Em vez de fechar o programa: [X]

ele fica perto do relógio.
Exemplo:

🔔 Todo List

Ao clicar:
Abrir
Nova tarefa
Sair



Notificações
Se uma tarefa vencer:

⚠ Trabalho de Banco de Dados
Vence hoje às 18:00



Tema claro e escuro 
Guardar a preferência do usuário.



Atalhos
Ctrl + N
Nova tarefa

Ctrl + F
Pesquisar

Delete
Excluir

Ctrl + S
Salvar



Estatísticas
Hoje
✔ 12 concluídas
❌ 3 pendentes

Taxa
80%



Calendário
Visualizar tarefas por dia.



Histórico
Concluídas

05/07
✔ Academia

06/07
✔ Comprar arroz

07/07
✔ Trabalho de Python





Desafios extras

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