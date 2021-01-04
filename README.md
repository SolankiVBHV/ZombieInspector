# ZombieInspector
CLI Crawler that logs into UCM nodes to check for zombie process and add the result in Smartsheet as well update in a Cisco Teams chat. 

Note:
1. Add details for variable `SHEET_ID` and `token` in `smartsheetFunction.py`.
2. Add Teams bot token for `access_token` and Teams room ID for `roomId`.
3. This tool would need LAN access to the nodes that needs monitoring and internet access(either direct or via proxy) to update the Smartsheet and Teams bot. 