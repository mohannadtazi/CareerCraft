import pandas as pd
from crewai_tools import BaseTool


class ExcelWriteTool(BaseTool):
    name: str = "Excel Writer"
    description: str = "Write the DataFrame passed to it into an Excel file and return status."

    def _run(self, df: pd.DataFrame) -> str:
        # Save the DataFrame to an Excel file using Pandas
        file_path = "custom_cv.xlsx"
        df.to_excel(file_path, index=False)
        return f"Data written to {file_path}"

    class Config:
        arbitrary_types_allowed = True
