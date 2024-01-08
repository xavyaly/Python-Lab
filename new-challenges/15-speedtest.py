#!/usr/bin/python3

import speedtest 

d_speed = speedtest.Speedtest()

print(f"{d_speed.download()/800000:.2f}mb")

# Error
# ModuleNotFoundError: No module named 'speedtest'


# brew install speedtest-cli

# >>> import speedtest
# >>> d_speed = speedtest.Speedtest()
# >>> print(f"{d_speed.download()/800000:.2f}mb")
# 38.32mb