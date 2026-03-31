import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from PIL import Image, ImageTk 
from extractor import HtmlExtractor
from exporter import CsvExporter

class IdCardExtractorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Extrator de Dados")
        self.geometry("1000x750") 
        
        self.students_data = []
        self.selected_index = None
        self.current_preview = None 

        self.setup_ui()

    def setup_ui(self):
        top_frame = tk.Frame(self, pady=10)
        top_frame.pack(fill=tk.X, padx=10)

        btn_select_files = tk.Button(top_frame, text="1. Selecionar Arquivo(s)", command=self.load_files, width=25)
        btn_select_files.pack(side=tk.LEFT, padx=5)

        btn_export_csv = tk.Button(top_frame, text="3. Exportar CSV", command=self.export_data, width=20, bg="lightgreen")
        btn_export_csv.pack(side=tk.RIGHT, padx=5)

        paned_window = ttk.PanedWindow(self, orient=tk.VERTICAL)
        paned_window.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        mid_frame = tk.Frame(paned_window)
        paned_window.add(mid_frame, weight=1) 

        columns = ("Photo", "Name", "RG", "Birthdate")
        self.tree = ttk.Treeview(mid_frame, columns=columns, show="headings", selectmode="browse")
        
        self.tree.heading("Photo", text="Caminho da Foto")
        self.tree.heading("Name", text="Nome do Atleta")
        self.tree.heading("RG", text="RG / CPF")
        self.tree.heading("Birthdate", text="Data de Nascimento")
        
        self.tree.column("Photo", width=250)
        self.tree.column("Name", width=300)
        self.tree.column("RG", width=120, anchor=tk.CENTER)
        self.tree.column("Birthdate", width=120, anchor=tk.CENTER)

        scrollbar = ttk.Scrollbar(mid_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        bottom_frame = tk.LabelFrame(paned_window, text="2. Editar Aluno Selecionado", padx=10, pady=10)
        paned_window.add(bottom_frame, weight=0)

        form_frame = tk.Frame(bottom_frame)
        form_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Label(form_frame, text="Caminho da Foto:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry_photo = tk.Entry(form_frame, width=80) 
        self.entry_photo.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky=tk.W)

        tk.Label(form_frame, text="Nome:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_name = tk.Entry(form_frame, width=50) 
        self.entry_name.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        tk.Label(form_frame, text="RG:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.entry_rg = tk.Entry(form_frame, width=25)
        self.entry_rg.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        tk.Label(form_frame, text="Data Nasc:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.entry_birthdate = tk.Entry(form_frame, width=20)
        self.entry_birthdate.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        btn_frame = tk.Frame(bottom_frame)
        btn_frame.pack(side=tk.LEFT, padx=30)
        
        btn_update = tk.Button(btn_frame, text="Salvar\nAlterações", command=self.update_student, height=3, width=15)
        btn_update.pack()

        photo_frame = tk.Frame(bottom_frame, width=200, height=200, bg="lightgray", relief=tk.SUNKEN, borderwidth=1)
        photo_frame.pack(side=tk.RIGHT, padx=10)
        photo_frame.pack_propagate(False) 

        self.lbl_photo = tk.Label(photo_frame, text="Sem Imagem", bg="lightgray")
        self.lbl_photo.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def load_files(self):
        file_paths = filedialog.askopenfilenames(
            title="Selecione as fichas HTML",
            filetypes=[("Arquivos HTML", "*.html *.htm"), ("Todos os arquivos", "*.*")]
        )
        
        if not file_paths: return

        self.students_data.clear()
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.students_data, files_processed = HtmlExtractor.extract_from_files(file_paths)

        for index, student in enumerate(self.students_data):
            self.tree.insert("", tk.END, iid=str(index), values=(
                student["foto"], student["nome"], student["rg"], student["data_nascimento"]
            ))

        if files_processed == 0:
            messagebox.showwarning("Aviso", "Nenhum arquivo HTML/HTM válido foi processado.")
        else:
            messagebox.showinfo("Sucesso", f"Busca concluída! {len(self.students_data)} alunos extraídos.")

    def update_photo_preview(self, image_path):
        if not image_path or not os.path.exists(image_path):
            self.lbl_photo.config(image="", text="Foto não\nencontrada")
            self.current_preview = None
            return

        try:
            img = Image.open(image_path)
            img.thumbnail((190, 190)) 
            
            self.current_preview = ImageTk.PhotoImage(img)
            self.lbl_photo.config(image=self.current_preview, text="")
        except Exception as e:
            self.lbl_photo.config(image="", text="Erro ao carregar")
            self.current_preview = None

    def on_tree_select(self, event):
        selected_items = self.tree.selection()
        if not selected_items: return

        self.selected_index = int(selected_items[0])
        student = self.students_data[self.selected_index]

        self.entry_photo.delete(0, tk.END)
        self.entry_photo.insert(0, student["foto"])
        self.entry_name.delete(0, tk.END)
        self.entry_name.insert(0, student["nome"])
        self.entry_rg.delete(0, tk.END)
        self.entry_rg.insert(0, student["rg"])
        self.entry_birthdate.delete(0, tk.END)
        self.entry_birthdate.insert(0, student["data_nascimento"])

        self.update_photo_preview(student["foto"])

    def update_student(self):
        if self.selected_index is None:
            messagebox.showwarning("Aviso", "Selecione um aluno na tabela primeiro.")
            return

        new_path = self.entry_photo.get()
        new_name = self.entry_name.get()
        new_rg = self.entry_rg.get()
        new_birthdate = self.entry_birthdate.get()

        self.students_data[self.selected_index].update({
            "foto": new_path, "nome": new_name, "rg": new_rg, "data_nascimento": new_birthdate
        })

        self.tree.item(str(self.selected_index), values=(new_path, new_name, new_rg, new_birthdate))
        self.update_photo_preview(new_path)
        messagebox.showinfo("Atualizado", "Dados atualizados com sucesso!")

    def export_data(self):
        if not self.students_data:
            messagebox.showwarning("Aviso", "Não há dados para exportar.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv", filetypes=[("Arquivo CSV", "*.csv")], title="Salvar CSV como..."
        )

        if file_path:
            try:
                CsvExporter.export(self.students_data, file_path)
                messagebox.showinfo("Sucesso", "Arquivo CSV salvo com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao salvar:\n{e}")

if __name__ == "__main__":
    app = IdCardExtractorApp()
    app.mainloop()