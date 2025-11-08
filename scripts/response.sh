# response.ps1
# Takes action based on anomaly detection: BLOCK_IP or RESTART_SERVICE
# Usage example: .\response.ps1 -Action BLOCK_IP -Target "192.168.0.10"

param (
    [Parameter(Mandatory = $true)][string]$Action,
    [Parameter(Mandatory = $true)][string]$Target
)

switch ($Action) {
    "BLOCK_IP" {
        # Using Windows Firewall to block IP
        New-NetFirewallRule -DisplayName "Block IP $Target" -Direction Inbound -RemoteAddress $Target -Action Block
        Add-Content "C:\logs\incident_response.log" "$(Get-Date): BLOCK_IP performed on $Target"
    }
    "RESTART_SERVICE" {
        Restart-Service -Name $Target -Force
        Add-Content "C:\logs\incident_response.log" "$(Get-Date): RESTART_SERVICE performed on $Target"
    }
    default {
        Write-Output "Unknown action: $Action"
    }
}
