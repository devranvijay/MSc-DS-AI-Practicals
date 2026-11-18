# ===== 4b. Water Jug Problem =====
jugA, jugB = 0,0
capA, capB = 4,3
tar = 2
jugB = capB
print(f"step1: jugA = {jugA}, jugB = {jugB}")
jugA, jugB = jugB,0
print(f"step2: jugA = {jugA}, jugB = {jugB}")
jugB = capB
print(f"step3: jugA = {jugA}, jugB = {jugB}")
transfer = capA - jugB
jugA += transfer
jugB -= transfer
print(f"step4: jugA = {jugA}, jugB = {jugB}")
