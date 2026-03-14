# ProjectOOP Pygame Shooter

เกมยิงปืนแนว 2D สร้างด้วย Python และ Pygame

## สมาชิกทีม
- กฤษฎาพงษ์ ทิณพัฒน์ (รหัสนักศึกษา 68114540054)
- นายอติวิชญ์ สีหนันท์ (รหัสนักศึกษา 68114540689)

## คำอธิบาย
เกมมีพื้นฐาน:
- ผู้เล่นอยู่ฝั่งซ้ายของหน้าจอ (โซนจำกัด)
- ยิงพลัง (ปุ่ม SPACE)
- ศัตรู spawn ทางขวาเข้ามา
- score: enemy1=10, enemy2=20, enemy3=-5
- ศัตรูจะเพิ่มความเร็วแบบช้า ๆ (ไม่เร็วเกินไป) เมื่อเวลาผ่านไป
- ถ้าศัตรูเข้าถึงเส้นเขตผู้เล่นแล้วเกมแพ้ และแสดง GAME OVER + สรุปคะแนน
- ปุ่ม R สำหรับ reset เกม

## โฟลเดอร์และไฟล์ที่สำคัญ
- main.py
- allflie/settings.py
- allflie/player.py
- allflie/enemy.py
- allflie/bullet.py

## วิธีใช้งาน
1. ติดตั้ง Python 3.13 และ Pygame
2. เปิด terminal แล้วเข้า folder
   `cd "C:\Users\Asus Tuf Gaming\OneDrive\Desktop\ProjectOOP"`
3. สั่งรัน
   `./.venv/Scripts/python.exe main.py`

## คำสั่งติดตั้ง
```
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel
.\.venv\Scripts\python.exe -m pip install pygame
```

## ปุ่มควบคุม
- ลูกศร/WASD: เคลื่อนที่
- SPACE: ยิง
- R: รีเซ็ต

## ชนิดศัตรู
- Enemy 1: +10 คะแนน
- Enemy 2: +20 คะแนน
- enemy3: -5 คะแนน (สามารถปล่อยผ่านได้, ถ้ายิงโดนจะถูกหักคะแนน)
