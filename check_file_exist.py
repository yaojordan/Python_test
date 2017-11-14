# Python 3.4
import os
import sys
import shutil
import glob

file_path = r'D:\CoreTracer\Shuttle\s1743\CoreTracer_x86\workspace\CachedFiles'

# TC304
gdbcmds = glob.glob('D:\CoreTracer\Shuttle\s1743\CoreTracer_x86\workspace\CachedFiles\*.gdbcmds')
gdb_index = glob.glob('D:\CoreTracer\Shuttle\s1743\CoreTracer_x86\workspace\CachedFiles\*.gdb-index')
gdb_index_elf = glob.glob('D:\CoreTracer\Shuttle\s1743\CoreTracer_x86\workspace\CachedFiles\*.gdb-index.elf')

try:
    while os.path.isdir(file_path):

        if sys.argv[1] == "TC303":
            if not gdb_index and not gdb_index_elf:
                # print("TC303 Pass")
                sys.exit(0)
            else:
                # print("TC303 Fail")
                sys.exit(1)

        elif sys.argv[1] == "TC304":
            # Check all three types of data exist
            # if list isn't empty
            if gdbcmds and gdb_index and gdb_index_elf:

                print("TC304 Pass")

                for data in gdb_index:
                    os.remove(data)
                for data in gdb_index_elf:
                    os.remove(data)

                sys.exit(0)

            else:
                sys.exit(1)

except Exception as e:
    print(e)
    sys.exit(1)