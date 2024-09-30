 # Récapitulatif de SNORT lors de ping venant de deux personnes

 
 
 ```
 sudo/bin/snort -i ens18 --daq-dir /usr/local/lib/daq_s3/lib/daq -c /etc/snort/snort.lua -R /etc/snort/rules/local.rules -A alert_fast -l /var/log/snort
[sudo] password for user:
--------------------------------------------------
o")~   Snort++ 3.2.2.0
--------------------------------------------------
Loading /etc/snort/snort.lua:
Loading snort_defaults.lua:
Finished snort_defaults.lua:
        ips
        binder
        wizard
        appid
        js_norm
        file_policy
        http2_inspect
        http_inspect
        ftp_data
        ftp_client
        ftp_server
        smtp
        port_scan
        gtp_inspect
        dce_http_server
        dce_http_proxy
        dce_smb
        stream
        stream_udp
        stream_ip
        stream_icmp
        stream_tcp
        stream_user
        stream_file
        arp_spoof
        back_orifice
        dns
        imap
        netflow
        normalizer
        pop
        rpc_decode
        sip
        ssh
        ssl
        telnet
        cip
        dnp3
        iec104
        mms
        modbus
        s7commplus
        dce_tcp
        dce_udp
        references
        classifications
        alert_fast
        alert_full
        output
        alerts
        decode
        active
        daq
        host_cache
        hosts
        network
        packets
        search_engine
        so_proxy
        file_id
        host_tracker
        trace
        process
Finished /etc/snort/snort.lua:
Loading file_id.rules_file:
Loading file_magic.rules:
Finished file_magic.rules:
Finished file_id.rules_file:
Loading rule args:
Loading /etc/snort/rules/local.rules:
Finished /etc/snort/rules/local.rules:
Finished rule args:
--------------------------------------------------
ips policies rule stats
              id  loaded  shared enabled    file
               0     220       0     220    /etc/snort/snort.lua
--------------------------------------------------
rule counts
       total rules loaded: 220
               text rules: 220
            option chains: 220
            chain headers: 2
--------------------------------------------------
port rule counts
             tcp     udp    icmp      ip
     any       0       0       1       0
   total       0       0       1       0
--------------------------------------------------
service rule counts          to-srv  to-cli
                  file_id:      219     219
                    total:      219     219
--------------------------------------------------
fast pattern groups
                to_server: 1
                to_client: 1
--------------------------------------------------
search engine (ac_bnfa)
                instances: 2
                 patterns: 438
            pattern chars: 2602
               num states: 1832
         num match states: 392
             memory scale: KB
             total memory: 71.2812
           pattern memory: 19.6484
        match list memory: 28.4375
        transition memory: 22.9453
appid: MaxRss diff: 3024
appid: patterns loaded: 300
--------------------------------------------------
pcap DAQ configured to passive.
Commencing packet processing
++ [0] ens18
^C** caught int signal
== stopping
-- [0] ens18
--------------------------------------------------
Packet Statistics
--------------------------------------------------
daq
                 received: 232
                 analyzed: 231
              outstanding: 1
          outstanding_max: 1
                    allow: 231
                 rx_bytes: 21850
--------------------------------------------------
codec
                    total: 231          (100.000%)
                 discards: 1            (  0.433%)
                      arp: 14           (  6.061%)
                      eth: 231          (100.000%)
                    icmp4: 214          ( 92.641%)
                     ipv4: 217          ( 93.939%)
                      tcp: 3            (  1.299%)
--------------------------------------------------
Module Statistics
--------------------------------------------------
appid
                  packets: 216
        processed_packets: 215
          ignored_packets: 1
           total_sessions: 3
--------------------------------------------------
arp_spoof
                  packets: 14
--------------------------------------------------
binder
              raw_packets: 15
                new_flows: 3
                 inspects: 18
--------------------------------------------------
detection
                 analyzed: 231
               hard_evals: 214
                   alerts: 214
             total_alerts: 214
                   logged: 214
--------------------------------------------------
ips_actions
                    alert: 214
--------------------------------------------------
port_scan
                  packets: 217
                 trackers: 7
--------------------------------------------------
search_engine
         qualified_events: 214
--------------------------------------------------
stream
                    flows: 3
--------------------------------------------------
stream_icmp
                 sessions: 2
                      max: 2
                  created: 2
                 released: 2
--------------------------------------------------
stream_tcp
                 sessions: 1
                      max: 1
                  created: 1
                 released: 1
             instantiated: 1
                   setups: 1
            data_trackers: 1
              segs_queued: 1
            segs_released: 1
                 max_segs: 1
                max_bytes: 64
         asymmetric_flows: 1
--------------------------------------------------
tcp
        bad_tcp4_checksum: 1
--------------------------------------------------
Appid Statistics
--------------------------------------------------
detected apps and services
              Application: Services   Clients    Users      Payloads   Misc       Referred
                  unknown: 1          0          0          0          0          0
--------------------------------------------------
Summary Statistics
--------------------------------------------------
process
                  signals: 1
--------------------------------------------------
timing
                  runtime: 00:00:53
                  seconds: 53.737369
                 pkts/sec: 4
o")~   Snort exiting
```