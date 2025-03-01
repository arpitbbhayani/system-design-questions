# 🎙️ Design Text-based Live Commentary

<!--ts-->
📌 **Table of Contents**
- [🎯 Problem Statement](#problem-statement)
- [📜 Requirements](#requirements)
   - [🛠️ Core Requirements](#core-requirements)
   - [⚙️ High-Level Requirements](#high-level-requirements)
   - [🔍 Micro Requirements](#micro-requirements)
- [📌 Output](#output)
   - [📄 Design Document](#design-document)
   - [🛠️ Prototype](#prototype)
      - [🧰 Recommended Tech Stack](#recommended-tech-stack)
      - [⚠️ Keep in Mind](#keep-in-mind)
- [🏆 Outcome](#outcome)
   - [📚 You'll Learn](#youll-learn)
- [🚀 Share and Shoutout](#share-and-shoutout)
<!--te-->

---

# 🎯 Problem Statement

Design a **real-time text-based live commentary** service for a cricket match 🏏. The commentary is updated **ball-by-ball** by a professional commentator and must be served instantly to millions of readers 📢.

### Key Elements:
✅ Smooth **data flow** to provide a seamless UX
✅ **Database & caching** strategy for high efficiency
✅ **Two workflows** - one for **commentators** 📝 and another for **readers** 👀

---

# 📜 Requirements

> *Be creative and explore additional constraints and features that would enhance the product experience.*

## 🛠️ Core Requirements
✔️ Professional commentators update live commentary 📖
✔️ The system must handle **5 million+ concurrent readers** 🌍
✔️ **Ultra-low latency** to ensure real-time delivery ⚡

## ⚙️ High-Level Requirements
🔹 Ensure **High Availability (HA)** for uninterrupted service 🔄
🔹 Data must be **durable** to prevent loss 🔐
🔹 Handle **scalability** for fluctuating traffic 📈
🔹 Design a **cost-effective** solution with proper justification 💰
🔹 Implement **capacity planning** for future-proofing 🏗️
🔹 Enable seamless **integration** with external services 🔗

## 🔍 Micro Requirements
🔸 Data **consistency** is a must 🔄
🔸 Ensure **no deadlocks** in the system 🚫
🔸 Optimize **throughput** by avoiding performance bottlenecks 🚀

---

# 📌 Output

## 📄 Design Document 📜
✅ Create a **detailed design document** covering:
- **System architecture**, components, and interactions 🏗️
- **Critical trade-offs** and design decisions 🔎
- **Scaling strategy** and handling of chokepoints ⚙️

> *Keep the design simple and efficient – unnecessary complexity should be avoided!* 🤯❌

## 🛠️ Prototype ⚡
Develop a **working prototype** to simulate the commentary system. Key tasks:
- Implement a **real-time commentary workflow** locally 🖥️

### 🧰 Recommended Tech Stack

| **Component** | **Options** |
|--------------|-------------|
| 🌐 **Language** | Golang, Java, C++ |
| 🛢️ **Database** | MySQL |
| ⚡ **Cache** | Redis |

### ⚠️ Keep in Mind
⚠️ Optimize **resource utilization** efficiently
⚠️ Avoid **over-engineering** the solution ❌

---

# 🏆 Outcome

## 📚 You'll Learn 🎓
✔️ Designing an **optimal database** schema 📊
✔️ Achieving **high performance & scalability** 🚀
✔️ Avoiding **over-engineering pitfalls** ⚠️

---

# 🚀 Share and Shoutout

If you find this **assignment helpful**, please:
🌟 **Share** with friends & peers 👫
🌟 **Star** this repository ⭐
🌟 **Give me a shoutout** on:
   - **Twitter:** [@arpit_bhayani](https://twitter.com/@arpit_bhayani) 🐦
   - **LinkedIn:** [@arpitbhayani](https://www.linkedin.com/in/arpitbhayani/) 🔗

📌 This assignment is part of **[Arpit's System Design Masterclass](https://arpitbhayani.me/masterclass)** – a premium course on designing **scalable, fault-tolerant, and highly available systems**! 🎓🚀

