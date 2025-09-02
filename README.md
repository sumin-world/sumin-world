<h1 align="center">sumin-world 🦀</h1>

<details>
<summary>🤔 Why this name?</summary>

```rust
use std::ops::BitOr; struct S(&'static str); impl BitOr for S{type Output=String; fn bitor(self,rhs:Self)->Self::Output{format!("{} in {}!",self.0,rhs.0)}} fn main(){println!("{}",S("sum")|S("world"));}
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

### 🏆 Baekjoon
<p align="center">
  <a href="https://solved.ac/bettermonde/">
    <img src="http://mazassumnida.wtf/api/v2/generate_badge?boj=bettermonde" height="150"/>
  </a>
</p>

---

### 🔧 What I build
- **TCP HTTP Client (C)** — non-blocking `connect`, DNS multi-A failover, recv timeout  
  ↳ https://github.com/sumin-world/suminworld-system-lab/tree/main/network/basics  
- **Multi-client Echo Server (C)** — `select()` 기반, 타임아웃/keepalive 옵션  
  ↳ https://github.com/sumin-world/suminworld-system-lab/tree/main/network/echo_server
- **Rust snippets** — “sum in world, suminworld!” one-liner & fun experiments

### 🐿️ Interests
Low-level networking, socket internals, TLS, packet forensics, systems debugging

### 🪼 Posts
- 네트워크 소켓 프로그래밍/패킷 분석 실습 가이드 (Velog)  
  https://velog.io/@suminworld
