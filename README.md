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

### 🔥 Recent Activity

<!--RECENT_ACTIVITY:start-->
1. ⬆️ Pushed 1 commit(s) to [sumin-world/suminworld-system-lab](https://github.com/sumin-world/suminworld-system-lab)<br>
2. 🔱 Forked [sumin-world/operating-system-in-1000-lines](https://github.com/sumin-world/operating-system-in-1000-lines) from [nuta/operating-system-in-1000-lines](https://github.com/nuta/operating-system-in-1000-lines)<br>
3. ⬆️ Pushed 7 commit(s) to [sumin-world/gluesql](https://github.com/sumin-world/gluesql)<br>
4. ⭐ Starred [xtiankisutsa/awesome-mobile-CTF](https://github.com/xtiankisutsa/awesome-mobile-CTF)<br>
5. ⭐ Starred [shellphish/how2heap](https://github.com/shellphish/how2heap)<br>
<!--RECENT_ACTIVITY:end-->

---

### 📝 Latest Blog Posts

<!-- BLOG-POST-LIST:START -->
- [[네트워크] Part 2: 첫 패킷 캡처 시도](https://suminworld.tistory.com/27)
- [[네트워크] Part 1-4: 환경 세팅기 - 무선 랜카드 USB 패스스루 과정 ALFA AWUS036ACM&lpar;MT7612U&rpar; &lpar;UTM on macOS &amp;rarr; Ubuntu VM&rpar;](https://suminworld.tistory.com/26)
- [[네트워크] Part 1-3: 환경 세팅기 Ubuntu 24.04 + UTM 환경에서 ALFA AWUS036ACM 무선랜카드 설정](https://suminworld.tistory.com/25)
- [x86-64 스택 프롤로그&lpar;Stack Prologue&rpar;와 스택 프레임&lpar;Stack Frame&rpar;](https://suminworld.tistory.com/24)
- [ALFA AWUS036ACM&lpar;MT7612U&rpar; 모니터모드 캡처 설정](https://suminworld.tistory.com/23)
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

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=sumin-world&label=count" alt="count" height="16" />
</p>

<p align="center">
  <i>💡 "Learning by building, one system call at a time"</i>
</p>
