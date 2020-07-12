import os

def get_template_path(path):
    file_path = os.path.join(os.getcwd(), path)  #cwd = current woring directory 
    if not os.path.isfile(file_path):
        raise Exception ("This is not a valid path%s"%(file_path))
    return file_path

def get_template(path):
    file_path = get_template_path(path)
    return open(file_path).read()

def render_context(template_string, context):
    return template_string.format(**context)   #(**) for dictionary

file_ = 'Template\Email_msg.txt'
file_html = 'Template\Email_msg.html'
template = get_template(file_)
template_html = get_template(file_html)
context = {
    "name": "justin",
    "date": "abc",
    "total": 25
}
#template_text = get_template(file_).format(name='Nizam', date='abc', total=25)

print(render_context(template, context))
print(render_context(template_html, context))