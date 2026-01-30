# 📚 OOP Week 09: Inheritance Project

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
โปรเจกต์นี้เป็นการสาธิตหลักการของ **Object-Oriented Programming (OOP)** โดยเน้นเรื่อง **Inheritance (การสืบทอด)** และการใช้งาน Class ในรูปแบบต่างๆ ดังนี้:
* `Person` (Base Class) - คลาสแม่ที่เก็บข้อมูลพื้นฐาน
* `Student` (Derived Class) - คลาสลูกสำหรับข้อมูลนักศึกษา
* `Staff` (Derived Class) - คลาสลูกสำหรับข้อมูลบุคลากร

---
### 🚀 How to Run
รับโปรเจกต์ผ่าน **uv** ด้วยคำสั่งดังนี้:

<<<<<<< HEAD
### เตรียมสภาพแวดล้อม:
`uv sync`

### รันไฟล์ทดสอบ:
`uv run main.py`
`uv run app2.py`
`uv run app3.py`
`uv run inheritanceEx.py`
---

### 📂 Project Structure
```text
week09/
├── models/               # โฟลเดอร์เก็บ Class ต่างๆ
│   ├── BankAccount.py    # คลาสจัดการบัญชีธนาคาร (Operator Overloading)
│   ├── classroom.py      # คลาสจัดการห้องเรียน (List interaction)
│   ├── person.py         # Base Class (คลาสแม่)
│   ├── staff.py          # Derived Class (บุคลากร)
│   └── student.py        # Derived Class (นักศึกษา)
├── app2.py               # ไฟล์ทดสอบระบบ BankAccount
├── app3.py               # ไฟล์ทดสอบระบบ Classroom
├── inheritanceEx.py      # ไฟล์แบบฝึกหัด Inheritance รวม
├── main.py               # ไฟล์หลักสำหรับรันโปรแกรม
├── pyproject.toml        # ไฟล์ตั้งค่าโปรเจกต์ (uv)
└── README.md             # ไฟล์อธิบายโปรเจกต์
=======
1. **ติดตั้ง Dependencies:**
   ```powershell
   uv run main.py
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
>>>>>>> 98a5e9b7c453eea553e0efe6993b052479aa706a
