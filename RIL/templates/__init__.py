from pathlib import Path

from jinja2 import Environment, FileSystemLoader

directory = Path(__file__).parent
engine = Environment(loader=FileSystemLoader(directory))
