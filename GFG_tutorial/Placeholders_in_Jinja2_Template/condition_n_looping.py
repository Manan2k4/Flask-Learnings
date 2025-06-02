from jinja2 import Environment, FileSystemLoader

# Setup Jinja2 environment and tell it where to look for templates
env = Environment(loader=FileSystemLoader('condition_n_looping'))

# Load the main template (which extends base.html)
template = env.get_template('index_template.html')

# Variables to pass
name = 'Manan'
email = 'Manan@example.com'
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Render the template with values
rendered_form = template.render(pl_name=name, pl_email=email, numbers=numbers)

# Write the output to an HTML file
with open('condition_n_looping/index.html', 'w') as output:
    output.write(rendered_form)