import os
import shutil

def generate_project_structure(project_name):
    root_dir = os.path.join(os.getcwd(), project_name)

    # Create backend directory and files
    backend_dir = os.path.join(root_dir, 'backend')
    os.makedirs(backend_dir)
    shutil.copyfile('backend/Dockerfile', os.path.join(backend_dir, 'Dockerfile'))
    shutil.copyfile('backend/manage.py', os.path.join(backend_dir, 'manage.py'))
    shutil.copytree('backend/myapp', os.path.join(backend_dir, 'myapp'))
    shutil.copyfile('backend/requirements.txt', os.path.join(backend_dir, 'requirements.txt'))

    # Create frontend directory and files
    frontend_dir = os.path.join(root_dir, 'frontend')
    os.makedirs(frontend_dir)
    shutil.copyfile('frontend/Dockerfile', os.path.join(frontend_dir, 'Dockerfile'))
    shutil.copytree('frontend/public', os.path.join(frontend_dir, 'public'))
    shutil.copytree('frontend/src', os.path.join(frontend_dir, 'src'))
    shutil.copyfile('frontend/package.json', os.path.join(frontend_dir, 'package.json'))
    shutil.copyfile('frontend/package-lock.json', os.path.join(frontend_dir, 'package-lock.json'))

if __name__ == '__main__':
    project_name = input("Enter your project name: ")
    generate_project_structure(project_name)
    print("Project structure generated successfully!")
