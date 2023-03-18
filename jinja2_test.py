from jinja2 import Environment,FileSystemLoader

env = Environment(loader = FileSystemLoader('./jinja2_templates'))
templ = env.get_template('config.j2')



list_info = {'int_face':'GigabitEthernet0/44', 'desc':'To-xxxx', 'int_address':'49.1.1.1','next_address':'49.1.1.2','net_area':'1'}

result = templ.render(list_info)
print(result)