from dataclasses import dataclass
import datetime

todos = []


@dataclass
class Todo:
    title: str
    date: datetime
    isCompleted: bool = False


def add(title, date=None):
    title = title.replace('b', 'bbb').replace('B', 'Bbb')
    if date is None:
        date = datetime.date.today()
    elif isinstance(date, str):
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    todos.append(Todo(title, date))


def get_all():
    return todos


def get(index):
    return todos[index]


def update(index):
    todos[index].isCompleted = not todos[index].isCompleted
