from pymavlink import mavutil
import time

# =========================
# 1. BAĞLANTI
# =========================
master = mavutil.mavlink_connection('udp:127.0.0.1:14550')

master.wait_heartbeat()
print("Bağlantı kuruldu (ArduPilot)")

# =========================
# 2. ARM
# =========================
print("ARM ediliyor...")
master.arducopter_arm()
master.motors_armed_wait()
print("ARMED")

time.sleep(2)

# =========================
# 3. GUIDED MODE
# =========================
master.set_mode_apm('GUIDED')
print("GUIDED MODE aktif")

time.sleep(2)

# =========================
# 4. TAKEOFF
# =========================
def takeoff(altitude):
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
        0,
        0, 0, 0, 0,
        0, 0,
        altitude
    )

print("Takeoff başlıyor...")
takeoff(5)

time.sleep(8)

# =========================
# 5. WAYPOINT FONKSİYONU
# =========================
def goto(x, y, z):
    master.mav.set_position_target_local_ned_send(
        0,
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        0b110111111000,
        x, y, -z,   # NED → Z NEGATİF
        0, 0, 0,
        0, 0, 0,
        0, 0
    )

# =========================
# 6. WAYPOINTLER (SENİN SENARYO)
# =========================
waypoints = [
    (0, 0, 1.5),        # start
    (1.5, 1.5, 1.5),    # silindir
    (3.5, 3.5, 1.5),    # küp
    (1.5, 5.5, 1.5),    # küre
    (0, 0, 1.5)         # dönüş
]

for i, wp in enumerate(waypoints):
    print(f"Waypoint {i+1}: {wp}")

    for _ in range(100):
        goto(wp[0], wp[1], wp[2])
        time.sleep(0.1)

# =========================
# 8. LAND
# =========================
print("Landing...")

master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_NAV_LAND,
    0,
    0, 0, 0, 0,
    0, 0,
    0
)

print("İniş komutu gönderildi")
