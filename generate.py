from jinja2 import Environment, PackageLoader, select_autoescape


env = Environment(
    loader=PackageLoader('conference', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)


@dataclass
class Speaker:
    firstname: str
    lastname: str


speakers = [
    Speaker('Kristian', 'Kersting')
]


template = env.get_template('base.html')
