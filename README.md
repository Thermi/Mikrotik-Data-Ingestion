# Mikrotik Data Ingestion into Elasticsearch

These files are works I created based on other people's contributions, but largely my own work to integrate the firewall logs of Mikrotik devices into Elasticsearch

Because I only use the firewall rules, those are the only ones I adapted and fixed for the new features (connection tracking state, packet mark, protocol flags) or log formats (BSD format with <prio/facility>$DATE $PREFIX format)

# Credit
- Most of the patterns from the mikrotik_fw_ingest pipeline are from frap (https://github.com/frap/logstash/blob/master/patterns/mikrotik)

