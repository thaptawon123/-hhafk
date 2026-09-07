code = '''import os
import subprocess
import time
import threading

BOT_DIR = os.path.expanduser('~/-hhafk-main/yoooo12')

def find_exe_path():
    if not os.path.exists(BOT_DIR):
        return None
    for f in os.listdir(BOT_DIR):
        if f.startswith('MinecraftClient'):
            return os.path.join(BOT_DIR, f)
    return None

EXE_PATH = find_exe_path()

def read_output(p):
    while p.poll() is None:
        line = p.stdout.readline()
        if line:
            print(line.strip(), flush=True)

def run_single_bot():
    global EXE_PATH
    if not EXE_PATH or not os.path.exists(EXE_PATH):
        # ลองค้นหาใหม่อีกรอบ
        EXE_PATH = find_exe_path()
    
    if not EXE_PATH or not os.path.exists(EXE_PATH):
        print(f'❌ ไม่พบไฟล์รันบอทที่ขึ้นต้นด้วย MinecraftClient ใน: {BOT_DIR}')
        return

    try:
        os.chmod(EXE_PATH, 0o755)
    except Exception:
        pass
        
    print(f'กำลังเริ่มรันบอทจากไฟล์: {EXE_PATH}...')
    p = subprocess.Popen([EXE_PATH], cwd=BOT_DIR, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace')
    threading.Thread(target=read_output, args=(p,), daemon=True).start()
    try:
        print('⏳ รอเชื่อมต่อเซิร์ฟเวอร์ (12 วินาที)...')
        time.sleep(20)
        if p.poll() is not None: return
        print('🔑 กำลังส่งรหัสผ่าน...')
        p.stdin.write('/dialog set pass tang2547\\n')
        p.stdin.flush()
        time.sleep(10)
        if p.poll() is not None: return
        print('🖱️ ยืนยันเข้าสู่ระบบ...')
        p.stdin.write('/dialog click 1\\n')
        p.stdin.flush()
        time.sleep(10)
        if p.poll() is not None: return
        print('🔐 ข้าม/จัดการ 2FA...')
        p.stdin.write('/dialog click 2\\n')
        p.stdin.flush()
        time.sleep(10)
        if p.poll() is not None: return
        print('🤖 กำลังรันคำสั่ง AFK เสถียร...')
        for cmd in ['/useitem\\n', '/inventory container click 10\\n', '/afk\\n']:
            if p.poll() is not None: return
            p.stdin.write(cmd)
            p.stdin.flush()
            time.sleep(5)
        print('✅ บอททำงานออนไลน์และรัน AFK สำเร็จเรียบร้อย!')
        p.wait()
    except Exception as e:
        print(f'❌ เกิดข้อผิดพลาด: {e}')

if __name__ == '__main__':
    run_single_bot()
'''
with open('run.py', 'w', encoding='utf-8') as f:
    f.write(code)
