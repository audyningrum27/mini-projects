total_donation = 0
donation_standard = 50000
while True:
    try:
        target_hours = int(input("Masukkan target jam: "))
        target_minutes = target_hours * 60
        target_donation = target_hours * donation_standard
        break
    except ValueError:
        print("[Error] Tolong masukkan hanya angka saja!")
        continue

running_programme = True

print(f"\n=== PROGRAM DONASI DIMULAI ===")

while running_programme:
    total_current_minutes = int((total_donation / donation_standard) * 60)
    current_hours = total_current_minutes // 60
    current_minutes = total_current_minutes % 60

    print(
        f"\nProgress: {current_hours} jam {current_minutes} menit."
        f"\nTarget jam: {target_hours} jam."
        f"\nTarget donasi: Rp.{target_donation:,}."
        f"\nTerkumpul: Rp.{total_donation:,}."
    )

    if total_current_minutes < target_minutes:
        try:
            new_donation = int(input("Masukkan jumlah donasi: Rp "))
            if new_donation <= 0:
                print("\n[Error] Donasi tidak boleh minus atau nol!")
                continue
            total_donation = total_donation + new_donation
        except ValueError:
            print("\n[Error] Tolong masukkan hanya angka saja!")
            continue
    
    else:
        print("\nTarget tercapai! Tidak menerima donasi lagi.")

        while True:
            pilihan_user = input('Pilih "selesai" atau "tambah_jam"? Ketik pilihanmu: ').lower()

            if pilihan_user == "selesai":
                print("\n=== Program dihentikan. Terima kasih! ===")
                running_programme = False
                break
                
            elif pilihan_user == "tambah_jam":
                while True:
                    try:
                        additional_hours = int(input("Masukkan berapa jam tambahan targetmu: "))
                        if additional_hours <= 0:
                            print("\n[Error] Tambahan jam harus lebih dari 0!")
                            continue
                        break
                    except ValueError:
                        print("\n[Error] Tolong masukkan hanya angka saja!")
                
                target_hours = target_hours + additional_hours
                target_minutes = target_hours * 60
                target_donation = target_hours * donation_standard
                
                print(f"\nBerhasil! Target ditambah {additional_hours} jam. Mari kumpulkan donasi lagi!")
                break
            
            else:
                print("\nPilihan tidak dikenali. Mohon hanya ketik 'selesai' atau 'tambah_jam'.")