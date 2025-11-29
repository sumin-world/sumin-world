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

- **[Tiny Shell](https://github.com/sumin-world/suminworld-system-lab/tree/main/shell)** (C)
  - Job control, signal handling, race condition prevention
  - Process management & I/O redirection

#### 🦀 Rust Experiments
- **One-liner Challenge**: `sum in world = suminworld!`
- Custom operators & trait implementations

---

### 🔥 Recent Activity

<!--RECENT_ACTIVITY:start-->
1. ⭐ Starred [remzi-arpacidusseau/ostep-translations](https://github.com/remzi-arpacidusseau/ostep-translations)<br>
2. ⬆️ Pushed undefined commit(s) to [sumin-world/suminworld-system-lab](https://github.com/sumin-world/suminworld-system-lab)<br>
3. ⬆️ Pushed undefined commit(s) to [sumin-world/suminworld-system-lab](https://github.com/sumin-world/suminworld-system-lab)<br>
4. ⬆️ Pushed undefined commit(s) to [sumin-world/sumin-world](https://github.com/sumin-world/sumin-world)<br>
5. ⭐ Starred [nv-morpheus/Morpheus](https://github.com/nv-morpheus/Morpheus)<br>
<!--RECENT_ACTIVITY:end-->

---

### 📝 Latest Blog Posts

<!-- BLOG-POST-LIST:START -->
- [️리눅스 백신 실습2 - ClamAV 실시간 보호 구현 &lpar;inotify + bash 자동화&rpar;](https://suminworld.tistory.com/50)
- [Google Dev Challenge: C 언어 타입 변환의 함정](https://suminworld.tistory.com/49)
- [[OS] 뮤텍스 + Block&lpar;&rpar; 방식의 문제점 &lpar;Producer-Consumer Problem&rpar;](https://suminworld.tistory.com/48)
- [[운영체제론] Constant Time Coalescing &lpar;Case 1-4&rpar; 정리](https://suminworld.tistory.com/46)
- [tmux &lpar;수정 예정&rpar;](https://suminworld.tistory.com/44)
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
