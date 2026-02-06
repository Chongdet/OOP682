# 🏗️ OOP Week 10: Design Patterns & Architecture with FastAPI

### 👤 Student Information
* **Name:** นาย ทรงเดช จำปาเทศ
* **Student ID:** 68114540214

---

### 🛠 Tech Stack & Tools
<p align="left">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="python" />
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="fastapi" />
  <img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white" alt="git" />
  <img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="vscode" />
</p>

### 📦 Package Manager
<img src="https://img.shields.io/badge/managed%20by-uv-purple?style=for-the-badge" alt="uv" />

---

### 📝 Project Description
โปรเจกต์นี้เป็นการนำหลักการ **OOP** มาประยุกต์ใช้ร่วมกับ **Web Framework (FastAPI)** โดยเน้นการออกแบบสถาปัตยกรรมซอฟต์แวร์ที่ดี (Software Architecture) เพื่อให้โค้ดมีความยืดหยุ่น ดูแลรักษาง่าย และทดสอบได้ง่าย

**Concepts หลักที่ใช้:**
* **SOLID Principles:** หลักการออกแบบ Class ให้มีหน้าที่ชัดเจน (Single Responsibility) และรองรับส่วนขยาย
* **Layered Architecture:** การแบ่งชั้นของโค้ดเป็น Controllers (Routers), Services และ Repositories
* **Dependency Injection (DI):** การฉีด Object ที่ต้องใช้งานเข้าไป แทนการสร้างเองภายใน Class (ใช้ระบบ DI ของ FastAPI)

---

### 🚀 How to Run
รันโปรเจกต์ผ่าน **uv** ด้วยคำสั่งดังนี้:

### 1. เตรียมสภาพแวดล้อม (Install dependencies):
```bash
uv sync