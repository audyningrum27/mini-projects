total_donation = 0
donation_standard = 50000
target_hours = int(input("Masukkan target jam: "))
target_minutes = target_hours * 60
target_donation = target_hours * donation_standard

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
            total_donation = total_donation + new_donation
        except ValueError:
            print("[Error] Tolong masukkan hanya angka saja!")
            continue
    
    else:
        print("Target tercapai! Tidak menerima donasi lagi.")

        while True:
            pilihan_user = input('Pilih "selesai" atau "tambah_jam"? Ketik pilihanmu: ').lower()

            if pilihan_user == "selesai":
                print("Program dihentikan. Terima kasih~")
                running_programme = False
                break
                
            elif pilihan_user == "tambah_jam":
                additional_hours = int(input("Masukkan berapa jam tambahan targetmu: "))
                target_hours = target_hours + additional_hours
                target_minutes = target_hours * 60
                
                print(f"Berhasil! Target ditambah {additional_hours} jam. Mari kumpulkan donasi lagi!")
                break
                
            else:
                print("Pilihan tidak dikenali. Mohon hanya ketik 'selesai' atau 'tambah_jam'.")