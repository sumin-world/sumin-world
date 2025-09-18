<h1 align="center">sumin-world 🦀</h1>

<details>
<summary>🤔 Why this name?</summary>

```rust
use std::ops::BitOr;
struct S(&'static str);
impl BitOr for S {
    type Output = String;
    fn bitor(self, rhs: Self) -> Self::Output {
        format!("{} in {}!", self.0, rhs.0)
    }
}
fn main() {
    println!("{}", S("sum") | S("world"));
}
```

*Sometimes the answer is in the code itself* ✨

</details>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Share+Tech+Mono&weight=700&size=24&pause=1200&color=00F5FF&center=true&vCenter=true&width=650&lines=C+%26+Rust+System+Programming;Linux+Kernel+%26+Security+Research" alt="Typing SVG" />
</p>

---

### 🔧 Tech Stack

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg" width="40" height="40"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-original.svg" width="40" height="40"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" width="40" height="40"/>
</p>

---

### 🚀 Featured Projects

#### 🌐 Network Programming

**[TCP HTTP Client](https://github.com/sumin-world/suminworld-system-lab/tree/main/network/basics)** (C)
[![Build](https://github.com/sumin-world/suminworld-system-lab/actions/workflows/c-build.yml/badge.svg)](https://github.com/sumin-world/suminworld-system-lab/actions)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

- Non-blocking connect with timeout
- DNS multi-A record failover
- Production-ready HTTP/1.1 implementation

**[Multi-client Echo Server](https://github.com/sumin-world/suminworld-system-lab/tree/main/network/echo_server)** (C)
[![Build](https://github.com/sumin-world/suminworld-system-lab/actions/workflows/c-build.yml/badge.svg)](https://github.com/sumin-world/suminworld-system-lab/actions)

- `select()` based I/O multiplexing
- Configurable timeout & keepalive
- Handles multiple concurrent clients

#### 🔒 System Security & Programming

**[Signal Handling Demo](https://github.com/sumin-world/suminworld-system-lab/tree/main/signal-demo)** (C)
[![C Build](https://github.com/sumin-world/suminworld-system-lab/actions/workflows/c-build.yml/badge.svg)](https://github.com/sumin-world/suminworld-system-lab/actions)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

- Comprehensive POSIX signal handling
- GitHub Actions CI/CD automation
- Interactive demo with automated testing
- [📝 Blog Post](https://suminworld.tistory.com/signal-demo)

**[Tiny Shell](https://github.com/sumin-world/suminworld-system-lab/tree/main/tinyshell)** (C)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/sumin-world/suminworld-system-lab)

- Full job control implementation
- Signal handling & race condition prevention
- Process management & I/O redirection
- [📝 Blog Post](https://suminworld.tistory.com/12)

#### 🦀 Rust Experiments

**Custom Operators & Traits**
![Rust](https://img.shields.io/badge/rust-%23000000.svg?style=flat&logo=rust&logoColor=white)

- One-liner: `sum in world = suminworld!`
- Operator overloading experiments
- Creative trait implementations

---

### 🔥 Recent Activity

<!--START_SECTION:activity-->
<!--END_SECTION:activity-->

---

### 📝 Latest Blog Posts

<!-- BLOG-POST-LIST:START -->
<!-- BLOG-POST-LIST:END -->

---

### 🐿️ Research Interests

- **System Hacking**: Buffer overflow, heap exploitation, ROP chains
- **Network Security**: ARP/DNS spoofing, session hijacking, packet analysis
- **Linux Internals**: Syscalls, process management, memory subsystem
- **CTF Practice**: Dreamhack, pwnable.kr, OverTheWire

---

### 🏆 Competitive Programming

<p align="center">
  <a href="https://solved.ac/bettermonde/">
    <img src="http://mazassumnida.wtf/api/v2/generate_badge?boj=bettermonde" height="150"/>
  </a>
</p>

---

### 📊 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=sumin-world&show_icons=true&theme=tokyonight" height="165">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=sumin-world&layout=compact&theme=tokyonight" height="165">
</p>

---

<p align="center">
  <i>💡 "Learning by building, one system call at a time"</i>
</p>

---

### 🔄 Auto-Update Setup

`.github/workflows/recent-activity.yml` 파일 생성:

```yaml
name: Recent Activity

on:
  schedule:
    - cron: "0 */12 * * *"   # 12시간마다 (UTC 기준)
  workflow_dispatch:

permissions:
  contents: write

jobs:
  update-activity:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: Readme-Workflows/recent-activity@v2
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

`.github/workflows/blog-post.yml` 파일 생성:

```yaml
name: Latest Blog Posts

on:
  schedule:
    - cron: '0 */12 * * *'
  workflow_dispatch:

jobs:
  update-readme:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: gautamkrishnar/blog-post-workflow@master
        with:
          feed_list: "https://suminworld.tistory.com/rss"
```<h1 align="center">sumin-world 🦀</h1>

<details>
<summary>🤔 Why this name?</summary>

```rust
use std::ops::BitOr;
struct S(&'static str);
impl BitOr for S {
    type Output = String;
    fn bitor(self, rhs: Self) -> Self::Output {
        format!("{} in {}!", self.0, rhs.0)
    }
}
fn main() {
    println!("{}", S("sum") | S("world"));
}
```

*Sometimes the answer is in the code itself* ✨

</details>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Share+Tech+Mono&weight=700&size=24&pause=1200&color=00F5FF&center=true&vCenter=true&width=650&lines=C+%26+Rust+System+Programming;Linux+Kernel+%26+Security+Research" alt="Typing SVG" />
</p>

---

### 🔧 Tech Stack

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg" width="40" height="40"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-original.svg" width="40" height="40"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" width="40" height="40"/>
</p>

---

### 🚀 Featured Projects

#### 🌐 Network Programming
- **[TCP HTTP Client](https://github.com/sumin-world/suminworld-system-lab/tree/main/network/basics)** (C)
  - Non-blocking connect, DNS multi-A failover, recv timeout
  - Production-ready HTTP/1.1 implementation

- **[Multi-client Echo Server](https://github.com/sumin-world/suminworld-system-lab/tree/main/network/echo_server)** (C)
  - `select()` based I/O multiplexing
  - Timeout & keepalive support

#### 🔒 System Security & Programming
- **[Signal Handling Demo](https://github.com/sumin-world/suminworld-system-lab/tree/main/signal-demo)** (C)
  - POSIX signal handling with CI/CD automation
  - Interactive demo with automated testing

- **[Tiny Shell](https://github.com/sumin-world/suminworld-system-lab/tree/main/tinyshell)** (C)
  - Job control, signal handling, race condition prevention
  - Process management & I/O redirection

#### 🦀 Rust Experiments
- **One-liner Challenge**: `sum in world = suminworld!`
- Custom operators & trait implementations

---

### 📝 Technical Blog Posts

<table>
<tr>
<td width="50%">

**System Security**
- [버퍼 오버플로우 취약점](https://suminworld.tistory.com/2)
- [Tiny Shell: 잡 컨트롤 & 시그널](https://suminworld.tistory.com/12)

</td>
<td width="50%">

**Network Programming**
- [C 소켓 Echo 서버 구현](https://suminworld.tistory.com/9)
- [ALFA AWUS036ACM 모니터 모드](https://suminworld.tistory.com/14)

</td>
</tr>
</table>

---

### 🐿️ Research Interests

- **System Hacking**: Buffer overflow, heap exploitation, ROP chains
- **Network Security**: ARP/DNS spoofing, session hijacking, packet analysis
- **Linux Internals**: Syscalls, process management, memory subsystem
- **CTF Practice**: Dreamhack, pwnable.kr, OverTheWire

---

### 🏆 Competitive Programming

<p align="center">
  <a href="https://solved.ac/bettermonde/">
    <img src="http://mazassumnida.wtf/api/v2/generate_badge?boj=bettermonde" height="150"/>
  </a>
</p>

---

### 📊 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=sumin-world&show_icons=true&theme=tokyonight" height="165">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=sumin-world&layout=compact&theme=tokyonight" height="165">
</p>

---

<p align="center">
  <i>💡 "Learning by building, one system call at a time"</i>
</p>
