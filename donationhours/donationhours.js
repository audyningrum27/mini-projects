// First, run "npm install prompt-sync".
const prompt = require('prompt-sync')();
let total_donation = 0;
const donation_standard = 50000;
let target_hours;
while (true) {
    target_hours = Number.parseInt(prompt("Masukkan target jam: "));
    if (Number.isNaN(target_hours)) {
        console.log("[Error] Tolong masukkan hanya angka saja!");
    } else {
        break;
    }
}
let target_minutes = target_hours * 60;
let target_donation = target_hours * donation_standard;

let running_programme = true;

console.log("\n=== PROGRAM DONASI DIMULAI ===");

while (running_programme === true) {
    let total_current_minutes = Number.parseInt((total_donation / donation_standard) * 60);
    let current_hours = Math.floor(total_current_minutes / 60);
    let current_minutes = total_current_minutes % 60;

    console.log(
        `\nProgress: ${current_hours} jam ${current_minutes} menit.` +
        `\nTarget jam: ${target_hours} jam.` +
        `\nTarget donasi: Rp.${target_donation.toLocaleString('id-ID')}.` +
        `\nTerkumpul: Rp.${total_donation.toLocaleString('id-ID')}.`
    );

    if (total_current_minutes < target_minutes) {
        let new_donation = Number.parseInt(prompt("Masukkan jumlah donasi: Rp "));
        if (Number.isNaN(new_donation) || new_donation <= 0) {
            console.log("\n[Error] Tolong masukkan hanya angka saja dan harus lebih dari 0!");
            continue;
        };
        total_donation += new_donation;
    } else {
        console.log("\nTarget tercapai! Tidak menerima donasi lagi.");

        while (true) {
            let pilihan_user = prompt('Pilih "selesai" atau "tambah_jam"? Ketik pilihanmu: ').toLowerCase();

            if (pilihan_user == "selesai") {
                console.log("\n=== Program dihentikan. Terima kasih! ===");
                running_programme = false;
                break

            } else if (pilihan_user == "tambah_jam") {
                let additional_hours;
                while (true) {
                    additional_hours = Number.parseInt(prompt("Masukkan berapa jam tambahan targetmu: "));
                    if (Number.isNaN(additional_hours)) {
                        console.log("\n[Error] Tolong masukkan hanya angka saja!");
                    } else {
                        break;
                    }
                };

                target_hours += additional_hours;
                target_minutes = target_hours * 60;
                target_donation = target_hours * donation_standard;

                console.log(`\nBerhasil! Target ditambah ${additional_hours} jam. Mari kumpulkan donasi lagi!`);
                break

            } else {
                console.log("\nPilihan tidak dikenali. Mohon hanya ketik 'selesai' atau 'tambah_jam'.");
            }
        }
    }
}