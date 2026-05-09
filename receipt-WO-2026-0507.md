huggingface-cli login
huggingface-cli upload <YOUR_ORG>/<YOUR_REPO> \
    ./receipt-WO-2026-0507.md \
    receipt-WO-2026-0507.md \
    --repo-type dataset \
    --commit-message "Upload Transaction Receipt for WO-2026-0507-BR-001"