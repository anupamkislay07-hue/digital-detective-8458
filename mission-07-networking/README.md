# Mission 07 – Networking

## 1. Mission Objective

Understand the core concepts that allow computers to communicate over networks—IP addresses, DNS, HTTP/HTTPS, and ports—and inspect network activity using macOS Terminal commands.

---

## 2. Task 7.1 – Core Networking Concepts

| Concept | What It Is / What It Does |
|---|---|
| **IP Address** | A numerical address (like `192.168.1.12` on a local Wi-Fi network, or a public IP on the internet) that identifies a device on a network so packets know where they're coming from and where to be routed. |
| **DNS** | The internet's phonebook—humans remember names like `github.com`, while networks route using IP addresses, so DNS translates human-readable domain names into IP addresses behind the scenes. |
| **HTTP vs. HTTPS** | HTTP sends data in plain text without encryption, whereas HTTPS wraps that traffic in TLS/SSL encryption (and verifies server identity), keeping passwords, messages, and browsing data private and tamper-resistant over the network. |
| **Ports** | Virtual numbered channels on a device that direct incoming network traffic to the right app or service. Port `80` is used for unencrypted HTTP web traffic; port `443` is used for encrypted HTTPS traffic. |

---

## 3. Task 7.2 – Network Diagnostic Commands

### `ifconfig | grep "inet "`

Prints IPv4 lines for all active network interfaces. `127.0.0.1` appears on `lo0` (the loopback / "this Mac" address), and a local network address (often starting with `192.168.` or `10.`) appears on the active Wi-Fi or Ethernet interface (`en0`, etc.).

### `ping google.com -c 4`

Sends 4 small packets to Google and prints each reply's sequence number, TTL, and round-trip time (RTT) in milliseconds, followed by packet loss percentage (`0.0% packet loss` when healthy) and min/avg/max latency statistics.

### `nslookup github.com`

Queries a DNS server for `github.com` and returns the resolver address used along with the resolved IPv4 (`A`) and/or IPv6 (`AAAA`) addresses for that domain.

### `curl -I https://github.com`

Fetches only the HTTP response headers (without downloading the full page body), showing status codes like `HTTP/2 200` (or a `301`/`302` redirect), along with server/security headers and content-type information.

---

## 4. Reflection

What stood out most is how many layers quietly hand off work—turning a domain name into an IP, aiming at a specific port, encrypting the payload, and bouncing packets across routers in milliseconds. Once you see `ping`, `nslookup`, and `curl` side by side, the "cloud" feels much more like concrete steps you can actually inspect.
