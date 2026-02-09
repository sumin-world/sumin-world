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
- **[Tiny Shell](https://github.com/sumin-world/suminworld-system-lab/tree/main/shell)** (C)
  - Job control, signal handling, race condition prevention
  - Process management & I/O redirection

#### 🦀 Rust Experiments

- **[rust-security-suminworld](https://github.com/sumin-world/rust-security-suminworld)** — Cargo workspace (7 crates, 64 tests, 0 warnings)
    - port_scanner — Async TCP port scanner (Tokio, 1024 concurrent connections)
    - discord_audit_bot — Discord server security audit bot (Serenity, 5-module architecture)
    - packet-match-fuzz — KMP pattern matcher & mutation fuzzer for packet payloads
    - wifi_audit — Passive 802.11 Wi-Fi auditor (Beacon/Probe analysis, libpcap)
    - crypto — Educational cryptography toolkit (Caesar, Vigenère, XOR, Feistel, RSA, FNV-1a)
    - merkle — SHA-256 Merkle tree with domain-separated hashing & inclusion proofs
    - kernel-features — Rust-for-Linux language features study (Field Projection, In-place Init, Arbitrary Self Types)
    - cache — Flush+Reload cache side-channel PoC (C)
- **One-liner Challenge**: `sum in world = suminworld!` — Custom operators & trait implementations

---

### 🔒 Security Research & Exploits

- **Linux Kernel CVE-2022-32250 Exploit Development** — WHS-2nd (White Hat School), Team Project (2024)
  - Implemented a Linux kernel exploit for CVE-2022-32250 (UAF) with:
    - Heap grooming & leakage primitives
    - KASLR-related exploitation steps
    - Privilege escalation technique via `modprobe_path` overwrite (controlled execution path)

---

- **[SKT USIM Hacking Analysis](https://github.com/sumin-world/telecom-usim-security-lab)** — USIS (University Student Intelligence Society), 3rd Cohort (2025, Team Project)
  - Wrote a readability-first technical report for a mixed-background team (many non-CS members)
  - Focus: USIM/telecom threat surface, core flows around subscriber identity, and security implications across telecom backend components (e.g., HSS/UDM) from an APT-style perspective
  - Role: Primary author of the report, organizing the narrative, diagrams, and explanations to make complex topics digestible

---
 
- **OpenStack “Open the Window” Security Auditing** — SSL 6th Term (Oct 2025 – Jan 2026)
  - Authored a detailed report on the **Barbican Key Management** module, including architecture analysis and threat modelling.
  - Presented the team’s vulnerability findings (DOM XSS, IDOR, SSRF) in the final briefing, ensuring accurate reproduction and impact analysis.
  - Worked across Skyline‑Console, Cinder, Glance, and Barbican to verify issues and document mitigation steps.

---

### 🧠 Machine Learning

- **ML‑based Flood Prediction (Han River)** — Hydrology / ML Coursework Project (2024)  
  - Proposed the project topic and led the effort to build an LSTM‑based time‑series model for predicting Han River water levels using real‑world data.  
  - Focused on rigorous evaluation, feature engineering, and iterative model improvement.  
  - This research concept later inspired the Social Crab hardware project in the BitCrab embedded systems club.

### ⚙️ Hardware

- **[Social Crab PCB Design](https://github.com/sumin-world/flood-alert-pcb)** — BitCrab Embedded Systems Club (Yonsei University) / 2024 IHEI Workstation Social Innovation Project (2024, Team Project)
  - As part of a small team from BitCrab, executed this hardware project inspired by our flood-prediction coursework, applying data-driven insights to embedded design for social impact (e.g., flood monitoring IoT prototype).
  - Designed a custom PCB for Raspberry Pi Pico, focusing on power-stability testing and embedded prototyping with protocols like I2C/SPI/UART.
  - Contributed to bring-up/testing workflows and documented processes for reproducible results.

---

#### 📡 Signal Integrity & Channel Analysis
- **[Channel Analysis Lab](https://github.com/sumin-world/channel-analysis-lab)** (Python)
  - Statistical worst-case analysis toolkit for high-speed serial channels (PCIe 6.0, USB4, 112G PAM4)
  - Vectorized Monte Carlo engine (NumPy, 10–50× speedup), 2^3 deterministic corner sweep, 2^k full-factorial DOE sensitivity
  - Corner vs MC gap analysis, main-effect Pareto ranking for manufacturing tolerance budgeting
  - Built on scikit-rf / Touchstone S-parameter data — CI-ready with Makefile pipeline

---

#### 🧊 Assistive Technology
- **[NaviBlock](https://github.com/sumin-world/navi-block)** (C++, Python) — Team NAVI, Yonsei IHEI Workstation (2025)
  - AI-powered spatial cognition training system for visually impaired users
  - 3×3 NFC sensor grid (PN532 ×9, TCA9548A I2C mux) on ESP32, communicating with mobile app via BLE
  - RAG-based voice assistant (GPT-4 + FAISS + pyttsx3) for on-demand spatial cognition Q&A
  - Role: Product Management, Hardware Product Development (PCB bring-up, firmware, sensor integration)

---

#### 📊 Market Intelligence
- **[Laneige INSIGHT MVP](https://github.com/sumin-world/amore-project)** (Python)
  - Automated market intelligence pipeline for K-Beauty on Amazon
  - Snapshot collection → Change detection → AI root-cause analysis (Groq/Claude/rule fallback) → ROI simulation
  - Perceptual hashing (pHash) for thumbnail A/B test detection
  - Streamlit dashboard with competitive analysis & ranking trend charts

---

### 🔥 Recent Activity

<!--RECENT_ACTIVITY:start-->
1. ⬆️ Pushed undefined commit(s) to [sumin-world/sumin-world](https://github.com/sumin-world/sumin-world)<br>
2. ⬆️ Pushed undefined commit(s) to [sumin-world/rust-security-suminworld](https://github.com/sumin-world/rust-security-suminworld)<br>
3. ⬆️ Pushed undefined commit(s) to [sumin-world/sumin-world](https://github.com/sumin-world/sumin-world)<br>
4. ⬆️ Pushed undefined commit(s) to [sumin-world/channel-analysis-lab](https://github.com/sumin-world/channel-analysis-lab)<br>
5. ⬆️ Pushed undefined commit(s) to [sumin-world/amore-project](https://github.com/sumin-world/amore-project)<br>
<!--RECENT_ACTIVITY:end-->

---

### 📝 Latest Blog Posts

<!-- BLOG-POST-LIST:START -->
- [일어서기](https://suminworld.tistory.com/39)
- [CSAPP 1.4: Processors Read and Interpret Instructions Stored in Memory](https://suminworld.tistory.com/60)
- [텍스트에서 지식 그래프 추출하기 - Extracting Knowledge Graphs From Text With GPT4o](https://suminworld.tistory.com/59)
- [IPv4 시장 가격 vs 클라우드 과금: v4/v6 연결 지연 측정](https://suminworld.tistory.com/58)
- [CSAPP 1.6 메모리 계층 &lpar;Memory Hierarchy&rpar; 정리](https://suminworld.tistory.com/57)
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
