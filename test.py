import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime

def valider_date_heure(date_heure_str):
    """Valide le format de la date et de l'heure."""
    try:
        datetime.strptime(date_heure_str, "%d/%m/%Y %H:%M")
        return True
    except ValueError:
        return False

def ajouter_rapport(auteur, date_heure, gravite, description):
    """Ajoute un rapport au fichier CSV."""
    if not valider_date_heure(date_heure):
        messagebox.showerror("Erreur", "Le format de la date et de l'heure est incorrect (JJ/MM/AAAA HH:MM).")
        return
    if not description.strip():
        messagebox.showerror("Erreur", "La description ne peut pas être vide.")
        return
    try:
        with open('rapports.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([auteur, date_heure, gravite, description.strip()])
        messagebox.showinfo("Succès", "Rapport ajouté avec succès.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue: {e}")

def afficher_interface():
    """Affiche l'interface graphique pour l'ajout de rapports."""
    window = tk.Tk()
    window.title("Gestion des rapports d'incidents")
    
    # Configuration de l'interface pour l'ajout d'un rapport
    tk.Label(window, text="Auteur:").grid(row=0, column=0, sticky="w")
    auteur_entry = tk.Entry(window)
    auteur_entry.grid(row=0, column=1, sticky="ew")

    tk.Label(window, text="Date et Heure (JJ/MM/AAAA HH:MM):").grid(row=1, column=0, sticky="w")
    date_heure_entry = tk.Entry(window)
    date_heure_entry.grid(row=1, column=1, sticky="ew")

    tk.Label(window, text="Gravité:").grid(row=2, column=0, sticky="w")
    gravite_combobox = ttk.Combobox(window, values=["Faible", "Moyenne", "Élevée"], state="readonly")
    gravite_combobox.grid(row=2, column=1, sticky="ew")

    tk.Label(window, text="Description:").grid(row=3, column=0, sticky="nw")
    description_text = tk.Text(window, height=5, width=50)
    description_text.grid(row=3, column=1, sticky="ew")

    tk.Button(window, text="Ajouter Rapport", command=lambda: ajouter_rapport(
        auteur_entry.get(), date_heure_entry.get(), gravite_combobox.get(), description_text.get("1.0", tk.END)
    )).grid(row=4, column=0, columnspan=2, pady=10)
    
    window.grid_columnconfigure(1, weight=1)  # Permet à la colonne de droite de s'ajuster avec la fenêtre
    window.mainloop()

if __name__ == "__main__":
    afficher_interface()
