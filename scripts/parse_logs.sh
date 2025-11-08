# parse_logs.ps1
# Filters and parses log lines based on patterns (FAILED|ERROR|CRITICAL|WARNING)
# Usage: .\parse_logs.ps1 -InputLine "log line here"

param (
    [string]$InputLine
)

if ($InputLine -match "FAILED|ERROR|CRITICAL|WARNING") {
    # Basic field extraction similar to awk in original script
    $fields = $InputLine -split "\s+"
    # Customize according to your log format, example:
    $field1 = $fields[0]
    $field2 = $fields[1]
    $field3 = $fields[2]
    $field4 = if ($fields.Length -gt 5) { "$($fields[4]) $($fields[5])" } else { "" }
    $field5 = if ($fields.Length -gt 8) { $fields[8] } else { "" }

    # Output formatted as in awk print
    "$field1 $field2 $field3 $field4 $field5"
} else {
    # No output if pattern not matched
    return $null
}
