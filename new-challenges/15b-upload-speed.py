#!/usr/bin/python3

import speedtest 

u_speed = speedtest.Speedtest()

print(f"{d_speed.upload()/800000:.2f}mb")


# brew install speedtest-cli

# >>> import speedtest
# >>> u_speed = speedtest.Speedtest()
# >>> print(f'{u_speed.upload()/800000:.2f}mb')
# 4.20mb