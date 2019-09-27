#!/usr/bin/env python

import delegator as delg

def job():
    current_network = delg.run("iwgetid -r")
    current_network_out = current_network.out

    if((current_network_out.find("I-ON") != -1) or (current_network_out.find("ION") != -1)):
        ion_ap = 'nmcli -f ssid,bssid,signal,bars,freq,rate  dev wifi | grep -E \'ION|I-ON\' | sort -k5 -k6 -s -r | head -n 1 | awk \'{print $1} {print $2}\''
        output = delg.run(ion_ap)

        optimal_ssid = output.out.splitlines()[0]
        optimal_bssid = output.out.splitlines()[1]

        print(optimal_ssid + " " + optimal_bssid)

if __name__ == '__main__':
    job()