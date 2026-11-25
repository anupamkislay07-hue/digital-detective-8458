# Mission 07 — Computer networks

## 1. Task / objective

Explain the basic network types and concepts (LAN, MAN, WAN, DNS, router, protocol, packet switching, client–server), observe connectivity and DNS lookups from the Terminal with privacy-safe output, and describe in numbered steps what happens when a website opens.

## 2. Work completed

### Task 7.1 — Network concepts

| Concept | Explanation in my own words | Example |
|---|---|---|
| **LAN** | Local Area Network — a small network covering one place, where devices talk directly to each other and share one connection outward. | My home Wi-Fi connecting a laptop, phone and printer. |
| **MAN** | Metropolitan Area Network — a larger network spanning a city or a big campus, joining several local networks together. | A university campus network covering many buildings across a city. |
| **WAN** | Wide Area Network — a network over very large distances, built by connecting many smaller networks through provider links. | The internet itself; a company linking offices in two countries. |
| **DNS** | Domain Name System — the internet's phonebook: it converts a human-friendly name into the IP address machines actually route to. | Typing `example.com` returns `104.20.23.154`. |
| **Router** | A device that joins different networks and forwards packets between them, choosing the next hop toward the destination. | The home Wi-Fi router sending a request from my laptop out to my ISP. |
| **Protocol** | An agreed set of rules for how data is formatted, addressed, sent and acknowledged, so two different systems can understand each other. | HTTP for web pages, TCP for reliable delivery, IP for addressing. |
| **Packet switching** | Data is cut into small packets that each carry addressing information, may travel by different routes, and are reassembled in order at the destination. | One web page arriving as many packets, some via different paths. |
| **Client–server** | One program (the client) asks for something, and another (the server) holds the data and answers the request. | My browser (client) requesting a page from a web server. |

### Task 7.2 — Connectivity and DNS observations

**Connectivity test** — `ping -c 4 example.com`:

```text
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 4.876/38.250/93.148/35.902 ms
```

**DNS lookup** — `nslookup example.com`:

```text
Address:        8.8.8.8#53

Non-authoritative answer:
Name:   example.com
Address: 104.20.23.154
Name:   example.com
Address: 172.66.147.243
```

**HTTP response headers** — `curl -sI https://example.com`:

```text
HTTP/2 200
content-type: text/html; charset=utf-8
server: cloudflare
```

Answers:

- **What a connectivity test checks.** `ping` sends small ICMP packets to a host and reports whether replies come back, how many were lost, and how long the round trip took. It tells me whether the destination is reachable and whether the link is fast and stable — it does not test whether a specific website or application works.
- **What a DNS lookup displays.** It shows which DNS server answered, the domain that was queried, and the address(es) mapped to that name. `nslookup` returned two IPv4 addresses for `example.com` plus the resolver used (`8.8.8.8` port `53`), which is how a single name can point at several servers for load balancing.
- **The role of DNS when I type a website name.** The browser cannot route to a name, only to an IP address, so it asks a DNS resolver to translate `example.com` into an address. Only then can it open a connection. If DNS fails, the site appears unreachable even though the network itself is fine.

No local IP address, Wi-Fi name, hostname or device name is recorded here; only public, generic `example.com` results are shown.

### Task 7.3 — What happens when a website opens

1. **I type the URL** into the browser, which splits it into the protocol (`https`), the host name (`example.com`) and the path.
2. **The client asks DNS** to resolve the host name, sending a query to the configured resolver, which replies with the server's IP address.
3. **The client opens a connection** to that IP address on port `443`, the standard HTTPS port. A TCP handshake establishes a reliable connection, and TLS negotiates encryption so the traffic cannot be read or altered in transit.
4. **My router forwards the packets** toward the destination. Packet switching means the request is broken into packets that may take different paths across several routers before reaching the server's network.
5. **The server receives the request** over HTTP, a protocol that defines how the request and response are formatted, and works out which page or resource is being asked for.
6. **The server sends the response** — a status line such as `HTTP/2 200`, headers describing the content type, and the HTML body — back through the network to my IP address.
7. **The browser renders the page.** It parses the HTML, requests the extra files (CSS, images, scripts), and paints the result on screen. DNS, connection, request and response together are the client–server exchange I actually watch happen in a fraction of a second.

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `ping -c 4 example.com` | Test reachability, packet loss and round-trip latency. |
| `nslookup example.com` | Query DNS and display the resolved addresses and resolver used. |
| `curl -sI https://example.com` | Fetch response headers only, to see status code, content type and server. |
| `ifconfig` | Viewed interface information; only public/generic details were recorded. |
| Web browser | Used to observe the URL being opened and the page being rendered. |

## 4. My understanding

Networks are layered agreements. Cables and Wi-Fi carry bits; IP addresses identify where they should go; routers move packets between networks; TCP makes delivery reliable; TLS makes it private; HTTP gives the request and response a shape; DNS removes the need to memorise numbers. Each layer only needs to trust the one below it, which is why so many different devices interoperate.

LAN, MAN and WAN are the same ideas at different scales — a home, a campus, the planet. Packet switching is what makes a shared network practical: nobody needs a dedicated wire, because data is chopped up, routed independently and reassembled. Client–server explains the whole shape of the web: a browser asks, a server answers.

The most useful observation was the DNS lookup: a name maps to *several* addresses, so "the IP address" of a site is not one fixed number.

## 5. Difficulties faced

- `ping` output includes the resolved address of the destination, and `ifconfig` lists local addresses, so I had to be careful to only record the public `example.com` results and not my own network details.
- `nslookup` reports a "Non-authoritative answer", which was confusing at first.
- Distinguishing a router (moves packets between networks) from a DNS resolver (looks up names) — both are involved in opening a page but do unrelated jobs.

## 6. How I resolved them

- I chose one public example domain for every command and copied only those results, deliberately leaving out local interface addresses and my Wi-Fi name.
- I looked up what "non-authoritative" means: the answer came from a resolver's cache rather than the domain's own authoritative name server. It is still the address the browser uses.
- I wrote the numbered walkthrough step by step, which forced me to place each device in exactly one role.

## 7. Evidence / files

- Public `ping`, `nslookup` and `curl` outputs quoted in section 2.2, all for `example.com`.
- No personal IP address, Wi-Fi name, hostname or device identifier is included.

## 8. Commit details

Commit message: **Explain networking concepts and website communication**

Pushed to GitHub on the `main` branch and verified the updated README on the repository page.
