# DjangoManagementCommand

This Django project manages blog posts and provides a platform for users to view, create, and manage posts.

## Project Structure

- `post`: Contains models, views, URLs, and other app-related functionalities.
- `manage.py`: Django's management script.
- `requirements.txt`: File containing Python dependencies.

## `post/management/commands/example_command.py` - `example_command.py` this file name is commnad name if we change file name to `create_100_post_object.py` command name will be `python manage.py create_100_post_object`

## Features
- Custom management command for generating 100 posts

## Installation

1. Clone the repository:

    ```bash
    https://github.com/AvazovOgabek/DjangoManagementCommand.git
    cd DjangoManagementCommand
    ```

2. Set up a virtual environment (recommended):

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use: .\env\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Apply migrations:

    ```bash
    python manage.py migrate
    ```

2. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

3. Access the application at `http://localhost:8000`.

## Creating 100 Posts

To create 100 posts, you can use the custom management command provided:

```bash
python manage.py example_command
```
post/
├── my_app/
│ ├── init.py
│ ├── models.py
│ ├── management/
│ │ ├── init.py
│ │ └── commands/
│ │ ├── init.py
│ │ └── example_command.py
│ ├── views.py
│ ├── urls.py
│ ├── apps.py
│ ├── admin.py
│ └── ...
├── manage.py
└── requirements.txt