from pathlib import Path



def get_info(dir: Path):
    if not dir.exists():
        print("Dir does not exist")
    else:
        return dir.read_text()
    
def store_info(dir: Path, info:str):
    if not dir.exists():
        print("Dir does not exist. Creating file")
        dir.touch()
    dir.write_text(info)
    

    
    
