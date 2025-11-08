# Streaming logs from multiple files and calling anomaly detector on parsed lines
Get-Content -Path "C:\path\to\log1.log" -Tail 0 -Wait | ForEach-Object {
    $line = $_
    # parse_logs.ps1 script (if any) can be invoked here or preprocess $line
    # Call Python anomaly detector and pass $line via stdin
    $proc = Start-Process -FilePath python -ArgumentList "ml\anomaly_detect.py" -NoNewWindow -RedirectStandardInput Pipe -PassThru
    $proc.StandardInput.WriteLine($line)
    $proc.StandardInput.Close()
    $proc.WaitForExit()
}
