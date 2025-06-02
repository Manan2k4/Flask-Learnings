# import Template from jinja2 for passing the content
from jinja2 import Template

# variables that contain placeholder data
name='Manan'
email='Manan@example.com'

# Create one external form_template html page and read it
File = open('basic_html_render/index_template.html', 'r')
content = File.read()
File.close()

# Render the template and pass the variables
template = Template(content)
rendered_form = template.render(pl_name=name, pl_email=email)

# save the txt file in the form.html
output = open('basic_html_render/index.html', 'w')
output.write(rendered_form)
output.close()