
import datetime
from prettytable import PrettyTable  # Import PrettyTable

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Dosen(User):
    def __init__(self, username, password, name):
        super().__init__(username, password)
        self.name = name

class Mahasiswa(User):
    def __init__(self, username, password, name, age):
        super().__init__(username, password)
        self.name = name
        self.age = age
        self.attendance_record = []

class Attendance:
    def __init__(self, mahasiswa, date, status):
        self.mahasiswa = mahasiswa
        self.date = date
        self.status = status

class Kampus:
    def __init__(self):
        self.dosen = [Dosen("admin Dosen", "22334455", "Bapak Rojen")]
        self.mahasiswas = [
            Mahasiswa("mahasiswa1", "2409116110", "Yaya", 15),
            Mahasiswa("mahasiswa2", "2409116111", "Paris", 16)
        ]
        self.attendance_records = []

    def welcome_message(self):
        print("Selamat Datang di Sistem Absensi Online!")

    def login(self, user_type):
        if user_type == "dosen":
            username = input("Masukkan username dosen: ")
            password = input("Masukkan password dosen: ")
            for dosen in self.dosen:
                if dosen.username == username and dosen.password == password:
                    print(f"Login berhasil, Selamat datang {dosen.name}!")
                    return dosen
            print("Username atau password dosen salah.")
            return None
        elif user_type == "mahasiswa":
            username = input("Masukkan username mahasiswa: ")
            password = input("Masukkan password mahasiswa: ")
            for mahasiswa in self.mahasiswas:
                if mahasiswa.username == username and mahasiswa.password == password:
                    print(f"Login berhasil, Selamat datang {mahasiswa.name}!")
                    return mahasiswa
            print("Username atau password mahasiswa salah.")
            return None

    def record_attendance(self, dosen):
        print("\nMencatat Kehadiran Mahasiswa:")
        for mahasiswa in self.mahasiswas:
            status = input(f"Apakah {mahasiswa.name} hadir? (h/t): ")
            attendance_record = Attendance(mahasiswa, datetime.datetime.now().strftime("%Y-%m-%d"), status)
            self.attendance_records.append(attendance_record)
            mahasiswa.attendance_record.append(attendance_record)  
            print(f"Kehadiran {mahasiswa.name} telah dicatat sebagai {'Hadir' if status.lower() == 'h' else 'Tidak Hadir'}.")
        print("Pencatatan absensi selesai.\n")

    def view_attendance(self):
        table = PrettyTable() 
        table.field_names = ["Mahasiswa", "Tanggal", "Status"]  

        for record in self.attendance_records:
            status = "Hadir" if record.status.lower() == 'h' else "Tidak Hadir"
            table.add_row([record.mahasiswa.name, record.date, status])  
        print("\nRekap Kehadiran:")
        print(table)  

    def dosen_menu(self, dosen):
        while True:
            print("\nMenu Dosen:")
            print("1. Catat Kehadiran")
            print("2. Lihat Kehadiran")
            print("3. Kembali ke menu awal")
            print("4. Selesai (End)")

            choice = input("Masukkan pilihan Anda: ")

            if choice == "1":
                self.record_attendance(dosen)
            elif choice == "2":
                self.view_attendance()
            elif choice == "3":
                print("Kembali ke menu awal...")
                self.main()  
                break
            elif choice == "4":
                print("Program selesai. Terima kasih!")
                exit()
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def mahasiswa_menu(self, mahasiswa):
        while True:
            print("\nMenu Mahasiswa:")
            print("1. Lihat Kehadiran")
            print("2. Kembali ke menu awal")
            print("3. Selesai (End)")

            choice = input("Masukkan pilihan Anda: ")

            if choice == "1":
                if not mahasiswa.attendance_record:
                    print("Tidak ada riwayat kehadiran.")
                else:
                    print("Riwayat Kehadiran:")
                    for attendance in mahasiswa.attendance_record:
                        status = "Hadir" if attendance.status.lower() == 'h' else "Tidak Hadir"
                        print(f"Tanggal: {attendance.date}, Status: {status}")
            elif choice == "2":
                print("Kembali ke menu awal...")
                self.main()  
                break
            elif choice == "3":
                print("Program selesai. Terima kasih!")
                exit()
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def main(self):
        self.welcome_message()
        while True:
            user_type = input("Masuk sebagai dosen atau mahasiswa? (dosen/mahasiswa) ")
            if user_type.lower() == "dosen":
                user = self.login("dosen")
                if user is not None:
                    self.dosen_menu(user)
            elif user_type.lower() == "mahasiswa":
                user = self.login("mahasiswa")
                if user is not None:
                    self.mahasiswa_menu(user)
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

# Membuat instance Kampus dan menjalankan program
kampus = Kampus()
kampus.main()

