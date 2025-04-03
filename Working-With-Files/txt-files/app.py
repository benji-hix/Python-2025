from pathlib import Path

# reading files

def create_path() -> Path:
    script_dir = Path(__file__).parent
    path = script_dir / 'monsters'

    path.mkdir(parents=True, exist_ok=True)

    path = path / 'lala-barina.txt'

    file = path.open('w')
    file.write('Temnoceran')
    file.close()

    return path

def read_file() -> None:
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
    except Exception as e:
        print(f'Unexpected error: {e}')
    return

monsters = ['Jin Dahaad', 'Rompoplo', 'Arkveld']

def open_via_context_manager():
    path = Path(__file__).parent / 'monsters' / 'monsters.txt'
    data = ['Lagiacrus', 'Gigginox', 'Bazelgeuse']

    with path.open('w') as file:
        for monster in data:
            file.write(monster + '\n')



def write_monsters_to_file(filename: str) -> None:
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

def append_to_file(filename: str) -> None:
    file = open(filename, 'a')

    for monster in final_monster:
        file.write('\n' + monster)

    file.close()
    return

# Context Managers --> auto closes

def main() -> None:
    open_via_context_manager()
    return

if __name__ == "__main__":
    main()