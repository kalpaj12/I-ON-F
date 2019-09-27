#!/usr/bin/env python

import os
import delegator as delg
import subprocess
import commands


def job():
    current_network = delg.run("iwgetid -r")
    current_network_out = current_network.out

    if((current_network_out.find("I-ON") != -1) or (current_network_out.find("ION") != -1)):
        ion_ap = 'nmcli -f ssid,bssid,signal,bars,freq,rate,in-use  dev wifi | grep -E \'ION|I-ON\' | sort -k5 -k6 -s -r | head -n 1 | awk \'{print $1} {print $2} {print $9} \''
        output = delg.run(ion_ap)

        optimal_ssid = output.out.splitlines()[0]
        optimal_bssid = output.out.splitlines()[1]
        isStar = output.out.splitlines()[2]

        print(optimal_ssid + " " + optimal_bssid)

        # Cleanup ssid's
        if(current_network_out.find(optimal_bssid) == -1 and isStar != "*"):
            res = commands.getstatusoutput("nmcli -t -f TYPE,UUID,NAME con")
            lines = res[1].split('\n')
            for line in lines:
                parts = line.split(":")
                if (parts[0] == "802-11-wireless" and parts[2].find(optimal_ssid) != -1):
                    os.system("nmcli connection delete uuid " + parts[1])

        # connect to optmised_bssid here

        else:
            print("on optmised connection")


if __name__ == '__main__':
    job()
