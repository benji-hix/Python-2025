from pathlib import Path

# reading files

def create_path():
    script_dir = Path(__file__).parent
    path = script_dir / 'monsters'

    path.mkdir(parents=True, exist_ok=True)

    path = path / 'lala-barina.txt'

    file = path.open('w')
    file.write('Temnoceran')
    file.close()

    return path

def read_file():
    path = Path(__file__).parent
    selected_file = input('What monster are you looking for?')
    path = path / 'Monsters' / selected_file
    
    try:
        file = path.open('r')
        file.seek(0,0)
        lines = file.readlines()
        for line in lines:
            print(line)
        file.close()
    except FileNotFoundError as error:
        print(f'{path} does not exist.')

    return

monsters = ['Jin Dahaad', 'Rompoplo', 'Arkveld']

def write_monsters_to_file(filename: str):
    # open file
    file = open(filename, 'w+')

    # write to file
    for monster in monsters[:-1]:
        file.write(monster + '\n')
    file.write(monsters[-1])

    # close
    file.close()
    return

final_monster = ['Xo Shia']

def append_to_file(filename: str):
    file = open(filename, 'a')

    for monster in final_monster:
        file.write('\n' + monster)

    file.close()
    return


def main():
    create_path()
    read_file()
    return

if __name__ == "__main__":
    main()