import click
from codingtimer.codingtimer import CodingTimer

@click.command()
def main():
    CT = CodingTimer()
    CT.main()

if  __name__ == "__main__":
    main()