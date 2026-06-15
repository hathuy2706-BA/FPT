#!/bin/bash

SCRIPT_DIR="/Users/hathuy/Documents/FPT-1/ruleai"
PID_FILE="$SCRIPT_DIR/sync_rules.pid"
LOG_FILE="$SCRIPT_DIR/sync_rules.log"

# Kiểm tra xem script đã chạy chưa
if [ -f "$PID_FILE" ]; then
    PID=$(cat "$PID_FILE")
    if ps -p "$PID" > /dev/null 2>&1; then
        echo "Rule sync watcher is already running with PID $PID."
        exit 0
    else
        echo "PID file exists but process is not running. Cleaning up..."
        rm "$PID_FILE"
    fi
fi

# Chạy python script trong background
echo "Starting rule sync watcher..."
nohup python3 "$SCRIPT_DIR/sync_rules.py" > "$LOG_FILE" 2>&1 &
NEW_PID=$!
echo "$NEW_PID" > "$PID_FILE"
echo "Rule sync watcher started in background with PID $NEW_PID."
echo "Logs are written to $LOG_FILE."
