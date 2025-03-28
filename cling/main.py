import argparse
from pathlib import Path

from app.trainer import Trainer, banks_prefix, categories_prefix


def main():
    banks_list = [file.stem for file in Path(banks_prefix).glob("*.yaml")]
    categories_list = [file.stem for file in Path(categories_prefix).glob("*.yaml")]
    parser = argparse.ArgumentParser(prog="cling", description="CLI commands training utility")
    parser.add_argument(
        "--bank",
        nargs="+",
        choices=banks_list,
        default=banks_list,
        help="Select specific command banks",
    )
    parser.add_argument(
        "--subbank",
        nargs="+",
        choices=["general"],
        default=["general"],
        help="Select specific command subbanks",
    )
    parser.add_argument(
        "--category",
        nargs="+",
        choices=categories_list,
        default="none",
        help="Select sets of banks based on their implications",
    )
    parser.add_argument(
        "--difficulty",
        nargs="+",
        choices=["easy", "medium", "hard"],
        default=["easy", "medium", "hard"],
        help="Choose difficulty levels",
    )
    parser.add_argument(
        "--language", choices=["en", "ru"], default="en", help="Choose an interface language"
    )
    parser.add_argument("--repeat", type=int, default=5, help="Amount of questions in session")

    args = parser.parse_args()

    trainer = Trainer(args.bank, args.difficulty, args.language, args.subbank, args.category)

    trainer.start_session(args.repeat)


if __name__ == "__main__":
    main()
