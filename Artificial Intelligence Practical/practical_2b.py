# ===== 2b. Tower of Hanoi =====
def tower_of_hanoi(n, source, destination, auxillary):
    if n==1:
        print(f"move disk 1 from {source}->{destination}")
        return
    tower_of_hanoi(n-1,source,auxillary,destination)
    print(f"move disk {n} from {source}->{destination}")
    tower_of_hanoi(n-1,auxillary,destination,source)
tower_of_hanoi(3,'A','C','B')
