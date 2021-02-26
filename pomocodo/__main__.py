import click
from pomocodo.pomocodo import PomoCodo

@click.command()
def main():
    CT = PomoCodo()
    CT.main()

if  __name__ == "__main__":
    main()