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

### 🐿️ Interests
System hacking (buffer overflow, heap, exploit techniques)  
Network hacking (ARP/DNS spoofing, session hijacking)  
Linux internals (syscall, process, memory management)  
Security research & CTF practice (Dreamhack, pwnable.kr, OverTheWire)

### 🔧 What I build
- **TCP HTTP Client (C)** — non-blocking `connect`, DNS multi-A failover, recv timeout  
  ↳ https://github.com/sumin-world/suminworld-system-lab/tree/main/network/basics  
- **Multi-client Echo Server (C)** — `select()` 기반, 타임아웃/keepalive 옵션  
  ↳ https://github.com/sumin-world/suminworld-system-lab/tree/main/network/echo_server
- **Rust snippets** — "sum in world, suminworld!" one-liner & fun experiments

### 🪼 Blog Posts
- **[시스템 보안] 버퍼 오버플로우 취약점**  
  ↳ https://suminworld.tistory.com/2
- **[네트워크] C 소켓 프로그래밍 Echo 서버 구현 - 기본부터 멀티클라이언트까지**  
  ↳ https://suminworld.tistory.com/9
- **[시스템 프로그래밍] Tiny Shell 프로젝트: 잡 컨트롤, 시그널, 레이스 컨디션 다루기**  
  ↳ https://suminworld.tistory.com/12
- **[네트워크] ALFA AWUS036ACM 모니터 모드 설정 (Wi-Fi 보안 실습 - 1)**  
  ↳ https://suminworld.tistory.com/14
