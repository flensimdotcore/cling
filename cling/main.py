import argparse
from app.trainer import Trainer

def main():
    parser = argparse.ArgumentParser(prog="cling", description="CLI commands training utility")
    parser.add_argument("--bank", choices=["git"], required=True, help="Choose a commands bank")
    parser.add_argument("--difficulty", choices=["easy", "medium", "hard"], default="medium", help="Choose a difficulty")
    parser.add_argument("--repeat", type=int, default=5, help="Amount of questions in session")

    args = parser.parse_args()

    trainer = Trainer(args.bank, args.difficulty)

    trainer.start_session(args.repeat)

if __name__ == "__main__":
    main()