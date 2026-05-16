from pymavlink import mavutil
import time
import math

# -----------------------------
# BAGLANTİ
# -----------------------------
master = mavutil.mavlink_connection('udp:127.0.0.1:14550')
master.wait_heartbeat()
print("Heartbeat alindi - baglanti kuruldu")


def set_mode(mode_name):
    mode_id = master.mode_mapping()[mode_name]
    master.mav.set_mode_send(
        master.target_system,
        mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
        mode_id
    )
    print(f"Komut gonderildi: {mode_name} moda geciliyor")

def arm():
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,
        1, 0, 0, 0, 0, 0, 0
    )
    print("ARM komutu gonderildi")

def takeoff(altitude):
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
        0,
        0, 0, 0, 0, 0, 0, altitude
    )
    print(f"Kalkis komutu gonderildi: {altitude}m")

def goto(lat, lon, alt):
    master.mav.mission_item_send(
        master.target_system,
        master.target_component,
        0,
        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
        mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
        2, 0, 0, 0, 0, 0,
        lat, lon, alt
    )
    print(f"Yeni hedef: {lat}, {lon}, {alt}")

# -----------------------------
# TELEMETRİ OKUMA
# -----------------------------
def get_position():
    msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
    lat = msg.lat / 1e7
    lon = msg.lon / 1e7
    alt = msg.relative_alt / 1000.0
    return lat, lon, alt

# -----------------------------
# MOD DEĞİŞTİR
# -----------------------------
set_mode('GUIDED')

# MOD ONAY BEKLE
while True:
    msg = master.recv_match(type='HEARTBEAT', blocking=True)
    if msg.custom_mode == master.mode_mapping()['GUIDED']:
        print("GUIDED moda geçildi onaylandı")
        break

# -----------------------------
# ARM
# -----------------------------
arm()

while True:
    msg = master.recv_match(type='HEARTBEAT', blocking=True)
    if msg.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED:
        print("Araç ARM edildi")
        break

# -----------------------------
# KALKIŞ
# -----------------------------
takeoff(10)

# 10 metreye çıkmasını bekle
while True:
    lat, lon, alt = get_position()
    print(f"İrtifa: {alt:.1f} m")
    if alt >= 9:
        print("Hedef irtifaya ulaşıldı")
        break
    time.sleep(1)

# -----------------------------
# GİDİLECEK NOKTA (örnek offset)
# -----------------------------
lat, lon, alt = get_position()

target_lat = lat + 0.0001
target_lon = lon + 0.0001
target_alt = 10

goto(target_lat, target_lon, target_alt)

print("Hedef konuma gidiliyor...")

# basit kontrol (yaklaşma)
while True:
    lat, lon, alt = get_position()

    dist = math.sqrt(
        (lat - target_lat)**2 +
        (lon - target_lon)**2
    )

    print(f"Hedefe uzaklık: {dist:.7f}")

    if dist < 0.00002:
        print("Hedefe ulaşıldı")
        break

    time.sleep(1)

# -----------------------------
# İNİŞ
# -----------------------------
set_mode('LAND')
print("İniş modu gönderildi")

while True:
    lat, lon, alt = get_position()
    print(f"İniş - irtifa: {alt:.1f}")
    if alt < 0.3:
        print("Araç indi")
        break
    time.sleep(1)
