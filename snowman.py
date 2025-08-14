import game_logic
import ascii_art


def main():
    while True:
        game_logic.play_game()

        if not game_logic.confirm_replay():
            break


if __name__ == "__main__":
    main()
