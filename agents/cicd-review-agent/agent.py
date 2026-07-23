from schema import ReviewFinding, ReviewResult


def review_pull_request(pr_diff: str) -> ReviewResult:
    findings: list[ReviewFinding] = []

    if not pr_diff.strip():
        findings.append(
            ReviewFinding(
                severity="low",
                file_path="N/A",
                summary="Empty diff provided",
                recommendation="Provide PR diff content to run checks.",
            )
        )

    status = "fail" if findings else "pass"
    return ReviewResult(status=status, findings=findings)
