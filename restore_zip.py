"""Restore the original ZIP. Open in Python IDLE and press F5."""
from hashlib import sha256
import json
from pathlib import Path
import shutil
from tempfile import NamedTemporaryFile

def restore(folder, destination):
    manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
    name = manifest["original_zip"]
    if Path(name).name != name or not name.lower().endswith(".zip"):
        raise ValueError("Invalid archive filename in manifest")
    target = destination / name
    if target.exists():
        with target.open("rb") as source:
            existing = sha256()
            for chunk in iter(lambda: source.read(1024 * 1024), b""):
                existing.update(chunk)
        if existing.hexdigest() == manifest["sha256"]:
            return target
        raise FileExistsError(f"A different file already exists at {target}. Choose another folder.")
    whole = sha256()
    temp = None
    try:
        with NamedTemporaryFile(dir=destination, delete=False) as handle:
            temp = Path(handle.name)
            for record in manifest["parts"]:
                part_name = record["name"]
                if Path(part_name).name != part_name:
                    raise ValueError("Invalid part name")
                data = (folder / part_name).read_bytes()
                if len(data) != record["bytes"] or sha256(data).hexdigest() != record["sha256"]:
                    raise ValueError(f"{part_name} is incomplete or changed.")
                handle.write(data)
                whole.update(data)
        if temp.stat().st_size != manifest["bytes"] or whole.hexdigest() != manifest["sha256"]:
            raise ValueError("The complete archive did not match its saved checksum.")
        with temp.open("rb") as src:
            with target.open("xb") as dst:
                try:
                    shutil.copyfileobj(src, dst, 1024 * 1024)
                except BaseException:
                    dst.close()
                    target.unlink(missing_ok=True)
                    raise
        return target
    finally:
        if temp is not None:
            temp.unlink(missing_ok=True)

if __name__ == "__main__":
    from tkinter import Tk, filedialog, messagebox
    window = Tk()
    window.withdraw()
    try:
        chosen = filedialog.askdirectory(title="Choose where to save the complete analysis ZIP")
        if chosen:
            result = restore(Path(__file__).resolve().parent, Path(chosen))
            messagebox.showinfo("Archive verified", f"Ready to extract:\n{result}")
    except Exception as error:
        messagebox.showerror("Could not restore the ZIP", str(error))
        raise
    finally:
        window.destroy()
