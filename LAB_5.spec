# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['LAB_5.py'],
             pathex=['/home/kekemon/Desktop/LAB/2_рік/2_семестр/АМО/LAB_4~'],
             binaries=[],
             datas=[('lab_files/*', 'lab_files/')],
             hiddenimports=['lab_files', 'matplotlib.pyplot', 'numpy', 'pkg_resources.py2_warn', 'numpy.core._dtype_ctypes', 'tkinter'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          Tree('lab_files', prefix='lab_files/'),
          a.zipfiles,
          a.datas,
          [],
          name='LAB_5',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
