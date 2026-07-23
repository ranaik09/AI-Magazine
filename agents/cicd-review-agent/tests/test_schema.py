import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from schema import ReviewFinding, ReviewResult  # noqa: E402


def test_review_result_defaults():
    result = ReviewResult(status="pass")
    assert result.status == "pass"
    assert result.findings == []


def test_review_finding_model():
    finding = ReviewFinding(
        severity="high",
        file_path="agent.py",
        summary="Issue found",
        recommendation="Fix it",
    )
    assert finding.severity == "high"
