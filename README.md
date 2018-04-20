# Google Spreadhsheet Api - Append

A [Supercode](http://gosupercode.com) function that appends google spreadsheet data.

## Server Usage

[Supercode](http://gosupercode.com) SDK will be available after the launch.

```
import supercode

service_account_json = {}
SUPERCODE_API_KEY = "your-supercode-api-key"

response = supercode.call(
    "append-to-sheet",
    SUPERCODE_API_KEY,
    range="Sheet1!A:B",
    value_list=[["Test", "Test"]],
    service_account_json=service_account_json,
    major_dimension, # not required default value is `ROWS`
    value_input_option # not required default value is `RAW`
)

print response
```


**Note:** Supercode has not been launched yet. This is for internal testing only.
