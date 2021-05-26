from starlette.templating import Jinja2Templates

from easy_going.utils.config import template_dir

templates = Jinja2Templates(directory=template_dir)
