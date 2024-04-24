import click, requests
from requests.exceptions import RequestException
from utils import convtxt, convtable, convjson, tests
from random import randint
import friendlywords as friendlywords

API_URL = f"http://localhost:8085/api"

TODOS_URL = f"{API_URL}/todos"

@click.group()
def cli():
    pass

@click.command()
@click.option(
    "-f",
    type=click.Choice(["txt", "table", "json"]),
    default="json",
)
def get(format):
    try:
        response = requests.get(TODOS_URL)
        if response.status_code == 200:
            data = response.json()
            if format == "txt":
                click.echo(convtxt(data))
            elif format == "table":
                click.echo(convtable(data))
            elif format == "json":
                click.echo(convjson(data))
            return data
        else:
            click.echo(f"ERROR en llamada a la API: {response.status_code}")
    except RequestException as e:
        click.echo(f"ERROR: \n{e}")


@click.command()
@click.argument("txt")
def add(txt):
    try:
        response = requests.post(TODOS_URL, {"txt": txt})
        if response.status_code == 200:
            click.echo(f"Añadido con éxito el TODO -> {txt}")
        else:
            click.echo(f"ERROR en llamada a la API: {response.status_code}")
    except RequestException as e:
        click.echo(f"ERROR: \n{e}")


@click.command()
@click.argument("id")
def delete(id):
    try:
        url = f"{TODOS_URL}/{id}"
        response = requests.delete(url)
        click.echo(f"Eliminado con éxito el TODO -> {id}")
        if response.status_code != 200:
            click.echo(f"ERROR en llamada a la API: {response.status_code}")
    except RequestException as e:
        click.echo(f"ERROR: \n{e}")


@click.command()
def tests():
    click.echo("\n ### TESTS ###")

    num = randint(10, 100)
    generadosaleatoriamente = [friendlywords.generate(3) for _ in range(num)]

    context = click.get_current_context()

    click.echo(f"\n 1. Create a random number of Todos between 10 and 100")
    for i in generadosaleatoriamente:
        context.invoke(add, txt=i)

    click.echo("\n 2. Get all the Todos in JSON format")
    context.invoke(get, format="json")

    click.echo("\n 3. Get all the Todos in text format")
    context.invoke(get, format="txt")

    click.echo("\n 4. Get all the Todos in table format")
    stored_todos = context.invoke(get, format="table")

    click.echo("\n 5. Clean all the stored Todos")
    for i in stored_todos:
        context.invoke(delete, id=i.get("_id"))


cli.add_command(get)
cli.add_command(add)
cli.add_command(delete)
cli.add_command(tests)


if __name__ == "__main__":
    cli()
