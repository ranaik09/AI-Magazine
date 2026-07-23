from pydantic import BaseModel, Field


class ReviewFinding(BaseModel):
    severity: str = Field(description="low, medium, or high")
    file_path: str = Field(description="Path of the file where issue was found")
    summary: str = Field(description="Short issue summary")
    recommendation: str = Field(description="Suggested remediation")


class ReviewResult(BaseModel):
    status: str = Field(description="pass or fail")
    findings: list[ReviewFinding] = Field(default_factory=list)
