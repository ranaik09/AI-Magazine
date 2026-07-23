from agent import review_pull_request


def main() -> None:
    print("CI/CD Review Agent started.")
    result = review_pull_request("")
    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
