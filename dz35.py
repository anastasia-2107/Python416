from jinja2 import Environment, FileSystemLoader

list = ["Страница с домашним заданием", "Домашнее задание выполнено!!!"]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('dz35_main.html')
msg = tm.render(users=list, title="Домашнее задание")

print(msg)