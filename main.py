#Projeto bloqueador de sites
import tkinter as tk
from tkinter import messagebox
import os

import ctypes
import subprocess
import sys

# Caminho para o arquivo hosts
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"  # Windows
# hosts_path = "/etc/hosts"  # Linux/Mac

redirect = "127.0.0.1"


# Aqui vai o código principal do bloqueador
print("Executando como administrador!")

class BloqueadorSitesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bloqueador de Sites")
        self.root.geometry("200x400")

        self.label = tk.Label(root, text="Sites para bloquear:")
        self.label.pack()

        self.text_area = tk.Text(root, height=10)
        self.text_area.pack()

        self.bloquear_button = tk.Button(root, text="Bloquear", command=self.bloquear_sites)
        self.bloquear_button.pack(pady=5)

        self.desbloquear_button = tk.Button(root, text="Desbloquear", command=self.desbloquear_sites)
        self.desbloquear_button.pack(pady=5)

        self.label_bloqueados = tk.Label(root, text="Sites atualmente bloqueados:")
        self.label_bloqueados.pack()

        self.lista_bloqueados = tk.Text(root, height=10, state="disabled")
        self.lista_bloqueados.pack()

        self.atualizar_lista_bloqueados()

    def bloquear_sites(self):
        
        
        
        sites = self.text_area.get("1.0", tk.END).strip().split("\n")
        if not sites:
            messagebox.showwarning("Atenção", "Digite pelo menos um site.")
            return

        try:
            with open(hosts_path, "r+") as file:
                conteudo = file.read()
                for site in sites:
                    site = site.strip()
                    if site and site not in conteudo:
                        file.write(f"{redirect} {site}\n")
            messagebox.showinfo("Sucesso", "Sites bloqueados com sucesso!")
            self.atualizar_lista_bloqueados()
        except PermissionError:
            messagebox.showerror("Erro", "Permissão negada! Rode como administrador.")

    def desbloquear_sites(self):
        sites = self.text_area.get("1.0", tk.END).strip().split("\n")
        try:
            with open(hosts_path, "r+") as file:
                conteudo = file.readlines()
                file.seek(0)
                for linha in conteudo:
                    if not any(site.strip() in linha for site in sites):
                        file.write(linha)
                file.truncate()
            messagebox.showinfo("Sucesso", "Sites desbloqueados com sucesso!")
            self.atualizar_lista_bloqueados()
        except PermissionError:
            messagebox.showerror("Erro", "Permissão negada! Rode como administrador.")

    def atualizar_lista_bloqueados(self):
        try:
            with open(hosts_path, "r") as file:
                conteudo = file.readlines()
            bloqueados = [linha.strip() for linha in conteudo if redirect in linha]
            self.lista_bloqueados.config(state="normal")
            self.lista_bloqueados.delete("1.0", tk.END)
            self.lista_bloqueados.insert(tk.END, "\n".join(bloqueados))
            self.lista_bloqueados.config(state="disabled")
        except Exception:
            self.lista_bloqueados.config(state="normal")
            self.lista_bloqueados.delete("1.0", tk.END)
            self.lista_bloqueados.insert(tk.END, "Erro ao ler o arquivo hosts.")
            self.lista_bloqueados.config(state="disabled")


# Executar o app
if __name__ == "__main__":
    root = tk.Tk()
    app = BloqueadorSitesApp(root)
    root.mainloop()

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    # Caminho para o script atual
    script = sys.argv[0]
    # Reexecuta o script como administrador
    subprocess.run(['powershell', '-Command',
                    f'Start-Process python -ArgumentList "{script}" -Verb runAs'])
    sys.exit()