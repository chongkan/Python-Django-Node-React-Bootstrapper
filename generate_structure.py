import os

def generate_project_structure(project_name):
    root_dir = os.path.join(os.getcwd(), project_name)

    # Create backend directory and files
    backend_dir = os.path.join(root_dir, 'backend')
    os.makedirs(backend_dir)

    # Create backend files
    with open(os.path.join(backend_dir, 'Dockerfile'), 'w') as dockerfile:
        dockerfile.write('FROM python:3\n\n# Add your Dockerfile instructions here')

    with open(os.path.join(backend_dir, 'manage.py'), 'w') as manage_py:
        manage_py.write('# Your manage.py content here')

    os.makedirs(os.path.join(backend_dir, 'myapp'))
    with open(os.path.join(backend_dir, 'myapp', '__init__.py'), 'w') as init_py:
        init_py.write('# Your __init__.py content here')

    with open(os.path.join(backend_dir, 'myapp', 'settings.py'), 'w') as settings_py:
        settings_py.write('# Your settings.py content here')

    with open(os.path.join(backend_dir, 'myapp', 'urls.py'), 'w') as urls_py:
        urls_py.write('# Your urls.py content here')

    with open(os.path.join(backend_dir, 'myapp', 'wsgi.py'), 'w') as wsgi_py:
        wsgi_py.write('# Your wsgi.py content here')

    with open(os.path.join(backend_dir, 'requirements.txt'), 'w') as requirements_txt:
        requirements_txt.write('# Your requirements.txt content here')

    # Create frontend directory and files
    frontend_dir = os.path.join(root_dir, 'frontend')
    os.makedirs(frontend_dir)

    # Create frontend files
    with open(os.path.join(frontend_dir, 'Dockerfile'), 'w') as dockerfile:
        dockerfile.write('FROM node:latest\n\n# Add your Dockerfile instructions here')

    os.makedirs(os.path.join(frontend_dir, 'public'))
    with open(os.path.join(frontend_dir, 'public', 'index.html'), 'w') as index_html:
        index_html.write('<!-- Your index.html content here -->')

    with open(os.path.join(frontend_dir, 'public', 'favicon.ico'), 'w'):
        pass  # Empty file

    os.makedirs(os.path.join(frontend_dir, 'src', 'components'))
    with open(os.path.join(frontend_dir, 'src', 'App.js'), 'w') as app_js:
        app_js.write('// Your App.js content here')

    with open(os.path.join(frontend_dir, 'src', 'index.js'), 'w') as index_js:
        index_js.write('// Your index.js content here')

    with open(os.path.join(frontend_dir, 'src', 'components', 'Header.js'), 'w') as header_js:
        header_js.write('// Your Header.js content here')

    with open(os.path.join(frontend_dir, 'src', 'components', 'Footer.js'), 'w') as footer_js:
        footer_js.write('// Your Footer.js content here')

    with open(os.path.join(frontend_dir, 'package.json'), 'w') as package_json:
        package_json.write('{ "name": "your-package-name", "version": "1.0.0" }')

    with open(os.path.join(frontend_dir, 'package-lock.json'), 'w') as package_lock_json:
        package_lock_json.write('# Your package-lock.json content here')

if __name__ == '__main__':
    project_name = input("Enter your project name: ")
    generate_project_structure(project_name)
    print("Project structure generated successfully!")
