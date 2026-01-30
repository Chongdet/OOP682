# 📚 OOP Week 09

### 👤 Student Information
* **Name:** นาย ทรงเดช จำปาเทศ
* **Student ID:** 68114540214

---

### 🛠 Tech Stack & Tools
<p align="left">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="python" />
  <img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white" alt="git" />
  <img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" alt="github" />
  <img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="vscode" />
</p>

### 📦 Package Manager
<img src="https://img.shields.io/badge/managed%20by-uv-purple?style=for-the-badge" alt="uv" />

---

### 📝 Project Description
โปรเจกต์นี้เป็นการสาธิตหลักการของ **Object-Oriented Programming (OOP)** โดยเน้นเรื่อง **Inheritance (การสืบทอด)** ซึ่งประกอบไปด้วย:
* `Person` (Base Class) - คลาสแม่ที่เก็บข้อมูลพื้นฐาน
* `Student` (Derived Class) - คลาสลูกสำหรับข้อมูลนักศึกษา
* `Staff` (Derived Class) - คลาสลูกสำหรับข้อมูลบุคลากร

---

### 🚀 How to Run
รันโปรเจกต์ผ่าน **uv** ด้วยคำสั่งดังนี้:

1. **ติดตั้ง Dependencies:**
   ```powershell
   uv sync
---

### ⚠️ อย่าลืมสั่ง "ปิดจบ" งานบน GitHub
เพื่อให้หน้าเว็บ GitHub อัปเดตตามไฟล์ล่าสุด และกำจัด `uv.lock` กับ `.venv` ออกไปตามที่คุณต้องการ ให้รัน 3 คำสั่งนี้ใน Terminal ครับ:

```powershell
# 1. ลบสิ่งที่ไม่อยากให้โชว์บน GitHub (แต่ยังอยู่ในเครื่อง)
git rm -r --cached .venv
git rm --cached uv.lock

# 2. บันทึกการเปลี่ยนแปลง
git add .
git commit -m "docs: complete README and clean up repository"

# 3. ส่งขึ้น GitHub
git push origin main