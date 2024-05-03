import platform
import cpuinfo

sysinfo = {
    "architecture": platform.machine(),
    "cpu": cpuinfo.get_cpu_info()['brand_raw'],
    "os": platform.system().capitalize()
}

uname = platform.uname()


def Main(args):
    return """
\x1b[38;5;27m     ((((            ((/((           (((,           .(((     \x1b[0m  fetchdist            
\x1b[38;5;27m  ((      ((      /((     ((       ((    ((       ((    ((   \x1b[0m  -------------------
\x1b[38;5;27m((          ((/ ((           (( ((          (( ((          ((\x1b[0m  %s              
\x1b[38;5;27m       (              /              *                       \x1b[0m  %s              
\x1b[38;5;27m     ((  ((         ((  ((         ((  ((         ((  ((     \x1b[0m  %s              
\x1b[38;5;27m  ((       ((    ((,      ((/   ((,      ((/   /((      (((  \x1b[0m  %s              
\x1b[38;5;27m((            (((            (((            (((            ((\x1b[0m  %s    
""" % (
        f"\x1b[38;5;27mOS\x1b[0m: Aquarity v1.0beta LTS {sysinfo['architecture']}",
        f"\x1b[38;5;27mHost\x1b[0m: {uname.node} on {sysinfo['os']}",
        "\x1b[38;5;27mShell\x1b[0m: aqx shell",
        "\x1b[38;5;27mDesktop\x1b[0m: No aquarity GUI",
        f"\x1b[38;5;27mCPU\x1b[0m: {sysinfo['cpu']}"
    )
