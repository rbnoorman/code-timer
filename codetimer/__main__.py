import click
from codetimer.codetimer import CodeTimer

@click.command()
def main():
    CT = CodeTimer()
    CT.main()

if  __name__ == "__main__":
    main()