from pymavlink import mavutil
import time

# Bağlantı
master = mavutil.mavlink_connection('udp:127.0.0.1:14550')

print("Bağlantı bekleniyor...")
master.wait_heartbeat()
print("Bağlandı!")

def get_battery(msg):
    return msg.battery_remaining

while True:
    msg = master.recv_match(blocking=True)

    if not msg:
        continue

    msg_type = msg.get_type()

    # GPS
    if msg_type == "GLOBAL_POSITION_INT":
        lat = msg.lat / 1e7
        lon = msg.lon / 1e7
        alt = msg.relative_alt / 1000.0
        print(f"[GPS] Lat: {lat:.6f}, Lon: {lon:.6f}, Alt: {alt:.2f}m")

    # Hız
    if msg_type == "VFR_HUD":
        print(f"[SPEED] Airspeed: {msg.airspeed:.2f} m/s")

    # Batarya
    if msg_type == "SYS_STATUS":
        print(f"[BATTERY] %{msg.battery_remaining}")

    # Mod bilgisi
    if msg_type == "HEARTBEAT":
        mode = mavutil.mode_string_v10(msg)
        armed = msg.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED
        print(f"[MODE] {mode} | Armed: {bool(armed)}")

    time.sleep(0.5)
