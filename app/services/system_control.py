import subprocess

def lock_pc():
    subprocess.run(
        ["rundll32.exe", "user32.dll,LockWorkStation"],
        shell=True
    )
    return True