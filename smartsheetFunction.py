from pprint import pprint
import ast
import smartsheet
from datetime import date, datetime

class ssActions():
    SHEET_ID = "YOUR SHEET ID"
    TOKEN = "YOUR-SMARTSHEET-ACCESS-TOKEN"

    ss_client = smartsheet.Smartsheet(TOKEN)
    sheet = ss_client.Sheets.get_sheet(SHEET_ID)

    print(sheet._total_row_count._value)

    def add_row(self, cluster_mapping, zombie_result):
        row_a = smartsheet.models.Row()
        row_a.to_top = True
        for k,v in cluster_mapping.items():
            row_a.cells.append({
                "column_id": v,
                "value": str(zombie_result.get(k)),
                "strict": False
        })

        response = self.ss_client.Sheets.add_rows(self.SHEET_ID,[row_a])
        print(response)