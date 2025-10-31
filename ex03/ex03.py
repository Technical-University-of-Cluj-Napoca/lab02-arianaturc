from datetime import datetime
import os

def smart_log(*args, **kwargs) -> None:

    message = ' '.join(str(arg) for arg in args)

    kw = {}
    for ks, vs in kwargs.items():
        ks = ks.lower()
        kw[ks] = vs

    level = kw.get('level', 'info')
    timestamp = kw.get('timestamp', True)
    filename = kw.get('save_to')
    color = kw.get('colored', True)
    date = kw.get('date', False)

    colors = {
        "info": "\033[94m",
        "debug": "\033[90m",
        "warning": "\033[93m",
        "error": "\033[91m",
    }

    labels = {
        "info": "INFO",
        "debug": "DEBUG",
        "warning": "WARNING",
        "error": "ERROR",
    }

    reset_code = "\033[0m"

    timestamp_str = ''
    if timestamp:
        now = datetime.now()
        if date:
            timestamp_str = now.strftime('%H:%M:%S') + ' '
        else:
            timestamp_str = now.strftime('%H:%M:%S') + ' '

    if color:
        c = colors.get(level)
    else:
        c = reset_code

    label = labels.get(level)
    log_message = f"{c}{timestamp_str}[{label}] {message}"
    print(log_message)

    if filename:
        try:
            dir = os.path.dirname(filename)
            if dir and not os.path.exists(dir):
                os.makedirs(dir)
            file_message = f"{timestamp_str}[{label}] {message}\n"
            with open(filename, 'w') as f:
                f.write(file_message)
        except Exception as e:
            print(f"{colors}['error'][ERROR] Failed to write to log file: {e}")



if __name__ == '__main__':
    username = 'alice'
    smart_log("System started successfully.", level="info")
    smart_log("User", username, "logged in.", level="debug", timestamp=True)
    smart_log("Low disk space detected!", level="warning", save_to="logs/system.log")
    smart_log("Model", "training", "failed!", level="error", colored=True, save_to="logs/errors.log")
    smart_log("Process end", level="info", colored=False, save_to="logs/errors.log")