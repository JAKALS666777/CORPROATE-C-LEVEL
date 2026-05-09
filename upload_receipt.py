import argparse
import os
from huggingface_hub import HfApi

FILES_TO_UPLOAD = [
    ("transaction_receipt.md", "receipt-WO-2026-0507.md"),
    ("receipt-WO-2026-0507.md", "receipt-WO-2026-0507.md"),
]


def parse_args():
    parser = argparse.ArgumentParser(
        description="Upload receipt files to a Hugging Face dataset repository."
    )
    parser.add_argument(
        "repo_id",
        help="Hugging Face org/repo identifier, e.g. myorg/transaction-receipts",
    )
    parser.add_argument(
        "--token",
        help="Hugging Face API token. If omitted, HF_TOKEN environment variable will be used.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    token = args.token or os.getenv("HF_TOKEN")
    if not token:
        raise SystemExit("Hugging Face API token is required. Set HF_TOKEN or use --token.")

    api = HfApi()
    for local_path, repo_path in FILES_TO_UPLOAD:
        if not os.path.exists(local_path):
            raise SystemExit(f"Receipt file not found: {local_path}")

        print(f"Uploading {local_path} to {args.repo_id}/{repo_path}...")
        result = api.upload_file(
            path_or_fileobj=local_path,
            path_in_repo=repo_path,
            repo_id=args.repo_id,
            repo_type="dataset",
            token=token,
            commit_message="Upload Transaction Receipts for WO-2026-0507-BR-001",
        )
        print(f"Upload complete for {local_path}: {result}")


if __name__ == "__main__":
    main()
