
import sys
import os
import gc
import ctypes
import inspect
import threading
import time
import traceback
import hashlib
import random
import psutil
from types import FrameType, CodeType
 



os.environ["PYWEBVIEW_GUI"] = "edgechromium"
import webview
import requests
import re
import ctypes
from ctypes import c_longlong, sizeof, byref, c_void_p, c_size_t, c_bool, c_int, c_float, POINTER, Structure, wintypes, c_ulonglong
import pymem
from ctypes.wintypes import HANDLE, ULONG
import json
import threading
import random
import string
import time
import logging
import os
import urllib.request
import winreg
import tempfile
import shutil
import subprocess
import traceback
from pathlib import Path
from tkinter import Tk, filedialog
import sys
import keyboard
import pymem.process
import pymem.pattern
import win32gui









p = psutil.Process(os.getpid())
p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)



os.environ['WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS'] = (
    '--ignore-gpu-blocklist --enable-gpu-rasterization --enable-zero-copy '
    '--enable-hardware-overlays --enable-native-gpu-memory-buffers '
    '--num-raster-threads=4 --canvas-msaa-sample-count=0 --disable-low-res-tiling '
    '--disable-frame-rate-limit --disable-gpu-vsync --disable-checker-imaging '
    '--disable-features=PaintHolding,CalculateNativeWinOcclusion,msSmartScreenProtection,UseEcoQoSForBackgroundProcess,Vulkan,LayoutNG '
    '--disable-background-timer-throttling --disable-renderer-backgrounding '
    '--disable-best-effort-tasks --js-flags="--max-old-space-size=128 --scavenger_max_new_space_capacity_mb=16 --no-flush-bytecode" '
    '--disk-cache-size=1 --media-cache-size=1 --disable-background-networking '
    '--disable-component-update --disable-extensions --disable-hang-monitor '
    '--disable-notifications --disable-speech-api --disable-sync --disable-voice-input '
    '--enable-low-end-device-mode --disable-crash-reporter --disable-breakpad '
    '--disable-logging --disable-dev-shm-usage --disable-gpu-shader-disk-cache '
    '--disable-gpu-watchdog --disable-print-preview --disable-v8-idle-tasks '
    '--disable-client-side-phishing-detection --disable-sync-preferences '
    '--disable-default-apps --disable-domain-reliability --no-pings --mute-audio '
    '--no-first-run --no-default-browser-check --disable-ipc-flooding-protection '
    '--disable-backgrounding-occluded-windows --enable-begin-frame-control '
    '--disable-new-content-rendering-timeout --force-gpu-mem-available-mb=512'
)




import ctypes
from ctypes import *
from ctypes.wintypes import HANDLE
import random

# Global syscall ID cache
_syscall_id_cache = {}

# Structure definitions
class IO_STATUS_BLOCK(Structure):
    _fields_ = [
        ("Status", c_long),
        ("Information", c_void_p)
    ]

class CLIENT_ID(Structure):
    _fields_ = [
        ("UniqueProcess", c_void_p),
        ("UniqueThread", c_void_p)
    ]

class OBJECT_ATTRIBUTES(Structure):
    _fields_ = [
        ("Length", c_int),
        ("RootDirectory", c_void_p),
        ("ObjectName", c_void_p),
        ("Attributes", c_int),
        ("SecurityDescriptor", c_void_p),
        ("SecurityQualityOfService", c_void_p)
    ]

class PS_ATTRIBUTE(Structure):
    _fields_ = [
        ("Attribute", c_ulonglong),
        ("Size", c_size_t),
        ("Value", c_ulonglong),
        ("ReturnLength", POINTER(c_size_t))
    ]

class PS_ATTRIBUTE_LIST(Structure):
    _fields_ = [
        ("TotalLength", c_size_t),
        ("Attributes", PS_ATTRIBUTE * 1)
    ]

# NT API function definitions
ntdll = ctypes.windll.ntdll

NtProtectVirtualMemory = ntdll.NtProtectVirtualMemory
NtProtectVirtualMemory.argtypes = [HANDLE, POINTER(c_void_p), POINTER(c_size_t), c_int, POINTER(c_int)]
NtProtectVirtualMemory.restype = c_int

NtFlushInstructionCache = ntdll.NtFlushInstructionCache
NtFlushInstructionCache.argtypes = [HANDLE, c_void_p, c_size_t]
NtFlushInstructionCache.restype = c_int

NtCreateThreadEx = ntdll.NtCreateThreadEx
NtCreateThreadEx.argtypes = [POINTER(HANDLE), c_int, POINTER(OBJECT_ATTRIBUTES), HANDLE, c_void_p, c_void_p, c_int, c_size_t, c_size_t, c_size_t, c_void_p]
NtCreateThreadEx.restype = c_int

NtQueueApcThread = ntdll.NtQueueApcThread
NtQueueApcThread.argtypes = [HANDLE, c_void_p, c_void_p, c_void_p, c_void_p]
NtQueueApcThread.restype = c_int

NtAllocateVirtualMemory = ntdll.NtAllocateVirtualMemory
NtAllocateVirtualMemory.argtypes = [HANDLE, POINTER(c_void_p), c_ulonglong, POINTER(c_size_t), c_int, c_int]
NtAllocateVirtualMemory.restype = c_int

NtFreeVirtualMemory = ntdll.NtFreeVirtualMemory
NtFreeVirtualMemory.argtypes = [HANDLE, POINTER(c_void_p), POINTER(c_size_t), c_int]
NtFreeVirtualMemory.restype = c_int

NtWriteVirtualMemory = ntdll.NtWriteVirtualMemory
NtWriteVirtualMemory.argtypes = [HANDLE, c_void_p, c_void_p, c_size_t, POINTER(IO_STATUS_BLOCK)]
NtWriteVirtualMemory.restype = c_int

NtReadVirtualMemory = ntdll.NtReadVirtualMemory
NtReadVirtualMemory.argtypes = [HANDLE, c_void_p, c_void_p, c_size_t, POINTER(c_ulong)]
NtReadVirtualMemory.restype = c_int

NtDelayExecution = ntdll.NtDelayExecution
NtDelayExecution.argtypes = [c_bool, POINTER(c_longlong)]
NtDelayExecution.restype = c_int

NtCreateSection = ntdll.NtCreateSection
NtCreateSection.argtypes = [POINTER(c_void_p), c_ulong, c_void_p, POINTER(c_ulonglong), c_ulong, c_ulong, c_void_p]
NtCreateSection.restype = c_int

NtMapViewOfSection = ntdll.NtMapViewOfSection
NtMapViewOfSection.argtypes = [c_void_p, HANDLE, POINTER(c_void_p), c_ulonglong, c_size_t, c_void_p, POINTER(c_size_t), c_int, c_ulong, c_ulong]
NtMapViewOfSection.restype = c_int

NtUnmapViewOfSection = ntdll.NtUnmapViewOfSection
NtUnmapViewOfSection.argtypes = [HANDLE, c_void_p]
NtUnmapViewOfSection.restype = c_int

NtClose = ntdll.NtClose
NtClose.argtypes = [c_void_p]
NtClose.restype = c_int

# Memory protection constants
PAGE_EXECUTE_READWRITE = 0x40
PAGE_EXECUTE_READ = 0x20
PAGE_READWRITE = 0x04
PAGE_READONLY = 0x02
MEM_COMMIT = 0x1000
MEM_RESERVE = 0x2000
MEM_RELEASE = 0x8000

# Global syscall IDs dictionary
_syscall_ids = {}


class AdvancedSyscallEngine:
    def __init__(self, h_process, pid):
        self.h_process = h_process
        self.pid = pid
        self._code_caves = []
        self._stub_index = 0
        self._init_code_caves()

    def _resolve_syscall_id(self, func_name):
        """
        Extract syscall ID from ntdll export stub.
        Fast, minimal, and structured.
        """
        cached = _syscall_id_cache.get(func_name)
        if cached is not None:
            return cached

        kernel32 = ctypes.windll.kernel32

        try:
            ntdll = kernel32.GetModuleHandleW("ntdll.dll")
            if not ntdll:
                return None

            addr = kernel32.GetProcAddress(ntdll, func_name.encode("ascii"))
            if not addr:
                return None

            # Read stub directly (no copy)
            stub = (ctypes.c_ubyte * 32).from_address(addr)

            # Scan for mov eax, imm32 (0xB8)
            for i in range(28):
                if stub[i] == 0xB8:
                    syscall_id = (
                        stub[i + 1]
                        | (stub[i + 2] << 8)
                        | (stub[i + 3] << 16)
                        | (stub[i + 4] << 24)
                    )

                    if 0 < syscall_id < 0x1000:
                        _syscall_id_cache[func_name] = syscall_id
                        return syscall_id

            return None

        except (OSError, ValueError):
            return None

    def _init_code_caves(self):
        NUM_CAVES = 4
        CAVE_SIZE = 0x1000

        self._code_caves = []

        def _cleanup():
            """Free any allocated regions on failure."""
            for addr in self._code_caves:
                try:
                    base = c_void_p(addr)
                    size = c_size_t(0)
                    NtFreeVirtualMemory(
                        self.h_process,
                        byref(base),
                        byref(size),
                        MEM_RELEASE
                    )
                except Exception:
                    # Last-resort cleanup — ignore failures here
                    pass
            self._code_caves.clear()

        try:
            for i in range(NUM_CAVES):
                alloc_addr = c_void_p(0)
                region_size = c_size_t(CAVE_SIZE)

                # Step 1: Allocate as READ/WRITE (safer than RWX)
                status = NtAllocateVirtualMemory(
                    self.h_process,
                    byref(alloc_addr),
                    0,
                    byref(region_size),
                    MEM_COMMIT | MEM_RESERVE,
                    PAGE_READWRITE
                )

                if status != 0:
                    raise RuntimeError(
                        f"[CodeCave] Allocation failed at index {i} "
                        f"(NTSTATUS=0x{status:08X})"
                    )

                if not alloc_addr.value:
                    raise RuntimeError(f"[CodeCave] NULL allocation at index {i}")

                # Step 2: Change protection to EXECUTE_READ
                old_protect = c_ulong(0)
                protect_size = c_size_t(CAVE_SIZE)

                status = NtProtectVirtualMemory(
                    self.h_process,
                    byref(alloc_addr),
                    byref(protect_size),
                    PAGE_EXECUTE_READ,
                    byref(old_protect)
                )

                if status != 0:
                    raise RuntimeError(
                        f"[CodeCave] Protect failed at index {i} "
                        f"(NTSTATUS=0x{status:08X})"
                    )

                self._code_caves.append(alloc_addr.value)

            if len(self._code_caves) != NUM_CAVES:
                raise RuntimeError("[CodeCave] Incomplete allocation")

        except Exception as e:
            _cleanup()
            raise RuntimeError(f"_init_code_caves failed: {e}")

    def _protect_flush_write(self, addr, data):
        """
        Safely write bytes into a target process memory region.

        Steps:
            1. Temporarily change memory protection to PAGE_READWRITE.
            2. Write all bytes, handling partial writes.
            3. Restore the original memory protection.
            4. Flush the instruction cache.

        Returns:
            bool: True if the write succeeded, False otherwise.
        """
        if not addr or not data:
            return False

        size = len(data)
        if size == 0:
            return True  # nothing to write

        base_addr = c_void_p(addr)
        region_size = c_size_t(size)
        old_protect = c_ulong(0)

        try:
            # 1) Change protection → READWRITE
            status = NtProtectVirtualMemory(
                self.h_process,
                byref(base_addr),
                byref(region_size),
                PAGE_READWRITE,
                byref(old_protect)
            )
            if status != 0:
                return False

            # 2) Perform write (ensure full write)
            buffer = ctypes.create_string_buffer(data)
            total_written = 0

            while total_written < size:
                chunk_addr = addr + total_written
                remaining = size - total_written

                io_status = IO_STATUS_BLOCK()
                status = NtWriteVirtualMemory(
                    self.h_process,
                    chunk_addr,
                    ctypes.byref(buffer, total_written),
                    remaining,
                    byref(io_status)
                )

                if status != 0:
                    return False

                written = getattr(io_status, "Information", 0)
                if not written:
                    return False

                total_written += written

            # 3) Restore original protection
            tmp_protect = c_ulong(0)
            NtProtectVirtualMemory(
                self.h_process,
                byref(base_addr),
                byref(region_size),
                old_protect.value,
                byref(tmp_protect)
            )

            # 4) Flush instruction cache
            NtFlushInstructionCache(self.h_process, addr, size)

            return True

        except (OSError, ValueError):
            return False

    def _split_write(self, addr, data, chunk_size):
        """
        Chunked memory writer with controlled throttling.

        Features:
        - Full write guarantee per chunk
        - Single buffer allocation
        - Configurable delay (constant or ranged)
        """
        if not addr or not data:
            return False

        total_size = len(data)
        if total_size == 0:
            return True

        if chunk_size <= 0:
            return False

        # --- Throttling config (tune these) ---
        DELAY_MIN_MS = 1     # minimum delay per chunk
        DELAY_MAX_MS = 3     # maximum delay per chunk
        USE_JITTER = True    # toggle randomness

        try:
            buffer = ctypes.create_string_buffer(data)
            offset = 0

            while offset < total_size:
                remaining = total_size - offset
                current_size = chunk_size if remaining > chunk_size else remaining

                total_written = 0

                # --- Ensure full write of current chunk ---
                while total_written < current_size:
                    io_status = IO_STATUS_BLOCK()

                    status = NtWriteVirtualMemory(
                        self.h_process,
                        addr + offset + total_written,
                        ctypes.byref(buffer, offset + total_written),
                        current_size - total_written,
                        byref(io_status)
                    )

                    if status != 0:
                        return False

                    written = getattr(io_status, "Information", 0)
                    if not written:
                        return False

                    total_written += written

                offset += current_size

                # --- Controlled delay ---
                if DELAY_MAX_MS > 0:
                    if USE_JITTER:
                        delay_ms = random.uniform(DELAY_MIN_MS, DELAY_MAX_MS)
                    else:
                        delay_ms = DELAY_MIN_MS

                    # Convert ms → 100ns units (negative for relative time)
                    delay_interval = c_longlong(int(-10_000 * delay_ms))
                    NtDelayExecution(False, byref(delay_interval))

            return True

        except (OSError, ValueError):
            return False

    def advanced_write(self, addr, data):
        """
        Ultra‑stealthy memory write using exclusively ntdll APIs.
        Implements multiple evasion techniques with randomised ordering,
        micro‑delays, protection toggling, splitting, section mapping,
        and direct syscalls.
        """
        # ------------------------------------------------------------------
        # 1. Initial random delay (as in original)
        # ------------------------------------------------------------------
        syscall_id = self._resolve_syscall_id("NtWriteVirtualMemory")
        if syscall_id:
            delay = c_longlong(int(-10000 * random.uniform(0.01, 0.1)))
            NtDelayExecution(False, byref(delay))

        # ------------------------------------------------------------------
        # 2. Prepare data buffer and size
        # ------------------------------------------------------------------
        buf = ctypes.create_string_buffer(data)
        size = len(data)
        page_readwrite = 0x04          # PAGE_READWRITE

        # ------------------------------------------------------------------
        # 3. Helper: tiny random sleep using NtDelayExecution
        # ------------------------------------------------------------------
        def micro_sleep(seconds):
            """Sleep for a short random duration (seconds) using ntdll."""
            if seconds > 0:
                delay = c_longlong(int(-seconds * 10_000_000))
                NtDelayExecution(False, byref(delay))

        # ------------------------------------------------------------------
        # 4. Technique implementations (each returns bool)
        # ------------------------------------------------------------------

        def tech_protect_flush():
            """Change protection, write, restore, flush cache."""
            old_prot = ctypes.c_ulong()
            region_size = ctypes.c_size_t(size)
            status = NtProtectVirtualMemory(
                self.h_process,
                ctypes.byref(addr),
                ctypes.byref(region_size),
                page_readwrite,
                ctypes.byref(old_prot)
            )
            if status != 0:
                return False
            micro_sleep(random.uniform(0.001, 0.01))
            io_status = IO_STATUS_BLOCK()
            status = NtWriteVirtualMemory(
                self.h_process,
                addr,
                buf,
                size,
                byref(io_status)
            )
            NtProtectVirtualMemory(
                self.h_process,
                ctypes.byref(addr),
                ctypes.byref(region_size),
                old_prot.value,
                ctypes.byref(old_prot)
            )
            NtFlushInstructionCache(self.h_process, addr, size)
            return status == 0

        def tech_split_2():
            """Write in two random‑sized chunks."""
            split = random.randint(1, size - 1)
            chunk1 = data[:split]
            chunk2 = data[split:]
            if not self._split_write(addr, chunk1, 1):
                return False
            micro_sleep(random.uniform(0.001, 0.01))
            if not self._split_write(addr + split, chunk2, 1):
                return False
            return True

        def tech_split_3():
            """Write in three random‑sized chunks."""
            splits = sorted(random.sample(range(1, size), 2))
            chunk1 = data[:splits[0]]
            chunk2 = data[splits[0]:splits[1]]
            chunk3 = data[splits[1]:]
            offsets = [0, splits[0], splits[1]]
            for off, chunk in zip(offsets, [chunk1, chunk2, chunk3]):
                if not self._split_write(addr + off, chunk, 1):
                    return False
                micro_sleep(random.uniform(0.001, 0.01))
            return True

        def tech_direct():
            """Direct NtWriteVirtualMemory (original)."""
            io_status = IO_STATUS_BLOCK()
            status = NtWriteVirtualMemory(
                self.h_process,
                addr,
                buf,
                size,
                byref(io_status)
            )
            return status == 0

        def tech_nt_protect():
            """Use NtProtectVirtualMemory + NtWriteVirtualMemory (NT‑only)."""
            old_prot = ctypes.c_ulong()
            region_size = ctypes.c_size_t(size)
            status = NtProtectVirtualMemory(
                self.h_process,
                ctypes.byref(addr),
                ctypes.byref(region_size),
                page_readwrite,
                ctypes.byref(old_prot)
            )
            if status != 0:
                return False
            micro_sleep(random.uniform(0.001, 0.01))
            io_status = IO_STATUS_BLOCK()
            status = NtWriteVirtualMemory(
                self.h_process,
                addr,
                buf,
                size,
                byref(io_status)
            )
            NtProtectVirtualMemory(
                self.h_process,
                ctypes.byref(addr),
                ctypes.byref(region_size),
                old_prot.value,
                ctypes.byref(old_prot)
            )
            NtFlushInstructionCache(self.h_process, addr, size)
            return status == 0

        def tech_section_map():
            """Map a section, write via view, then unmap – avoids direct NtWriteVirtualMemory."""
            section_handle = ctypes.c_void_p()
            size_ulong = ctypes.c_ulonglong(size)
            status = NtCreateSection(
                ctypes.byref(section_handle),
                0xF001F,               # SECTION_ALL_ACCESS
                None,
                ctypes.byref(size_ulong),
                page_readwrite,
                0,
                0
            )
            if status != 0:
                return False
            view_base = ctypes.c_void_p()
            view_size = ctypes.c_size_t(size)
            status = NtMapViewOfSection(
                section_handle,
                self.h_process,
                ctypes.byref(view_base),
                0,
                view_size,
                None,
                ctypes.byref(view_size),
                1,
                0,
                page_readwrite
            )
            if status != 0:
                NtClose(section_handle)
                return False
            # Write data into the mapped view
            ctypes.memmove(view_base, buf, size)
            NtFlushInstructionCache(self.h_process, view_base, size)
            # Clean up
            NtUnmapViewOfSection(self.h_process, view_base)
            NtClose(section_handle)
            return True

        def tech_syscall():
            """Direct syscall (if available)."""
            if not hasattr(self, '_syscall_invoke'):
                return False
            status = self._syscall_invoke("NtWriteVirtualMemory", self.h_process, addr, buf, size)
            return status == 0

        # ------------------------------------------------------------------
        # 5. Build and rotate technique list
        # ------------------------------------------------------------------
        techniques = [
            tech_protect_flush,
            tech_split_2,
            tech_split_3,
            tech_direct,
            tech_nt_protect,
            tech_section_map,
            tech_syscall
        ]

        # Start at a random offset (based on stub_index) to spread out usage
        start_idx = self._stub_index % len(techniques)
        self._stub_index += 1

        # Try each technique in order, wrapping around
        for i in range(len(techniques)):
            tech = techniques[(start_idx + i) % len(techniques)]
            try:
                if tech():
                    return True
            except Exception:
                # Silently continue to next technique
                pass
            # Short random pause between attempts to avoid patterns
            micro_sleep(random.uniform(0.0005, 0.005))

        return False

    def advanced_read(self, addr, size):
        """
        Ultra‑stealthy memory read using only ntdll APIs and direct syscalls.
        Rotates through direct read, split‑read, and protection‑toggled read.
        Implements random delays and micro‑sleeps to break timing patterns.
        """
        # ------------------------------------------------------------------
        # 1. Initial random delay (timing obfuscation)
        # ------------------------------------------------------------------
        syscall_id = self._resolve_syscall_id("NtReadVirtualMemory")
        if syscall_id:
            delay = c_longlong(int(-10000 * random.uniform(0.01, 0.05)))
            NtDelayExecution(False, byref(delay))

        # ------------------------------------------------------------------
        # 2. Helper: micro‑sleep using NtDelayExecution
        # ------------------------------------------------------------------
        def micro_sleep(seconds):
            if seconds > 0:
                delay = c_longlong(int(-seconds * 10_000_000))
                NtDelayExecution(False, byref(delay))

        # ------------------------------------------------------------------
        # 3. Prepare buffer and get the optimal read function
        # ------------------------------------------------------------------
        # Use the direct syscall if available (most stealthy), otherwise fall back to ntdll's NtReadVirtualMemory.
        # In your code, you have 'nt_read_virtual_memory_syscall' defined globally.
        # Here we assume it's accessible via 'self.nt_read_syscall' – adjust as needed.
        read_func = getattr(self, 'nt_read_syscall', NtReadVirtualMemory)

        # ------------------------------------------------------------------
        # 4. Technique implementations (each returns bytes or None)
        # ------------------------------------------------------------------
        def tech_direct():
            """Direct read (syscall or ntdll)."""
            buffer = (ctypes.c_ubyte * size)()
            bytes_read = ctypes.c_ulong(0)
            status = read_func(
                self.h_process,
                addr,
                buffer,
                size,
                ctypes.byref(bytes_read)
            )
            if status == 0 and bytes_read.value > 0:
                return bytes(buffer[:bytes_read.value])
            return None

        def tech_split():
            """
            Split the read into 2–5 random‑sized chunks.
            Breaks large, contiguous read patterns.
            """
            # Determine number of chunks (2–5)
            num_chunks = random.randint(2, 5)
            # Generate random split points (ensuring each chunk >= 1 byte)
            if size <= num_chunks:
                # If size is smaller than number of chunks, just read directly
                return tech_direct()
            splits = sorted(random.sample(range(1, size), num_chunks - 1))
            chunks = []
            prev = 0
            for split in splits:
                chunks.append((prev, split - prev))
                prev = split
            chunks.append((prev, size - prev))

            result = bytearray()
            for offset, chunk_size in chunks:
                if chunk_size == 0:
                    continue
                buffer = (ctypes.c_ubyte * chunk_size)()
                bytes_read = ctypes.c_ulong(0)
                status = read_func(
                    self.h_process,
                    addr + offset,
                    buffer,
                    chunk_size,
                    ctypes.byref(bytes_read)
                )
                if status != 0 or bytes_read.value == 0:
                    return None
                result.extend(buffer[:bytes_read.value])
                micro_sleep(random.uniform(0.0005, 0.005))   # short random pause
            return bytes(result)

        def tech_protect_read():
            """
            Temporarily change memory protection to PAGE_READWRITE,
            read, then restore original protection.
            Useful if the target page is non‑readable (e.g., PAGE_NOACCESS).
            """
            old_prot = ctypes.c_ulong()
            region_size = ctypes.c_size_t(size)
            # Try to change protection (might fail if address is invalid)
            status = NtProtectVirtualMemory(
                self.h_process,
                ctypes.byref(addr),
                ctypes.byref(region_size),
                0x04,  # PAGE_READWRITE
                ctypes.byref(old_prot)
            )
            if status != 0:
                return None

            micro_sleep(random.uniform(0.001, 0.01))   # small pause after protection change

            buffer = (ctypes.c_ubyte * size)()
            bytes_read = ctypes.c_ulong(0)
            status = read_func(
                self.h_process,
                addr,
                buffer,
                size,
                ctypes.byref(bytes_read)
            )
            # Restore original protection (important to avoid leaving memory writable)
            NtProtectVirtualMemory(
                self.h_process,
                ctypes.byref(addr),
                ctypes.byref(region_size),
                old_prot.value,
                ctypes.byref(old_prot)
            )
            if status == 0 and bytes_read.value > 0:
                return bytes(buffer[:bytes_read.value])
            return None

        # ------------------------------------------------------------------
        # 5. Technique list and rotation
        # ------------------------------------------------------------------
        techniques = [
            tech_direct,         # fastest, least intrusive
            tech_split,          # pattern‑breaking
            tech_protect_read,   # for protected memory
        ]

        # Rotate starting point based on a persistent index
        start_idx = getattr(self, '_stub_index', 0) % len(techniques)
        self._stub_index = (self._stub_index + 1) if hasattr(self, '_stub_index') else 1

        # Try each technique in order (wrap around)
        for i in range(len(techniques)):
            tech = techniques[(start_idx + i) % len(techniques)]
            try:
                result = tech()
                if result is not None:
                    return result
            except Exception:
                # Silently continue – any failure is ignored
                pass
            micro_sleep(random.uniform(0.0005, 0.005))

        return None

    def cleanup(self):
        for cave_addr in self._code_caves:
            try:
                addr = c_void_p(cave_addr)
                size = c_size_t(0)
                NtFreeVirtualMemory(self.h_process, byref(addr), byref(size), MEM_RELEASE)
            except Exception:
                pass
        self._code_caves.clear()



class CLIENT_ID(Structure):
    _fields_ = [("UniqueProcess", c_void_p), ("UniqueThread", c_void_p)]

class OBJECT_ATTRIBUTES(Structure):
    _fields_ = [("Length", c_int), ("RootDirectory", c_void_p), ("ObjectName", c_void_p), ("Attributes", c_int), ("SecurityDescriptor", c_void_p), ("SecurityQualityOfService", c_void_p)]

class PS_ATTRIBUTE(Structure):
    _fields_ = [("Attribute", c_ulonglong), ("Size", c_size_t), ("Value", c_ulonglong), ("ReturnLength", POINTER(c_size_t))]

class PS_ATTRIBUTE_LIST(Structure):
    _fields_ = [("TotalLength", c_size_t), ("Attributes", PS_ATTRIBUTE * 1)]

NtProtectVirtualMemory = ntdll.NtProtectVirtualMemory
NtProtectVirtualMemory.argtypes = [HANDLE, POINTER(c_void_p), POINTER(c_size_t), c_int, POINTER(c_int)]
NtProtectVirtualMemory.restype = c_int

NtFlushInstructionCache = ntdll.NtFlushInstructionCache
NtFlushInstructionCache.argtypes = [HANDLE, c_void_p, c_size_t]
NtFlushInstructionCache.restype = c_int

NtCreateThreadEx = ntdll.NtCreateThreadEx
NtCreateThreadEx.argtypes = [POINTER(HANDLE), c_int, POINTER(OBJECT_ATTRIBUTES), HANDLE, c_void_p, c_void_p, c_int, c_size_t, c_size_t, c_size_t, c_void_p]
NtCreateThreadEx.restype = c_int

NtQueueApcThread = ntdll.NtQueueApcThread
NtQueueApcThread.argtypes = [HANDLE, c_void_p, c_void_p, c_void_p, c_void_p]
NtQueueApcThread.restype = c_int

NtAllocateVirtualMemory = ntdll.NtAllocateVirtualMemory
NtAllocateVirtualMemory.argtypes = [HANDLE, POINTER(c_void_p), c_ulonglong, POINTER(c_size_t), c_int, c_int]
NtAllocateVirtualMemory.restype = c_int

NtFreeVirtualMemory = ntdll.NtFreeVirtualMemory
NtFreeVirtualMemory.argtypes = [HANDLE, POINTER(c_void_p), POINTER(c_size_t), c_int]
NtFreeVirtualMemory.restype = c_int

PAGE_EXECUTE_READWRITE = 0x40
PAGE_READWRITE = 0x04
PAGE_READONLY = 0x02
MEM_COMMIT = 0x1000
MEM_RESERVE = 0x2000
MEM_RELEASE = 0x8000

_syscall_ids = {}

class GUITerminalLogger:
    def __init__(self, window):
        self.window = window
        self.buffer = []
        self.ready = False

    def mark_ready(self):
        if self.ready:
            return
        self.ready = True
        for line in self.buffer:
            self._send(line)
        self.buffer.clear()
        self._send("[SYSTEM] Terminal connected – showing backend logs")

    def _send(self, line):
        try:
            escaped = line.replace('\\', '\\\\').replace('"', '\\"').replace("'", "\\'")
            self.window.evaluate_js(f'logToTerminal("{escaped}")')
        except Exception as e:
            print(f"[Terminal send failed] {e}: {line}")

    def write(self, text):
        if not text or text.isspace():
            return
        lines = text.rstrip().split('\n')
        for line in lines:
            if line:
                if self.ready:
                    self._send(line)
                else:
                    self.buffer.append(line)

    def flush(self):
        pass

windowed = True
rpc_enabled = False  # always off

MANUAL_OFFSETS = {
    "SimAdaptiveUseNewVelocityCriteria": 0x67BCAF0,
    "InterpolationFrameVelocityThresholdMillionth": 0x676F778,
    "FullWindowMessages": 0x67ACE90,
    "RenderLocalLightFadeInMs": 0x6783668,
    "FixWallsOcclusion": 0x67C3BC8,
    "RenderHighlightTransparency": 0x67F5E20,
    "HighlightOutlinesOnMobile": 0x67F6530,
    "RenderPerformanceOverlay": 0x67F5DC0,
    "DebugHighlightSpecificFont": 0x67C0BF0,
    "LargeJohnson": 0x6f4a128,
    "BulletContactBreakChance": 0x6f4a1b0,
    "RagdollConstraintSolverIterationCount": 0x6f4a2a8,
    "FixRagdollSolverJank": 0x6f4a3c0,
    "DebugSimIntegrationStabilityTesting": 0x6f4a1a0,
    "SimFixAssemblyRadiusCalc": 0x6b4a6a7,
    "ISRLimitSimulationRadiusToNOUCount": 0x69AC0B4
}

kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_HIDE = 0
hWnd = kernel32.GetConsoleWindow()
if hWnd:
    user32.ShowWindow(hWnd, SW_HIDE)

kernel32.GetLastError.restype = wintypes.DWORD

APP_DIR = Path(os.path.expanduser("~")) / ".VSCode"
APP_DIR.mkdir(parents=True, exist_ok=True)
USER_FLAGS_FILE = APP_DIR / "plugin_config.json"
CONFIG_FILE = APP_DIR / "config.json"

DEFAULT_CONFIG = {
    "theme": "Samurai",
    "auto_apply_on_attach": True,
    "old_death_sound": False,
    "mouse_cursor": "default",
    "old_avatar_editor_background": False,
    "old_character_sounds": False,
    "emoji_type": "default",
    "use_custom_font": False,
    "custom_font_path": "",
    "hide_key": "insert",
    "safe_mode": True,
    "randomization": True,
    "timing_attack": True,
    "reapply": True,
    "offsetless": False,
    "batch_apply": False,
    "batch_size": 50,
    "batch_sleep_ms": 50
}

DEFAULT_FLAGS = []

if not USER_FLAGS_FILE.exists():
    USER_FLAGS_FILE.write_text(json.dumps(DEFAULT_FLAGS, indent=4))
if not CONFIG_FILE.exists():
    CONFIG_FILE.write_text(json.dumps(DEFAULT_CONFIG, indent=4))

try:
    existing_cfg = json.loads(CONFIG_FILE.read_text())

except Exception:
    pass

alrprinted = False

import psutil

import psutil

def find_roblox_processes():
    """
    Returns a list of PIDs for all running Roblox processes.
    Uses substring matching for better detection.
    """
    roblox_pids = []

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            name = proc.info['name']
            if name and "robloxplayer" in name.lower():  # substring search
                roblox_pids.append(proc.info['pid'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return roblox_pids






def get_module_base(pid):
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)

    TH32CS_SNAPMODULE = 0x00000008
    TH32CS_SNAPMODULE32 = 0x00000010
    INVALID_HANDLE_VALUE = ctypes.c_void_p(-1).value

    class MODULEENTRY32(ctypes.Structure):
        _fields_ = [
            ("dwSize", wintypes.DWORD),
            ("th32ModuleID", wintypes.DWORD),
            ("th32ProcessID", wintypes.DWORD),
            ("GlblcntUsage", wintypes.DWORD),
            ("ProccntUsage", wintypes.DWORD),
            ("modBaseAddr", ctypes.POINTER(ctypes.c_byte)),
            ("modBaseSize", wintypes.DWORD),
            ("hModule", wintypes.HMODULE),
            ("szModule", ctypes.c_char * 256),
            ("szExePath", ctypes.c_char * 260),
        ]

    CreateToolhelp32Snapshot = kernel32.CreateToolhelp32Snapshot
    Module32First = kernel32.Module32First
    Module32Next = kernel32.Module32Next
    CloseHandle = kernel32.CloseHandle

    CreateToolhelp32Snapshot.argtypes = [wintypes.DWORD, wintypes.DWORD]
    CreateToolhelp32Snapshot.restype = wintypes.HANDLE

    Module32First.argtypes = [wintypes.HANDLE, ctypes.POINTER(MODULEENTRY32)]
    Module32First.restype = wintypes.BOOL

    Module32Next.argtypes = [wintypes.HANDLE, ctypes.POINTER(MODULEENTRY32)]
    Module32Next.restype = wintypes.BOOL

    snapshot = CreateToolhelp32Snapshot(
        TH32CS_SNAPMODULE | TH32CS_SNAPMODULE32,
        pid
    )

    if snapshot == INVALID_HANDLE_VALUE:
        return None

    try:
        module_entry = MODULEENTRY32()
        module_entry.dwSize = ctypes.sizeof(MODULEENTRY32)

        # First module = main module (base)
        if not Module32First(snapshot, ctypes.byref(module_entry)):
            return None

        return ctypes.addressof(module_entry.modBaseAddr.contents)

    finally:
        CloseHandle(snapshot)


def fetch_fflag_offsets():
    url = "https://imtheo.lol/Offsets/FFlags.hpp"
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        matches = re.findall(r'uintptr_t\s+(\w+)\s*=\s*(0x[0-9A-Fa-f]+);', r.text)
        online = {name: int(offset, 16) for name, offset in matches}
        final = online.copy()
        final.update(MANUAL_OFFSETS)
        added = set(MANUAL_OFFSETS.keys()) - set(online.keys())
        print(f"[Windstrap] Loaded {len(final)} FFlags ")
        return final
    except Exception as e:
        print(f"[Wind] Offline mode: Using {len(MANUAL_OFFSETS)} manual offsets ({e})")
        return MANUAL_OFFSETS.copy()

FFLAGLIST_OFFSET = 0x7ce13d8

M_BASIS = 0xcbf29ce484222325
M_PRIME = 0x100000001b3
M_BASIS_ALT = 0x811c9dc5
M_PRIME_ALT = 0x01000193

OFF_FFLAG_VALUE_PTR = 0xC0

OFF_MAP_END = 0x00
OFF_MAP_LIST = 0x10
OFF_MAP_MASK = 0x28

OFF_ENTRY_FORWARD = 0x08
OFF_ENTRY_STRING = 0x10
OFF_ENTRY_GET_SET = 0x30

OFF_STR_BYTES = 0x00
OFF_STR_SIZE = 0x10
OFF_STR_CAPACITY = 0x18   # correct name: capacity of the allocated buffer
OFF_STR_ALLOC    = 0x18   # alias kept for compatibility

NODE_READ_SIZE    = 64    # always read exactly 64 bytes per node
NODE_STRIDES      = [64, 72, 56, 80, 88, 96]
MAX_CHAIN_STEPS   = 128
MAX_CHAIN_SAFETY  = 1000  # hard upper-bound: safe++ < 1000
MIN_VALID_PTR     = 0x10000
_FLAG_ADDR_LRU_MAX = 4096
KNOWN_FLAG_PREFIXES = (b"FFlag", b"DFInt", b"DFFlag", b"DFString", b"FInt", b"FString")

_pid_flag_addr_cache: dict = {}
_pid_map_struct_cache: dict = {}
_pid_stride_cache: dict = {}
_pid_bucket_cache: dict = {}   # hash-bucket cache: pid -> {bucket_idx: [node_ptr, ...]}


class New_no_offset_injector:
    def __init__(self, pm, safe_mode=False):
        self.pm = pm
        self.safe_mode = safe_mode
        self.h_process = pm.process_handle
        self.module = pymem.process.module_from_name(pm.process_handle, "RobloxPlayerBeta.exe")
        self._map_base_failed = False
        
        self._pid = getattr(pm, 'process_id', 0)
        
        if self._pid not in _pid_flag_addr_cache:
            _pid_flag_addr_cache[self._pid] = {}
        self.flag_addr_cache = _pid_flag_addr_cache[self._pid]
        
        if self._pid not in _pid_map_struct_cache:
            _pid_map_struct_cache[self._pid] = {}
        self._map_cache = _pid_map_struct_cache[self._pid]
        
        if self._pid not in _pid_stride_cache:
            _pid_stride_cache[self._pid] = {'stride': None, 'fails': []}
        self._stride_cache = _pid_stride_cache[self._pid]

        if self._pid not in _pid_bucket_cache:
            _pid_bucket_cache[self._pid] = {}
        self._bucket_cache = _pid_bucket_cache[self._pid]

    def get_map_base(self) -> int:
        if 'map_base' in self._map_cache:
            try:
                test = self.pm.read_ulonglong(self._map_cache['map_base'])
                if test != 0:
                    return self._map_cache['map_base']
            except Exception:
                del self._map_cache['map_base']
        
        addr = self.module.lpBaseOfDll + FFLAGLIST_OFFSET
        try:
            fflag_list_ptr = self.pm.read_ulonglong(addr)
            if fflag_list_ptr < MIN_VALID_PTR:
                self._map_base_failed = True
                return 0
            map_base = fflag_list_ptr + 8
            self.pm.read_bytes(map_base, 8)
            self._map_cache['map_base'] = map_base
            return map_base
        except Exception:
            self._map_base_failed = True
            return 0

    def get_singleton(self) -> int:
        return self.get_map_base()

    def _get_map_struct(self) -> tuple:
        if 'map_end' in self._map_cache and 'map_list' in self._map_cache:
            return self._map_cache['map_end'], self._map_cache['map_list'], self._map_cache['map_mask']
        
        map_base = self.get_map_base()
        if not map_base:
            return 0, 0, 0
        
        try:
            map_bytes = self.pm.read_bytes(map_base, 56)
        except Exception:
            return 0, 0, 0
        
        map_end  = int.from_bytes(map_bytes[OFF_MAP_END  : OFF_MAP_END  + 8], 'little')
        map_list = int.from_bytes(map_bytes[OFF_MAP_LIST : OFF_MAP_LIST + 8], 'little')
        map_mask = int.from_bytes(map_bytes[OFF_MAP_MASK : OFF_MAP_MASK + 8], 'little')
        
        if map_mask != 0 and map_list != 0:
            self._map_cache['map_end']  = map_end
            self._map_cache['map_list'] = map_list
            self._map_cache['map_mask'] = map_mask
            return map_end, map_list, map_mask
        
        for off_end, off_list, off_mask in [(0x00, 0x10, 0x28), (0x08, 0x18, 0x30), (0x00, 0x18, 0x38)]:
            me  = int.from_bytes(map_bytes[off_end  : off_end  + 8], 'little')
            ml  = int.from_bytes(map_bytes[off_list : off_list + 8], 'little')
            mm  = int.from_bytes(map_bytes[off_mask : off_mask + 8], 'little')
            if mm != 0 and ml > MIN_VALID_PTR:
                self._map_cache['map_end']  = me
                self._map_cache['map_list'] = ml
                self._map_cache['map_mask'] = mm
                return me, ml, mm
        
        return 0, 0, 0

    def _probe_stride(self, node_ptr: int) -> int:
        if self._stride_cache['stride'] is not None:
            return self._stride_cache['stride']
        
        candidates = [s for s in NODE_STRIDES if s not in self._stride_cache['fails']]
        if not candidates:
            self._stride_cache['fails'].clear()
            candidates = list(NODE_STRIDES)
        
        for stride in candidates:
            try:
                data = self.pm.read_bytes(node_ptr, stride)
                fwd = int.from_bytes(data[OFF_ENTRY_FORWARD : OFF_ENTRY_FORWARD + 8], 'little')
                s = OFF_ENTRY_STRING
                str_alloc = int.from_bytes(data[s + OFF_STR_ALLOC : s + OFF_STR_ALLOC + 8], 'little')
                if (fwd == 0 or fwd > MIN_VALID_PTR) and str_alloc < 0x10000:
                    self._stride_cache['stride'] = stride
                    return stride
            except Exception:
                if stride not in self._stride_cache['fails']:
                    self._stride_cache['fails'].append(stride)
        
        return NODE_STRIDES[0]

    def _ptr_aligned(self, ptr: int) -> bool:
        return ptr > MIN_VALID_PTR and (ptr & 0x7) == 0

    def _compute_fnv(self, name: str) -> int:
        basis = M_BASIS
        for char in name:
            basis ^= ord(char)
            basis = (basis * M_PRIME) & 0xFFFFFFFFFFFFFFFF
        return basis

    def _compute_fnv_alt(self, name: str) -> int:
        basis = M_BASIS_ALT
        for char in name:
            basis ^= ord(char)
            basis = (basis * M_PRIME_ALT) & 0xFFFFFFFF
        return basis

    def find_flag_addr(self, name: str) -> int:
        if name in self.flag_addr_cache:
            return self.flag_addr_cache[name]
        
        map_end, map_list, map_mask = self._get_map_struct()
        if map_mask == 0 or map_list == 0:
            return 0
        
        hash_primary = self._compute_fnv(name) & map_mask
        hash_alt     = self._compute_fnv_alt(name) & map_mask
        avg_chain    = max(1, len(self.flag_addr_cache) // max(1, map_mask + 1))
        adaptive_max = min(MAX_CHAIN_STEPS, max(32, avg_chain * 4))

        def scan_bucket(idx):
            # --- Hash bucket cache: return cached chain head if available ---
            cached_nodes = self._bucket_cache.get(idx)

            base = map_list + (idx * 16)
            try:
                bucket_data = self.pm.read_bytes(base, 24)
            except Exception:
                return 0

            current = int.from_bytes(bucket_data[8:16], 'little')
            if current == map_end or current < MIN_VALID_PTR:
                return 0

            # Seed the bucket cache with the chain head if not seen before
            if cached_nodes is None:
                self._bucket_cache[idx] = set()
                cached_nodes = self._bucket_cache[idx]

            steps = 0
            safe  = 0          # Node Chain Safety counter
            visited = set()

            while True:
                steps += 1
                safe  += 1
                # Better Node Chain Safety: hard cap at MAX_CHAIN_SAFETY (safe++ < 1000)
                if safe >= MAX_CHAIN_SAFETY:
                    break
                if steps > adaptive_max or current in visited:
                    break
                visited.add(current)
                cached_nodes.add(current)

                # --- Node Reading Size: always read exactly NODE_READ_SIZE (64) bytes ---
                try:
                    entry_data = self.pm.read_bytes(current, NODE_READ_SIZE)
                except Exception:
                    # Error Handling on Bad Node: continue to next node even if one fails
                    # Try to advance via the forward pointer using a minimal peek
                    try:
                        peek = self.pm.read_bytes(current + OFF_ENTRY_FORWARD, 8)
                        forward = int.from_bytes(peek, 'little')
                        if self._ptr_aligned(forward) and forward != current:
                            current = forward
                            continue
                    except Exception:
                        pass
                    break  # truly unreadable — stop chain

                s = OFF_ENTRY_STRING
                forward      = int.from_bytes(entry_data[OFF_ENTRY_FORWARD : OFF_ENTRY_FORWARD + 8], 'little')
                str_size     = int.from_bytes(entry_data[s + OFF_STR_SIZE     : s + OFF_STR_SIZE     + 8], 'little')
                # More Robust String Reading: use OFF_STR_CAPACITY (0x18) correctly
                # Small String Optimization: capacity <= 0xF means the string is stored inline
                str_capacity = int.from_bytes(entry_data[s + OFF_STR_CAPACITY : s + OFF_STR_CAPACITY + 8], 'little')

                if str_size < 1 or str_size > 256:
                    # Better Chain Walking: skip bad-size nodes instead of stopping
                    if not self._ptr_aligned(forward) or forward == current:
                        break
                    current = forward
                    continue

                entry_name = ""
                # SSO: capacity > 0xF means string is heap-allocated (ptr at offset s+0x00)
                #      capacity <= 0xF means string bytes are stored inline starting at s+0x00
                if str_capacity > 0xF:
                    ptr = int.from_bytes(entry_data[s : s + 8], 'little')
                    if self._ptr_aligned(ptr):
                        try:
                            entry_name = self.pm.read_bytes(ptr, str_size).decode('utf-8', errors='ignore').rstrip('\x00')
                        except Exception:
                            # Error Handling on Bad Node: continue chain even if string read fails
                            if self._ptr_aligned(forward) and forward != current:
                                current = forward
                            continue
                else:
                    # Inline small string — bytes live directly in the entry
                    try:
                        entry_name = entry_data[s : s + str_size].decode('utf-8', errors='ignore').rstrip('\x00')
                    except Exception:
                        if self._ptr_aligned(forward) and forward != current:
                            current = forward
                        continue

                if str_size == len(name) and entry_name == name:
                    get_set = int.from_bytes(entry_data[OFF_ENTRY_GET_SET : OFF_ENTRY_GET_SET + 8], 'little')
                    if self._ptr_aligned(get_set):
                        if len(self.flag_addr_cache) >= _FLAG_ADDR_LRU_MAX:
                            oldest = next(iter(self.flag_addr_cache))
                            del self.flag_addr_cache[oldest]
                        self.flag_addr_cache[name] = get_set
                        return get_set

                # Better Chain Walking: only stop if forward is truly invalid
                if not self._ptr_aligned(forward) or forward == current:
                    break
                current = forward

            return 0

        res = scan_bucket(hash_primary)
        if res:
            return res
        if hash_alt != hash_primary:
            res = scan_bucket(hash_alt)
            if res:
                return res
        return 0

    def find_flag(self, name: str):
        return self.find_flag_addr(name)

    def _flag_exists(self, name: str) -> bool:
        if self._map_base_failed:
            return False
        if not self.get_map_base():
            return False
        return self.find_flag_addr(name) != 0

    def get_string(self, name: str):
        addr = self.find_flag_addr(name)
        if not addr:
            return None
        try:
            fflag_struct = self.pm.read_bytes(addr, 0xD0)
            value_inst = int.from_bytes(fflag_struct[OFF_FFLAG_VALUE_PTR : OFF_FFLAG_VALUE_PTR+8], 'little')
            if not value_inst:
                return None
            buffer_ptr = self.pm.read_ulonglong(value_inst)
            length = self.pm.read_ulonglong(value_inst + 0x8)
            if length > 0:
                return self.pm.read_string(buffer_ptr, int(length))
            return ""
        except:
            return None

    def get_int(self, name: str):
        addr = self.find_flag_addr(name)
        if not addr:
            return None
        try:
            fflag_struct = self.pm.read_bytes(addr, 0xD0)
            value_ptr = int.from_bytes(fflag_struct[OFF_FFLAG_VALUE_PTR : OFF_FFLAG_VALUE_PTR+8], 'little')
            if not value_ptr:
                return None
            return self.pm.read_int(value_ptr)
        except:
            return None

    def get_float(self, name: str):
        addr = self.find_flag_addr(name)
        if not addr:
            return None
        try:
            fflag_struct = self.pm.read_bytes(addr, 0xD0)
            value_ptr = int.from_bytes(fflag_struct[OFF_FFLAG_VALUE_PTR : OFF_FFLAG_VALUE_PTR+8], 'little')
            if not value_ptr:
                return None
            return self.pm.read_float(value_ptr)
        except:
            return None

    def set_string(self, name: str, value: str):
        addr = self.find_flag_addr(name)
        if not addr:
            return False
        try:
            fflag_struct = self.pm.read_bytes(addr, 0xD0)
            value_inst = int.from_bytes(fflag_struct[OFF_FFLAG_VALUE_PTR : OFF_FFLAG_VALUE_PTR+8], 'little')
            if not value_inst:
                return False
            buffer_ptr = self.pm.read_ulonglong(value_inst)
            capacity = self.pm.read_ulonglong(value_inst + 0x10)
            new_value_bytes = value.encode('utf-8')
            new_len = len(new_value_bytes)
            if new_len > capacity:
                return False
            self.pm.write_bytes(buffer_ptr, new_value_bytes + b'\x00', new_len + 1)
            self.pm.write_ulonglong(value_inst + 0x8, new_len)
            return True
        except Exception:
            return False

    def set_int(self, name: str, value: int):
        addr = self.find_flag_addr(name)
        if not addr:
            return False
        try:
            fflag_struct = self.pm.read_bytes(addr, 0xD0)
            value_ptr = int.from_bytes(fflag_struct[OFF_FFLAG_VALUE_PTR : OFF_FFLAG_VALUE_PTR+8], 'little')
            if not value_ptr:
                return False
            self.pm.write_int(value_ptr, value)
            return True
        except:
            return False

    def set_float(self, name: str, value: float):
        addr = self.find_flag_addr(name)
        if not addr:
            return False
        try:
            fflag_struct = self.pm.read_bytes(addr, 0xD0)
            value_ptr = int.from_bytes(fflag_struct[OFF_FFLAG_VALUE_PTR : OFF_FFLAG_VALUE_PTR+8], 'little')
            if not value_ptr:
                return False
            self.pm.write_float(value_ptr, value)
            return True
        except:
            return False

    def close(self):
        pass

class Api:
    def __init__(self):
        self._window = None
        self._pm = None
        self._base = None
        self._connected_processes = {}
        self.all_offsets = {}
        self.offsets_lock = threading.Lock()
        self.config = self.load_config()
        self._original_values = {}
        self._suppress_guard = False
        self._guard_active = False
        self._auto_reapply_thread = None
        self.monitor_sleep = 30.0
        self._auto_reapply_enabled = bool(self.config.get('reapply', False))
        self._start_roblox_monitor()
        self._cache_all_offsets()
        self._start_auto_reapply()
        self.window_visible = True
        self.current_hide_key = self.config.get('hide_key', 'insert').lower()
        self._stealth_monitor_thread = None
        self._stealth_hide_active = False
        self._start_stealth_monitor()
        self._start_memory_cleaner()
        self.register_hide_hotkey()

    @staticmethod
    def find_hwnd_by_title(title):
        def enum_windows_callback(hwnd, windows):
            if win32gui.IsWindowVisible(hwnd) and title in win32gui.GetWindowText(hwnd):
                windows.append(hwnd)
        windows = []
        win32gui.EnumWindows(enum_windows_callback, windows)
        return windows[0] if windows else None

        
    def get_settings(self):
        return self.config

    def set_offsetless(self, enabled: bool):
        self.config['offsetless'] = bool(enabled)
        self.save_config()
        status = "enabled" if enabled else "disabled"
        print(f"[+] Offsetless Injection {status}")
        return {"ok": True}

    def set_batch_apply(self, enabled: bool, batch_size: int = 50, batch_sleep_ms: int = 50):
        self.config['batch_apply'] = bool(enabled)
        self.config['batch_size'] = max(1, int(batch_size))
        self.config['batch_sleep_ms'] = max(0, int(batch_sleep_ms))
        self.save_config()
        status = "enabled" if enabled else "disabled"
        print(f"[{'+' if enabled else '-'}] Batch Apply {status} | Size={self.config['batch_size']} | Sleep={self.config['batch_sleep_ms']}ms")
        return {"ok": True}

    def set_random(self, enabled: bool):
        self.config['randomization'] = bool(enabled)
        self.save_config()
        status = "enabled" if enabled else "disabled"
        print(f"[{'+' if enabled else '-'}] MWrite randomization {status}")
        return {"ok": True}

    def set_timing_attack(self, enabled: bool):
        self.config['timing_attack'] = bool(enabled)
        self.save_config()
        status = "enabled" if enabled else "disabled"
        print(f"[{'+' if enabled else '-'}] Timing injection {status}")
        return {"ok": True}

    def set_safe_mode(self, enabled: bool):
        self.config['safe_mode'] = bool(enabled)
        self.save_config()
        status = "enabled" if enabled else "disabled"
        print(f"[{'+' if enabled else '-'}] Safe Mode: Read/Write {status}")
        return {"ok": True}

    def set_reapply(self, enabled: bool):
        self.config['reapply'] = bool(enabled)
        self.save_config()
        self._auto_reapply_enabled = bool(enabled)
        status = "enabled" if enabled else "disabled"
        print(f"[{'+' if enabled else '-'}] Re-apply {status}")
        return {"ok": True}
        
    def get_offsetless_state(self):
        return {"offsetless": self.config.get('offsetless', False)}

    def register_hide_hotkey(self):
        try:
            keyboard.remove_hotkey(self.toggle_window_visibility)
        except:
            pass
        try:
            keyboard.add_hotkey(self.current_hide_key, self.toggle_window_visibility, suppress=True)
            print(f"[+] Registered key: {self.current_hide_key.upper()}")
        except Exception as e:
            print(f"[-] Failed to register '{self.current_hide_key}': {e}")

    def toggle_window_visibility(self):
        if not self._window:
            return
        if self.window_visible:
            self._window.hide()
            self.window_visible = False
            print("[-] Window HIDDEN")
        else:
            self._window.show()
            self.window_visible = True
            print("[+] Window SHOWN")

    def set_hide_key(self, key_name: str):
        key_lower = key_name.strip().lower()
        if not key_lower:
            return {"ok": False, "error": "No key provided"}

        allowed = {'insert', 'delete', 'home', 'end', 'page up', 'page down', 'esc',
                   'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12'}
        if key_lower in allowed or '+' in key_lower or len(key_lower.replace('+', '')) == 1:
            self.current_hide_key = key_lower
            self.config['hide_key'] = key_lower
            self.save_config()
            self.register_hide_hotkey()
            return {"ok": True, "message": f"keybind changed to: {key_lower.upper()}"}
        else:
            return {"ok": False, "error": "Unsupported key combination"}

    def get_official_flags(self):
        flags = self.fetch_official_flags()
        if flags is None:
            return None
        return list(flags)

    def load_json_safe(self, content):
        return self.safe_load_json(content)

    def filter_and_convert_flags(self, input_data, official_flags):
        return self.convert_and_filter_flags(input_data, official_flags)

    @staticmethod
    def clean_flag_name(name: str) -> str:
        prefixes = ["DFInt", "DFString", "DFFlag", "FInt", "FString", "FFlag"]
        for pre in prefixes:
            if name.startswith(pre):
                return name[len(pre):]
        return name

    @staticmethod
    def _parse_bool(value):
        return str(value).strip().lower() in ("true", "1")

    @staticmethod
    def _values_equal(current, desired, flag_type):
        if flag_type == "bool":
            return Api._parse_bool(current) == Api._parse_bool(desired)
        if flag_type == "int":
            try: return int(current) == int(desired)
            except: return False
        if flag_type in ("float", "double"):
            try: return abs(float(current) - float(desired)) < 1e-6
            except: return False
        return str(current) == str(desired)

    @staticmethod
    def _safe_encode(flag_type: str, value) -> tuple:
        import struct
        ft = flag_type.lower()
        if ft == "bool":
            b = 1 if str(value).strip().lower() in ("true", "1") else 0
            return (bytes([b & 0x01]), 1)
        elif ft == "int":
            try:
                ival = int(value)
            except Exception:
                ival = 0
            ival = max(-2147483648, min(2147483647, ival))
            return (ival.to_bytes(4, byteorder='little', signed=True), 4)
        elif ft in ("float", "double"):
            try:
                fval = float(value)
            except Exception:
                fval = 0.0
            return (struct.pack('<f', fval), 4)
        elif ft in ("log", "channel"):
            try:
                ival = int(value)
            except Exception:
                ival = 0
            if -128 <= ival <= 127:
                return (ival.to_bytes(1, byteorder='little', signed=True), 1)
            elif -32768 <= ival <= 32767:
                return (ival.to_bytes(2, byteorder='little', signed=True), 2)
            else:
                ival = max(-2147483648, min(2147483647, ival))
                return (ival.to_bytes(4, byteorder='little', signed=True), 4)
        else:
            s = str(value).encode('utf-8')[:255] + b'\x00'
            return (s, len(s))

    def _read_memory_safe_syscall(self, h_process, addr, flag_type):
        try:
            pid = getattr(self._pm, 'process_id', 0) if self._pm else 0
            if not hasattr(self, '_advanced_engines'):
                self._advanced_engines = {}
            if pid not in self._advanced_engines:
                self._advanced_engines[pid] = AdvancedSyscallEngine(h_process, pid)
            engine = self._advanced_engines[pid]
            size_map = {"bool": 1, "int": 4, "float": 4, "double": 4, "string": 256}
            size = size_map.get(flag_type, 256)
            data = engine.advanced_read(addr, size)
            if data is None:
                return None
            if flag_type == "bool":
                return "True" if data[0] else "False"
            elif flag_type == "int":
                return str(int.from_bytes(data[:4], byteorder='little', signed=True))
            elif flag_type in ("float", "double"):
                import struct
                return str(struct.unpack('<f', data[:4])[0])
            elif flag_type == "string":
                return data.split(b"\x00", 1)[0].decode("utf-8", errors="ignore")
            return None
        except Exception:
            try:
                if flag_type == "bool":
                    buffer = (ctypes.c_ubyte * 1)()
                    bytes_read = c_size_t()
                    status = NtReadVirtualMemory(h_process, addr, buffer, 1, byref(bytes_read))
                    if status == 0 and bytes_read.value == 1:
                        return "True" if buffer[0] else "False"
                    return None
                elif flag_type == "int":
                    buffer = (ctypes.c_ubyte * 4)()
                    bytes_read = c_size_t()
                    status = NtReadVirtualMemory(h_process, addr, buffer, 4, byref(bytes_read))
                    if status == 0 and bytes_read.value == 4:
                        return str(int.from_bytes(buffer, byteorder='little', signed=True))
                    return None
                elif flag_type in ("float", "double"):
                    buffer = (ctypes.c_ubyte * 4)()
                    bytes_read = c_size_t()
                    status = NtReadVirtualMemory(h_process, addr, buffer, 4, byref(bytes_read))
                    if status == 0 and bytes_read.value == 4:
                        import struct
                        return str(struct.unpack('<f', bytes(buffer))[0])
                    return None
                elif flag_type == "string":
                    buffer = (ctypes.c_ubyte * 256)()
                    bytes_read = c_size_t()
                    status = NtReadVirtualMemory(h_process, addr, buffer, 256, byref(bytes_read))
                    if status == 0:
                        b = bytes(buffer)
                        return b.split(b"\x00", 1)[0].decode("utf-8", errors="ignore")
                    return None
            except Exception:
                return None

    def _write_memory_safe_syscall(self, h_process, addr, encoded_bytes, byte_count):
        try:
            pid = getattr(self._pm, 'process_id', 0) if self._pm else 0
            if not hasattr(self, '_advanced_engines'):
                self._advanced_engines = {}
            if pid not in self._advanced_engines:
                self._advanced_engines[pid] = AdvancedSyscallEngine(h_process, pid)
            engine = self._advanced_engines[pid]
            return engine.advanced_write(addr, encoded_bytes)
        except Exception:
            try:
                buffer = (ctypes.c_ubyte * byte_count)(*encoded_bytes)
                io_status = IO_STATUS_BLOCK()
                status = NtWriteVirtualMemory(h_process, addr, buffer, byte_count, byref(io_status))
                return status == 0
            except Exception:
                return False

    def _read_memory(self, addr, flag_type, pm=None):
        target_pm = pm if pm else self._pm
        if not target_pm:
            raise RuntimeError("No pymem instance")
        
        safe_mode = self.config.get('safe_mode', True)
        
        if safe_mode:
            try:
                h_process = target_pm.process_handle
                result = self._read_memory_safe_syscall(h_process, addr, flag_type)
                if result is not None:
                    return result
            except Exception:
                pass
        
        try:
            if flag_type == "bool":
                return "True" if target_pm.read_bool(addr) else "False"
            elif flag_type == "int":
                try:
                    ptr = target_pm.read_ulonglong(addr)
                    if ptr > 0x10000:
                        return str(target_pm.read_int(ptr))
                except:
                    pass
                return str(target_pm.read_int(addr))
            elif flag_type in ("float", "double"):
                return str(target_pm.read_float(addr))
            elif flag_type == "string":
                try:
                    ptr = target_pm.read_ulonglong(addr)
                    target = ptr if ptr > 0x10000 else addr
                    b = target_pm.read_bytes(target, 256)
                    return b.split(b"\x00", 1)[0].decode("utf-8", errors="ignore")
                except:
                    return ""
        except:
            raise RuntimeError("Read failed")

    def _write_memory(self, addr, value, flag_type, max_retries=3, pm=None):
        target_pm = pm if pm else self._pm
        if not target_pm:
            return False, "No pymem"

        safe_mode = self.config.get('safe_mode', True)
        randomize = self.config.get('randomization', True)
        timing_attack = self.config.get('timing_attack', True)

        if randomize or timing_attack:
            delay = random.uniform(0.005, 0.001 if timing_attack else 0.002)
            time.sleep(delay)

        backoff = 0.05
        for attempt in range(max_retries + 1):
            try:
                if safe_mode:
                    encoded_bytes, byte_count = Api._safe_encode(flag_type, value)
                    h_process = target_pm.process_handle
                    
                    success = self._write_memory_safe_syscall(h_process, addr, encoded_bytes, byte_count)
                    
                    if not success:
                        raise Exception("Syscall write failed")
                else:
                    if flag_type == "bool":
                        target_pm.write_bool(addr, Api._parse_bool(value))
                    elif flag_type == "int":
                        ival = int(value)
                        try:
                            ptr = target_pm.read_ulonglong(addr)
                            target_pm.write_int(ptr if ptr > 0x10000 else addr, ival)
                        except:
                            target_pm.write_int(addr, ival)
                    elif flag_type in ("float", "double"):
                        target_pm.write_float(addr, float(value))
                    elif flag_type == "string":
                        b = str(value).encode("utf-8")[:255] + b"\x00"
                        try:
                            ptr = target_pm.read_ulonglong(addr)
                            target_pm.write_bytes(ptr if ptr > 0x10000 else addr, b, len(b))
                        except:
                            target_pm.write_bytes(addr, b, len(b))

                if self._values_equal(self._read_memory(addr, flag_type, pm=target_pm), value, flag_type):
                    if randomize:
                        time.sleep(random.uniform(0.001, 0.01))
                    return True, None

                raise Exception("Verification failed")

            except Exception as e:
                if attempt == max_retries:
                    return False, str(e)
                time.sleep(backoff)
                backoff *= 1.5 + random.random() * 0.5 if randomize else 2

        return False, "Max retries exceeded"

    def _start_auto_reapply(self):
        def reapply_daemon():
            while True:
                time.sleep(self.monitor_sleep)

                if not self._auto_reapply_enabled or self._suppress_guard:
                    continue

                if not self._connected_processes:
                    continue

                try:
                    flags = self.load_user_flags()
                    if not flags:
                        continue
                    
                    pids_needing_reapply = []
                    for pid, info in self._connected_processes.items():
                        if self._check_if_reapply_needed(flags, threshold_ratio=0.4, pm=info['pm'], base=info['base']):
                            pids_needing_reapply.append(pid)
                    
                    if not pids_needing_reapply:
                        continue

                    print(f"[Auto Reapply] Detected flag resets on PIDs {pids_needing_reapply} – reapplying...")
                    if self._window:
                        try:
                            self._window.evaluate_js('showToast("Flags reset detected – reapplying...", false)')
                        except: pass

                    result = self.apply_flags_to_roblox(
                        flags,
                        batch_size=150,
                        delay_between_batches=0.5 if not self.config.get('randomization', True) else random.uniform(0.1, 1),
                        max_retries=3 if self.config.get('timing_attack', True) else 2,
                        verbose=False,
                        target_pids=pids_needing_reapply
                    )

                    success = result.get('success', 0)
                    fail = result.get('fail', 0)
                    
                    if self._window and (success + fail) > 0:
                        msg = result.get('message', '')
                        escaped = msg.replace('\\', '\\\\').replace('"', '\\"')
                        is_error = fail > success
                        try:
                            self._window.evaluate_js(f'showToast("{escaped}", {str(is_error).lower()})')
                        except: pass
                    
                    if self.config.get('randomization', True):
                        time.sleep(random.uniform(0.1, 0.4))
                except Exception as e:
                    print(f"[Auto Reapply] Error: {e}")
                    time.sleep(1)

        self._auto_reapply_thread = threading.Thread(target=reapply_daemon, daemon=True)
        self._auto_reapply_thread.start()
        print(f"[Auto Reapply] Daemon started | Monitor: {self.monitor_sleep}s")

    def open_and_clean_file(self):
        if not self._window:
            return {"error": "Window not initialized."}
        files = self._window.create_file_dialog(
            webview.FileDialog.OPEN,
            allow_multiple=False,
            file_types=('JSON Files (*.json)', 'All Files (*.*)')
        )
        if not files:
            return {"error": "No file selected."}
        filepath = files[0]
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            content_json = self.safe_load_json(content)
            official_flags = self.fetch_official_flags()
            cleaned = self.convert_and_filter_flags(content_json, official_flags)
            return {"cleanedFlags": cleaned}
        except Exception as e:
            return {"error": f"Failed to process file: {str(e)}"}

    def cleanFlagsAndRenameFile(self):
        if not self._window:
            return {"error": "Window not initialized."}
        files = self._window.create_file_dialog(
            webview.FileDialog.OPEN,
            allow_multiple=False,
            file_types=('JSON Files (*.json)', 'All Files (*.*)')
        )
        if not files:
            return {"error": "No file selected."}
        return self.clean_flags_from_file(files[0], save_to_disk=True)

    @staticmethod
    def safe_load_json(content):
        try:
            return json.loads(content)
        except json.JSONDecodeError as e:
            idx = e.pos
            truncated = content[:idx]
            open_braces = truncated.count('{') - truncated.count('}')
            open_brackets = truncated.count('[') - truncated.count(']')
            truncated += '}' * open_braces + ']' * open_brackets
            try:
                return json.loads(truncated)
            except Exception:
                return {}

    @staticmethod
    def fetch_official_flags():
        url = "https://npdrlaufeimrkvdnjijl.supabase.co/functions/v1/get-offsets"
        try:
            response = requests.get(url, timeout=15)
            response.raise_for_status()
            text = response.text
            flags = re.findall(r'uintptr_t\s+(\w+)\s*=', text)
            return set(flags)
        except Exception as e:
            print(f"Warning: Failed to fetch official flags: {e}")
            return None

    @staticmethod
    def convert_and_filter_flags(input_data, valid_clean_names):
        def determine_type(val):
            val_str = str(val).lower()
            if val_str in ["true", "false"]:
                return "bool"
            try:
                int(val)
                return "int"
            except Exception:
                return "string" 

        result = []

        def process_flag(name: str, value):
            if valid_clean_names is None:
                final_name = name.strip()
            else:
                final_name = Api.clean_flag_name(name.strip())
            if valid_clean_names is not None and final_name not in valid_clean_names:
                return None

            val_str = "True" if str(value).lower() == "true" else "False" if str(value).lower() == "false" else str(value)
            val_type = determine_type(value)

            return {"name": final_name, "value": val_str, "type": val_type}

        if isinstance(input_data, dict):
            for key, value in input_data.items():
                processed = process_flag(key, value)
                if processed:
                    result.append(processed)

        elif isinstance(input_data, list):
            for item in input_data:
                if not isinstance(item, dict) or "name" not in item:
                    continue
                name = item["name"]
                value = item.get("value", "")
                processed = process_flag(name, value)
                if processed:
                    result.append(processed)

        return result

    def clean_flags_from_file(self, filepath, save_to_disk=True):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            return {"error": f"Failed to load file: {e}"}
        content_json = self.safe_load_json(content)
        official_flags = self.fetch_official_flags()
        try:
            cleaned = self.convert_and_filter_flags(content_json, official_flags)
        except Exception as e:
            return {"error": f"Unsupported format: {e}"}
        if save_to_disk:
            new_filename = self.random_filename()
            new_path = os.path.join(os.path.dirname(filepath), new_filename)
            try:
                with open(new_path, "w", encoding="utf-8") as f:
                    json.dump(cleaned, f, indent=4)
                return {"success": True, "message": f"Cleaned saved as {new_filename}", "path": new_path}
            except Exception as e:
                return {"error": f"Save failed: {e}"}
        return {"success": True, "flags": cleaned}

    @staticmethod
    def random_filename(prefix="", extension=".json", length=6):
        rand_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        return f"{prefix}{rand_str}{extension}"

    def export_flags(self, flags=None):
        if not self._window:
            return {"error": "Window not initialized."}
        
        if flags is None:
            flags = self.load_user_flags()
        
        export_dict = {}
        for flag in flags:
            name = flag.get("name", "").strip()
            value = flag.get("value", "").strip()
            if name:
                export_dict[name] = value
        
        result = self._window.create_file_dialog(
            webview.FileDialog.SAVE,
            allow_multiple=False,
            file_types=('JSON Files (*.json)', 'All Files (*.*)'),
            save_filename="my_fflags.json"
        )
        
        if not result or not result[0]:
            print("[-] Export cancelled by user")
            return {"error": "Export cancelled by user"}
        
        filepath = result[0]
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(export_dict, f, indent=4)
            print(f"[+] Exported {len(export_dict)} flags to {filepath} (simple dict format)")
            return {"success": True, "path": str(filepath)}
        except Exception as e:
            print(f"[-] Failed to export: {e}")
            return {"error": str(e)}
    
    def apply_engine_flag(self, name, value, ftype="string"):
        if not self._connected_processes:
            return {"success": 0, "fail": 1, "message": "Roblox not attached."}
        
        clean = self.clean_flag_name(name)
        use_no_offset = self.config.get('offsetless', False)
        
        with self.offsets_lock:
            offsets = self.all_offsets.copy()
        
        total_success = 0
        total_fail = 0
        
        for pid, info in self._connected_processes.items():
            pm = info['pm']
            base = info['base']
            ok = False
            try:
                if not use_no_offset and clean in offsets:
                    addr = base + offsets[clean]
                    ok, err = self._write_memory(addr, value, ftype, pm=pm)
                else:
                    injector = New_no_offset_injector(pm)
                    if not injector.get_singleton():
                        ok = False
                    else:
                        if ftype == "string":
                            ok = injector.set_string(clean, str(value))
                        elif ftype == "int":
                            ok = injector.set_int(clean, int(value))
                        elif ftype in ("float", "double"):
                            ok = injector.set_float(clean, float(value))
                        elif ftype == "bool":
                            ok = injector.set_int(clean, 1 if str(value).strip().lower() in ("true", "1") else 0)
                        else:
                            ok = injector.set_string(clean, str(value))
                if ok:
                    total_success += 1
                else:
                    total_fail += 1
            except Exception:
                total_fail += 1
        
        msg = f"Applied {clean} to {total_success} process(es)" if total_success > 0 else f"Failed to apply {clean}"
        return {"success": total_success, "fail": total_fail, "message": msg}

    def set_window(self, window):
        self._window = window
        
    def minimize_window(self):
        if self._window:
            self._window.minimize()
            
    def close_window(self):
        if self._window:
            self._window.destroy()
            
    def load_config(self):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                loaded = json.load(f)

            migrated = DEFAULT_CONFIG.copy()
            migrated.update({k: v for k, v in loaded.items() if k in migrated})

            if migrated != loaded:
                print("[CONFIG] Migrated old config – removed obsolete keys and added missing ones")
                try:
                    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
                        json.dump(migrated, f, indent=4)
                except Exception as save_err:
                    print(f"[CONFIG] Failed to save migrated config: {save_err}")

            return migrated

        except FileNotFoundError:
            print("[CONFIG] No config file found – using defaults")
            return DEFAULT_CONFIG.copy()

        except json.JSONDecodeError as e:
            print(f"[CONFIG] Corrupted config file – resetting to defaults: {e}")
            self.save_config()
            return DEFAULT_CONFIG.copy()

        except Exception as e:
            print(f"[CONFIG] Unexpected error loading config – using defaults: {e}")
            return DEFAULT_CONFIG.copy()

    def save_config(self):
        try:
            with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=4)
        except Exception as e:
            print(f"[CONFIG] Failed to save: {e}")
    

        
    def get_theme(self):
        return self.config.get('theme', 'white')
    
    def save_theme(self, theme):
        self.config['theme'] = theme
        self.save_config()

        print(f"[+] Changed to: {theme.replace('_', ' ').title()}")

        return {"ok": True}
        
    def set_stealth_mode(self, enabled: bool):
        enabled = bool(enabled)
        self.config['stealth_mode'] = enabled
        self.save_config()
        return {"ok": True}
    
    def _list_process_names(self):
        try:
            import subprocess
            out = subprocess.check_output(["tasklist"], creationflags=0x08000000)
            text = out.decode(errors='ignore').lower()
            return text
        except Exception:
            return ""
    
    def _start_stealth_monitor(self):
        if self._stealth_monitor_thread:
            return
        def loop():
            names = {
                "obs.exe", "obs64.exe", "bdcam.exe", "fraps.exe", "xboxgamebar.exe",
                "gamebar.exe", "nvspcaps64.exe", "nvcamera32.exe", "nvcamera64.exe",
                "sharex.exe", "camtasia.exe", "screenrecorder.exe", "gyazo.exe",
                "monosnap.exe", "flashbackrecorder.exe", "apowersoftscreenrecorder.exe"
            }
            while True:
                try:
                    enabled = bool(self.config.get('stealth_mode', False))
                    if enabled:
                        procs = self._list_process_names()
                        active = any(n in procs for n in names)
                        if active and self.window_visible:
                            if self._window:
                                try:
                                    self._window.hide()
                                    self.window_visible = False
                                    self._stealth_hide_active = True
                                except:
                                    pass
                        elif not active and self._stealth_hide_active and not self.window_visible:
                            if self._window:
                                try:
                                    self._window.show()
                                    self.window_visible = True
                                    self._stealth_hide_active = False
                                except:
                                    pass
                    else:
                        if self._stealth_hide_active and not self.window_visible and self._window:
                            try:
                                self._window.show()
                                self.window_visible = True
                                self._stealth_hide_active = False
                            except:
                                pass
                except:
                    pass
                time.sleep(1.5)
        import threading, time
        t = threading.Thread(target=loop, daemon=True)
        t.start()
        self._stealth_monitor_thread = t
        
    def _start_memory_cleaner(self):
        def clean_loop():
            try:
                psapi = ctypes.WinDLL('psapi.dll')
                psapi.EmptyWorkingSet.argtypes = [wintypes.HANDLE]
                psapi.EmptyWorkingSet.restype = wintypes.BOOL
            except Exception as e:
                print(f"[Memory Cleaner] Failed to load psapi: {e}")
                return

            while True:
                time.sleep(240)
                
                if not self._connected_processes:
                    continue

                cleaned_count = 0
                for pid in list(self._connected_processes.keys()):
                    try:
                        h_process = ctypes.windll.kernel32.OpenProcess(0x001F0FFF, False, pid)
                        if h_process:
                            psapi.EmptyWorkingSet(h_process)
                            ctypes.windll.kernel32.CloseHandle(h_process)
                            cleaned_count += 1
                    except Exception:
                        pass
                
                if cleaned_count > 0:
                    msg = f"[Memory Cleaner] Released memory for {cleaned_count} process(es)"
                    print(msg)
                    if self._window:
                        try:
                            self._window.evaluate_js(f'logToTerminal("{msg}", "success")')
                        except: pass

        t = threading.Thread(target=clean_loop, daemon=True)
        t.start()
        print("[Memory Cleaner] Daemon started | Interval: 4m")

    def get_settings(self):
        return {
            "auto_apply_on_attach": self.config.get('auto_apply_on_attach', False),
            "hide_key": self.config.get('hide_key', 'insert'),
            "safe_mode": self.config.get('safe_mode', True),
            "randomization": self.config.get('randomization', True),
            "timing_attack": self.config.get('timing_attack', True),
            "reapply": self.config.get('reapply', False),
            "offsetless": self.config.get('offsetless', False),
            "stealth_mode": self.config.get('stealth_mode', False),
            "batch_apply": self.config.get('batch_apply', False),
            "batch_size": self.config.get('batch_size', 50),
            "batch_sleep_ms": self.config.get('batch_sleep_ms', 50)
        }
    
    def get_preset_settings(self):
        return {
            "old_death_sound": self.config.get('old_death_sound', False),
            "mouse_cursor": self.config.get('mouse_cursor', 'default'),
            "old_avatar_editor_background": self.config.get('old_avatar_editor_background', False),
            "old_character_sounds": self.config.get('old_character_sounds', False),
            "emoji_type": self.config.get('emoji_type', 'default'),
            "use_custom_font": self.config.get('use_custom_font', False),
            "custom_font_path": self.config.get('custom_font_path', "")
        }
    
    def set_auto_apply_on_attach(self, enabled: bool):
        self.config['auto_apply_on_attach'] = bool(enabled)
        self.save_config()
        status = "enabled" if enabled else "disabled"
        print(f"[{'+' if enabled else '-'}] Auto-apply on attach {status}")
        return {"ok": True}
    
    def save_preset_settings(self, payload: dict):
        try:
            self.config['old_death_sound'] = bool(payload.get('old_death_sound', False))
            self.config['mouse_cursor'] = str(payload.get('mouse_cursor', 'default'))
            self.config['old_avatar_editor_background'] = bool(payload.get('old_avatar_editor_background', False))
            self.config['old_character_sounds'] = bool(payload.get('old_character_sounds', False))
            self.config['emoji_type'] = str(payload.get('emoji_type', 'default'))
            self.config['use_custom_font'] = bool(payload.get('use_custom_font', False))
            self.config['custom_font_path'] = str(payload.get('custom_font_path', ''))
            self.save_config()
            result = self.apply_nostalgia_presets()
            if "error" in result:
                print(f"[-] Failed to apply: {result['error']}")
                return {"ok": False, "error": result["error"]}
            else:
                print(f"[+] Successfully applied: {result.get('message', 'Presets applied!')}")
                return {"ok": True, "message": result.get("message", "Presets applied!")}
        except Exception as e:
            print(f"[-] Error: {str(e)}")
            return {"ok": False, "error": str(e)}
        
    def apply_custom_font(self):
        font_path = self.config.get('custom_font_path', '')
        if not font_path or not os.path.exists(font_path):
            return {"error": "No custom font selected or file not found."}
        version_folder = self.find_roblox_version_folder()
        if not version_folder:
            return {"error": "Roblox installation not found."}
        fonts_dir = os.path.join(version_folder, "content", "fonts")
        if not os.path.exists(fonts_dir):
            return {"error": "Fonts directory not found in Roblox installation."}
        target_fonts = [
            "AccanthisADFStd-Regular.ttf", "AmaticSC-Bold.ttf", "AmaticSC-Regular.ttf", "Arimo-Bold.ttf",
            "Arimo-Regular.ttf", "Balthazar-Regular.ttf", "Bangers-Regular.ttf", "BuilderExtended-Bold.ttf",
            "BuilderExtended-Regular.ttf", "BuilderExtended-SemiBold.ttf", "BuilderMono-Bold.ttf",
            "BuilderMono-Light.ttf", "BuilderMono-Regular.ttf", "BuilderSans-Bold.ttf",
            "BuilderSans-ExtraBold.ttf", "BuilderSans-Medium.ttf", "BuilderSans-Regular.ttf",
            "ComicNeue-Angular-Bold.ttf", "Creeper-Regular.ttf", "DenkOne-Regular.ttf",
            "Fondamento-Italic.ttf", "Fondamento-Regular.ttf", "FredokaOne-Regular.ttf",
            "GothamBlack.ttf", "GothamBold.ttf", "GothamBook.ttf", "GothamMedium.ttf",
            "GothamSemiBold.ttf", "GrenzeGotisch-Bold.ttf", "GrenzeGotisch-Regular.ttf",
            "Guru-Regular.ttf", "HWYGOTH.ttf", "Inconsolata-Regular.ttf", "IndieFlower-Regular.ttf",
            "JosefinSans-Regular.ttf", "Jura-Regular.ttf", "Kalam-Regular.ttf", "LuckiestGuy-Regular.ttf",
            "Merriweather-Italic.ttf", "Merriweather-Regular.ttf", "Michroma-Regular.ttf",
            "Montserrat-Black.ttf", "Montserrat-Bold.ttf", "Montserrat-Light.ttf", "Montserrat-Medium.ttf",
            "Montserrat-Regular.ttf", "Montserrat-SemiBold.ttf", "NotoNastArabicUI-Regular.ttf",
            "NotoSansBengaliUI-Regular.ttf", "NotoSansDevanagariUI-Regular.ttf", "NotoSansGeorgian-Regular.ttf",
            "NotoSansKhmerUI-Regular.ttf", "NotoSansMyanmarUI-Regular.ttf", "NotoSansSinhalaUI-Regular.ttf",
            "NotoSansThaiUI-Regular.ttf", "Nunito-Regular.ttf", "Oswald-Bold.ttf", "Oswald-Regular.ttf",
            "PatrickHand-Regular.ttf", "PermanentMarker-Regular.ttf", "PressStart2P-Regular.ttf",
            "Roboto-Bold.ttf", "Roboto-Italic.ttf", "Roboto-Mono-Regular.ttf",
            "Roboto-Regular.ttf", "RobotoCondensed-Regular.ttf", "RomanAntique.ttf", "Sarpanch-Bold.ttf",
            "Sarpanch-Regular.ttf", "SourceSans.ttf", "SourceSansBold.ttf", "SourceSansItalic.ttf",
            "SourceSansLight.ttf", "SourceSansPro-Bold.ttf", "SourceSansPro-Light.ttf",
            "SourceSansPro-Regular.ttf", "SourceSansPro-SemiBold.ttf", "SourceSansSemiBold.ttf",
            "SpecialElite-Regular.ttf", "TitilliumWeb-Bold.ttf", "TitilliumWeb-Regular.ttf",
            "Ubuntu-Italic.ttf", "Ubuntu-Regular.ttf", "zekton_rg.ttf",
        ]
        replaced = []
        skipped = []
        failed = []
        for target in target_fonts:
            dest = os.path.join(fonts_dir, target)
            if not os.path.exists(dest):
                skipped.append(target)
                continue
            try:
                shutil.copy2(font_path, dest)
                replaced.append(target)
            except PermissionError:
                failed.append(f"{target}: Permission denied – Run as Administrator!")
            except Exception as e:
                failed.append(f"{target}: {str(e)}")
        total_applied = len(replaced)
        if total_applied > 0:
            return {
                "success": True,
                "message": f"Custom font applied to {total_applied} font files! Relaunch Roblox to see full changes.",
                "applied_count": total_applied,
                "replaced": replaced[:10],
                "note": f"{len(skipped)} files skipped (not present in this version)"
            }
        else:
            return {
                "error": "No font files were replaced.",
                "details": failed or ["Run Windstrap as Administrator and try again."]
            }
        
    def choose_custom_font(self):
        try:
            root = Tk()
            root.withdraw()
            path = filedialog.askopenfilename(
                title="Select Custom Font (.ttf or .otf)",
                filetypes=[("Font files", "*.ttf *.otf"), ("All files", "*.*")]
            )
            root.destroy()
            if path:
                self.config['custom_font_path'] = path
                self.save_config()
                result = self.apply_custom_font()
                if self._window:
                    if result.get("success"):
                        print(f"[FONT] Custom font applied to {result['applied_count']} files")
                        msg = result["message"]
                        self._window.evaluate_js(f'showToast("{msg}", false)')
                    else:
                        print(f"[FONT] Failed to apply custom font")
                        err = result.get("error", "Failed to apply font")
                        self._window.evaluate_js(f'showToast("{err}", true)')
                return result
            return {"path": ""}
        except Exception as e:
            return {"error": str(e)}

    def _check_if_reapply_needed(self, flags, threshold_ratio=0.5, pm=None, base=None):
        target_pm = pm if pm else self._pm
        target_base = base if base else self._base

        if not target_pm or not target_base or not self.all_offsets:
            return True

        with self.offsets_lock:
            offsets = self.all_offsets.copy()

        wrong_count = 0
        total = len(flags)

        if total == 0:
            return False

        for flag in flags:
            clean_name = self.clean_flag_name(flag["name"])
            if clean_name not in offsets:
                continue

            addr = target_base + offsets[clean_name]
            desired_value = flag["value"]
            ftype = flag.get("type", "bool").lower()

            try:
                current = self._read_memory(addr, ftype, pm=target_pm)
                if not self._values_equal(current, desired_value, ftype):
                    wrong_count += 1
            except:
                wrong_count += 1

        return (wrong_count / total) >= threshold_ratio

    def _auto_apply_for_pid(self, pid):
        time.sleep(4)
        flags = self.load_user_flags()
        if not flags:
            return

        try:
            result = self.apply_flags_to_roblox(flags, target_pids=[pid])
            msg = result.get("message", "Auto-apply completed")
            print(f"[Auto Apply] PID {pid}: {msg}")
            if self._window:
                escaped_msg = f"PID {pid}: {msg}".replace('\\', '\\\\').replace('"', '\\"')
                try:
                    self._window.evaluate_js(f'showToast("{escaped_msg}", false)')
                except: pass
        except Exception as e:
            print(f"[Auto Apply] PID {pid} Failed: {e}")

    def _start_roblox_monitor(self):
        def monitor():
            last_running = False
            was_attached = False

            while True:
                try:
                    current_pids = find_roblox_processes()
                    
                    known_pids = set(self._connected_processes.keys())
                    found_pids = set(current_pids)
                    
                    new_pids = found_pids - known_pids
                    lost_pids = known_pids - found_pids
                    
                    for pid in lost_pids:
                        print(f"[-] Roblox process {pid} detached")
                        if pid in self._connected_processes:
                            del self._connected_processes[pid]
                            
                    for pid in new_pids:
                        try:
                            pm = pymem.Pymem(pid)
                            base = get_module_base(pid)
                            if base:
                                self._connected_processes[pid] = {'pm': pm, 'base': base}
                                print(f"[+] Attached to Roblox process {pid}")
                                if self.config.get('auto_apply_on_attach', False):
                                    threading.Thread(target=self._auto_apply_for_pid, args=(pid,), daemon=True).start()
                        except Exception as e:
                            print(f"[-] Failed to attach to {pid}: {e}")

                    if self._connected_processes:
                        first_pid = next(iter(self._connected_processes))
                        self._pm = self._connected_processes[first_pid]['pm']
                        self._base = self._connected_processes[first_pid]['base']
                        state = 'attached'
                    else:
                        self._pm = None
                        self._base = None
                        state = 'not_running' if not current_pids else 'running'

                    if self._window:
                        try:
                            count = len(self._connected_processes)
                            self._window.evaluate_js(f'window.updateRobloxStatus("{state}", {count})')
                            if new_pids:
                                 self._window.evaluate_js(f'showToast("Attached to {len(new_pids)} new instance(s)", false)')
                        except:
                            pass
                except Exception as e:
                    print(f"[Monitor] Error: {e}")
                
                time.sleep(1)

        threading.Thread(target=monitor, daemon=True).start()

    def _cache_all_offsets(self):
        def cache_task():
            offsets = fetch_fflag_offsets()
            if offsets:
                with self.offsets_lock:
                    self.all_offsets = offsets
                if self._window:
                    try:
                        preset_list = sorted(list(offsets.keys()))
                        self._window.evaluate_js(f'window.populatePresetFlags({json.dumps(preset_list)})')
                    except Exception as e:
                        print(f"JS eval error in cache offsets: {e}")
        threading.Thread(target=cache_task, daemon=True).start()

    def load_user_flags(self):
        try:
            with open(USER_FLAGS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if not isinstance(data, list):
                return DEFAULT_FLAGS[:]
            return [{**f, 'type': f.get('type', 'bool')} for f in data if isinstance(f, dict) and 'name' in f and 'value' in f] or DEFAULT_FLAGS[:]
        except Exception:
            return DEFAULT_FLAGS[:]

    def save_user_flags(self, flags):
        with self.offsets_lock:
            valid = set(self.all_offsets.keys())
        cleaned = [f for f in flags if self.clean_flag_name(f["name"]) in valid]
        try:
            with open(USER_FLAGS_FILE, 'w', encoding='utf-8') as f:
                json.dump(cleaned, f, indent=4)
            print(f"[+] Saved {len(cleaned)} flags to disk")
            return {"status": "success"}
        except Exception as e:
            print(f"[-] Failed to save flags: {e}")
            return {"status": "error", "message": str(e)}

    def import_from_json(self):
        if not self._window:
            return {"error": "Window not initialized."}

        result = self._window.create_file_dialog(
            webview.FileDialog.OPEN,
            allow_multiple=True,
            file_types=('JSON Files (*.json)', 'All Files (*.*)')
        )

        if not result or not result:
            print("[-] Import cancelled by user")
            return {"error": "Import cancelled by user"}

        use_offsetless = self.config.get('offsetless', False)
        
        if use_offsetless:
            print("[IMPORT] Offsetless mode ON → NO prefix cleaning, NO filtering")
            should_clean = False
            should_filter = False
        else:
            print("[IMPORT] Classic offset mode → prefix cleaning + filtering active")
            should_clean = True
            should_filter = True

        official_flags = self.fetch_official_flags() or set()

        with self.offsets_lock:
            known_names = official_flags.union(self.all_offsets.keys())

        all_imported_flags = []
        file_count = len(result)

        for filepath in result:
            print(f"[+] Loading flags from {filepath}")
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                content_json = self.safe_load_json(content)

                if should_clean:
                    processed = self.convert_and_filter_flags(content_json, valid_clean_names=known_names)
                else:
                    processed = self.convert_and_filter_flags(content_json, valid_clean_names=None)

                all_imported_flags.extend(processed)
                print(f"[+] Loaded {len(processed)} flags from {os.path.basename(filepath)}")

            except Exception as e:
                print(f"[-] Failed to process {filepath}: {e}")
                continue

        if not all_imported_flags:
            return {"error": "No valid flags found in selected files."}

        seen = {}
        for flag in all_imported_flags:
            name = flag["name"]
            seen[name] = flag

        unique_flags = list(seen.values())

        print(f"[+] Imported and merged {len(unique_flags)} unique flags from {file_count} file(s)")
        return {"flags": unique_flags, "file_count": file_count}
    
    def kill_roblox(self):
        print("[+] Attempting to terminate Roblox process...")
        try:
            result = subprocess.run(
                ['taskkill', '/F', '/IM', 'RobloxPlayerBeta.exe'],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                print("[+] Roblox process terminated successfully")
                return {"success": True}
            else:
                print(f"[-] Failed to terminate Roblox: {result.stderr.strip() or 'Unknown error'}")
                return {"error": result.stderr.strip() or "Unknown error"}
        except Exception as e:
            print(f"[-] Exception: {e}")
            return {"error": str(e)}

    def apply_flags_to_roblox(self, flags, batch_size=100, delay_between_batches=0.3, max_retries=3, verbose=False, target_pids=None):
        logger = logging.getLogger(__name__)
        total_input = len(flags)
        print(f"[APPLY] Starting injection for {total_input} flags...")

        if not self._connected_processes:
            print("[-] Apply failed: Roblox is not attached")
            return {"success": 0, "fail": len(flags), "removed": 0, "message": "Roblox not attached."}

        if target_pids:
            targets = {pid: self._connected_processes[pid] for pid in target_pids if pid in self._connected_processes}
        else:
            targets = self._connected_processes

        if not targets:
            return {"success": 0, "fail": len(flags), "removed": 0, "message": "No valid target processes found."}

        use_no_offset = self.config.get('offsetless', False)

        with self.offsets_lock:
            if not self.all_offsets and not use_no_offset:
                print("[-] Apply failed: FFlag offsets not loaded yet")
                return {"success": 0, "fail": len(flags), "removed": 0, "message": "FFlag offsets not loaded yet."}
            offsets = self.all_offsets.copy()

        filtered_flags = []
        removed_flags = []
        for flag in flags:
            original_name = flag.get('name', '')
            if not original_name:
                continue
            if use_no_offset:
                filtered_flags.append(flag)
            else:
                clean_name = self.clean_flag_name(original_name)
                if clean_name in offsets:
                    flag['clean_name'] = clean_name
                    filtered_flags.append(flag)
                else:
                    removed_flags.append(original_name)

        if removed_flags:
            print(f"[-] Removed {len(removed_flags)} invalid/unknown flags")
        
        try:
            self.save_user_flags(filtered_flags)
        except Exception: pass

        total_success = 0
        total_fail = 0
        all_errors = []

        print(f"[+] Applying to {len(targets)} process(es)")

        # Batch apply config
        use_batch = self.config.get('batch_apply', False)
        cfg_batch_size = max(1, int(self.config.get('batch_size', 50)))
        cfg_batch_sleep = max(0, int(self.config.get('batch_sleep_ms', 50)))  # in ms

        for pid, info in targets.items():
            pm = info['pm']
            base = info['base']
            print(f"[+] Injecting into PID {pid}...")
            
            success_count = 0
            fail_count = 0

            if use_no_offset:
                injector = New_no_offset_injector(pm)
                if not injector.get_singleton():
                    total_fail += len(filtered_flags)
                    continue

                flag_chunks = [filtered_flags[i:i+cfg_batch_size] for i in range(0, len(filtered_flags), cfg_batch_size)] if use_batch else [filtered_flags]

                for chunk_idx, chunk in enumerate(flag_chunks):
                    if use_batch and chunk_idx > 0 and cfg_batch_sleep > 0:
                        delay = c_longlong(int(-10000 * cfg_batch_sleep))
                        NtDelayExecution(False, byref(delay))

                    for flag in chunk:
                        name = flag.get('name')
                        value = flag.get('value')
                        flag_type = flag.get('type', 'string').lower()
                        
                        if name not in self._original_values:
                            try:
                                prev = None
                                if flag_type == 'string':
                                    prev = injector.get_string(name) or ""
                                elif flag_type in ('int', 'bool'):
                                    i = injector.get_int(name)
                                    if flag_type == 'bool':
                                        prev = "True" if (i or 0) != 0 else "False"
                                    else:
                                        prev = str(i) if i is not None else "0"
                                elif flag_type in ('float', 'double'):
                                    f = injector.get_float(name)
                                    prev = str(f) if f is not None else "0.0"
                                if prev is not None:
                                    self._original_values[name] = prev
                            except Exception: pass

                        set_success = False
                        try:
                            if flag_type == 'string':
                                set_success = injector.set_string(name, value)
                            elif flag_type == 'int':
                                set_success = injector.set_int(name, int(value))
                            elif flag_type == 'bool':
                                set_success = injector.set_int(name, 1 if self._parse_bool(value) else 0)
                            elif flag_type in ('float', 'double'):
                                set_success = injector.set_float(name, float(value))
                        except Exception: pass

                        if set_success:
                            success_count += 1
                        else:
                            fail_count += 1
            else:
                flag_chunks = [filtered_flags[i:i+cfg_batch_size] for i in range(0, len(filtered_flags), cfg_batch_size)] if use_batch else [filtered_flags]

                for chunk_idx, chunk in enumerate(flag_chunks):
                    if use_batch and chunk_idx > 0 and cfg_batch_sleep > 0:
                        delay = c_longlong(int(-10000 * cfg_batch_sleep))
                        NtDelayExecution(False, byref(delay))

                    for flag in chunk:
                        clean_name = flag.get('clean_name')
                        value = flag.get('value')
                        ftype = flag.get('type', 'string').lower()
                        addr = base + offsets[clean_name]
                        
                        if flag.get('name') not in self._original_values:
                            try:
                                if ftype == "bool":
                                    self._original_values[flag.get('name')] = "True" if pm.read_bool(addr) else "False"
                                elif ftype == "int":
                                    self._original_values[flag.get('name')] = str(pm.read_int(addr))
                            except: pass

                        try:
                            if ftype == "bool":
                                pm.write_bool(addr, str(value).lower() == "true")
                            elif ftype == "int":
                                ival = int(value)
                                try:
                                    ptr = pm.read_ulonglong(addr)
                                    if ptr and ptr > 0x10000: pm.write_int(ptr, ival)
                                    else: pm.write_int(addr, ival)
                                except: pm.write_int(addr, ival)
                            elif ftype in ("float", "double"):
                                pm.write_float(addr, float(value))
                            elif ftype == "string":
                                s = str(value)
                                b = s.encode("utf-8") + b"\x00"
                                try:
                                    str_ptr = pm.read_ulonglong(addr)
                                    target = str_ptr if (str_ptr and str_ptr > 0x10000) else addr
                                    pm.write_bytes(target, b, len(b))
                                except: pm.write_bytes(addr, b, len(b))
                            success_count += 1
                        except:
                            fail_count += 1
            
            total_success += success_count
            total_fail += fail_count

        result_msg = f"Applied to {len(targets)} instance(s). Total Success: {total_success}, Failed: {total_fail}"
        
        if self._window:
            try:
                self._window.evaluate_js(f'showToast("{result_msg}", {str(total_fail > 0).lower()})')
            except Exception: pass

        return {
            "success": total_success,
            "fail": total_fail,
            "removed": len(removed_flags),
            "message": result_msg,
            "errors": all_errors
        }


    def uninject_flags(self, batch_size=100, delay_between_batches=0.3, max_retries=3, verbose=False, target_pids=None):
        if not self._connected_processes:
            print("[-] Uninject failed: Roblox is not attached")
            return {"success": 0, "fail": 0, "message": "Roblox not attached."}
        
        if target_pids:
            targets = {pid: self._connected_processes[pid] for pid in target_pids if pid in self._connected_processes}
        else:
            targets = self._connected_processes

        if not targets:
            return {"success": 0, "fail": 0, "message": "No valid target processes found."}
        
        use_no_offset = self.config.get('offsetless', False)
        offsets = {}
        if not use_no_offset:
            with self.offsets_lock:
                if not self.all_offsets:
                    print("[-] Uninject failed: FFlag offsets not loaded yet")
                    return {"success": 0, "fail": 0, "message": "FFlag offsets not loaded yet."}
                offsets = self.all_offsets.copy()
        
        original_items = list(self._original_values.items())
        total_flags = len(original_items)
        
        if total_flags == 0:
            print("[+] No flags to restore – nothing injected previously")
            self._guard_active = False
            self._auto_reapply_enabled = False
            return {"success": 0, "fail": 0, "message": "No previously injected flags to restore."}
        
        print(f"[UNINJECT] Starting restoration for {total_flags} flags on {len(targets)} process(es)...")
        
        total_success = 0
        total_fail = 0
        all_errors = []
        
        self._suppress_guard = True
        
        def infer_type(value):
            if isinstance(value, str):
                val_lower = value.lower()
                if val_lower in ("true", "false"):
                    return "bool"
                try:
                    int(value)
                    return "int"
                except:
                    try:
                        float(value)
                        return "float"
                    except:
                        return "string"
            return "string" 

        for pid, info in targets.items():
            pm = info['pm']
            base = info['base']
            success_count = 0
            fail_count = 0
            
            if use_no_offset:
                injector = New_no_offset_injector(pm)
                if not injector.get_singleton():
                    total_fail += total_flags
                    continue
                
                for name, original in original_items:
                    ftype = infer_type(original)
                    ok = False
                    try:
                        if ftype == "bool":
                            ok = injector.set_int(name, 1 if str(original).lower() == "true" else 0)
                        elif ftype == "int":
                            ok = injector.set_int(name, int(original))
                        elif ftype in ("float", "double", "float64"):
                            ok = injector.set_float(name, float(original))
                        elif ftype == "string":
                            ok = injector.set_string(name, str(original))
                    except: pass
                    
                    if ok: success_count += 1
                    else: fail_count += 1
            else:
                for name, original in original_items:
                    clean_name = self.clean_flag_name(name)
                    if clean_name not in offsets:
                        fail_count += 1
                        continue
                    
                    addr = base + offsets[clean_name]
                    ftype = infer_type(original)
                    
                    try:
                        if ftype == "bool":
                            pm.write_bool(addr, str(original).lower() == "true")
                        elif ftype == "int":
                            ival = int(original)
                            try:
                                ptr = pm.read_ulonglong(addr)
                                if ptr and ptr > 0x10000: pm.write_int(ptr, ival)
                                else: pm.write_int(addr, ival)
                            except: pm.write_int(addr, ival)
                        elif ftype in ("float", "double"):
                            pm.write_float(addr, float(original))
                        elif ftype == "string":
                            s = str(original)
                            b = s.encode("utf-8") + b"\x00"
                            try:
                                str_ptr = pm.read_ulonglong(addr)
                                target = str_ptr if (str_ptr and str_ptr > 0x10000) else addr
                                pm.write_bytes(target, b, len(b))
                            except: pm.write_bytes(addr, b, len(b))
                        success_count += 1
                    except:
                        fail_count += 1
            
            total_success += success_count
            total_fail += fail_count

        self._original_values.clear()
        self._guard_active = False
        self._auto_reapply_enabled = False
        
        result_msg = f"Restored on {len(targets)} instance(s). Total Success: {total_success}, Failed: {total_fail}"
        
        if self._window:
            try:
                self._window.evaluate_js(f'showToast("{result_msg}", {str(total_fail > total_success).lower()})')
            except: pass
        
        print(f"[UNINJECT] {result_msg}")
        
        return {
            "success": total_success,
            "fail": total_fail,
            "message": result_msg,
            "errors": all_errors
        }

    def find_roblox_version_folder(self):
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Roblox\Environments\roblox-player")
            value, _ = winreg.QueryValueEx(key, "VersionFolder")
            winreg.CloseKey(key)
            path = os.path.join(os.getenv("LOCALAPPDATA"), "Roblox", "Versions", value)
            if os.path.exists(path):
                return path
        except Exception:
            pass
        versions_dir = os.path.join(os.getenv("LOCALAPPDATA"), "Roblox", "Versions")
        if os.path.exists(versions_dir):
            for folder in os.listdir(versions_dir):
                full = os.path.join(versions_dir, folder)
                if os.path.isdir(full) and os.path.exists(os.path.join(full, "RobloxPlayerBeta.exe")):
                    return full
        return None
    
    def apply_nostalgia_presets(self):
        presets = self.get_preset_settings()
        version_folder = self.find_roblox_version_folder()
        if not version_folder:
            return {"error": "Roblox installation not found."}
        content_root = version_folder
        replaced = 0
        restored = 0
        failed = []
        files_to_apply = []

        backup_dir = APP_DIR / "cursor_backups"
        backup_dir.mkdir(parents=True, exist_ok=True)
        backup_arrow = backup_dir / "default_ArrowCursor.png"
        backup_far = backup_dir / "default_ArrowFarCursor.png"
        cursor_path = os.path.join(content_root, "content", "textures", "Cursors", "KeyboardMouse")
        arrow_path = os.path.join(cursor_path, "ArrowCursor.png")
        far_path = os.path.join(cursor_path, "ArrowFarCursor.png")

        if not backup_arrow.exists() and os.path.exists(arrow_path):
            try:
                shutil.copy2(arrow_path, backup_arrow)
            except Exception as e:
                failed.append(f"Backup ArrowCursor: {str(e)}")
        if not backup_far.exists() and os.path.exists(far_path):
            try:
                shutil.copy2(far_path, backup_far)
            except Exception as e:
                failed.append(f"Backup ArrowFarCursor: {str(e)}")

        cursor_preset = presets["mouse_cursor"]
        cursor_name_map = {
            "default": "Default",
            "classic": "Classic",
            "blackdot": "Black Dot",
            "whitedot": "White Dot",
            "diamondsword": "Diamond Sword",
            "pink": "Pink Cross",
            "girl": "Girl"
        }
        cursor_display = cursor_name_map.get(cursor_preset.lower(), "Unknown")

        if cursor_preset.lower() != "default":
            cursor_url = {
                "classic": "https://www.rw-designer.com/cursor-view/134299.png",
                "blackdot": "https://www.rw-designer.com/cursor-view/150775.png",
                "whitedot": "https://www.rw-designer.com/cursor-view/150777.png",
                "diamondsword": "https://www.rw-designer.com/cursor-view/69125.png",
                "pink": "https://www.rw-designer.com/cursor-view/138479.png",
                "girl": "https://www.rw-designer.com/cursor-view/124576.png",
            }.get(cursor_preset.lower())

            if cursor_url:
                files_to_apply.extend([
                    ("ArrowCursor.png", cursor_url, os.path.join("content", "textures", "Cursors", "KeyboardMouse", "ArrowCursor.png")),
                    ("ArrowFarCursor.png", cursor_url, os.path.join("content", "textures", "Cursors", "KeyboardMouse", "ArrowFarCursor.png"))
                ])
                replaced += 2
                print(f"[+] Changed to: {cursor_display}")
        else:
            if backup_arrow.exists() and backup_far.exists():
                try:
                    os.makedirs(cursor_path, exist_ok=True)
                    shutil.copy2(backup_arrow, arrow_path)
                    shutil.copy2(backup_far, far_path)
                    restored += 2
                    print(f"[+] Restored to: Default")
                except Exception as e:
                    failed.append(f"Restore cursor: {str(e)}")
                    
        if presets["old_death_sound"]:
            files_to_apply.append(("ouch.ogg", "https://archive.org/download/ouch_20240329/ouch.ogg", os.path.join("content", "sounds", "ouch.ogg")))
        if files_to_apply:
            with tempfile.TemporaryDirectory() as tmpdir:
                for filename, source, rel_path in files_to_apply:
                    dest = os.path.join(content_root, rel_path)
                    try:
                        src = os.path.join(tmpdir, filename)
                        req = urllib.request.Request(source, headers={'User-Agent': 'Mozilla/5.0'})
                        with urllib.request.urlopen(req) as response, open(src, 'wb') as out_file:
                            shutil.copyfileobj(response, out_file)
                        os.makedirs(os.path.dirname(dest), exist_ok=True)
                        shutil.copy2(src, dest)
                        replaced += 1
                    except Exception as e:
                        failed.append(f"{filename}: {str(e)}")
        msg_parts = []
        if replaced > 0:
            msg_parts.append(f"Applied {replaced} files.")
        if restored > 0:
            msg_parts.append(f"Restored {restored} originals.")
        if not msg_parts:
            msg = "No changes needed."
        else:
            msg = " ".join(msg_parts)
        if failed:
            msg += f" Failed: {', '.join(failed[:3])}"
        return {"success": True, "message": msg.strip() + " Relaunch Roblox for changes!"}
    
        print(f"[PRESETS] Applied nostalgia settings: {msg}")

html=r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WINDSTRAP</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    <style>
        :root {
            /* Base Theme Variables (Default: Black) */
            --bg-body: #0a0a0a;
            --bg-body-img: none;
            --text-main: #e0e0e0;
            --text-muted: #9ca3af;
            --text-accent: #4285f4;
            
            --bg-sidebar: rgba(13, 13, 13, 0.75);
            --border-sidebar: rgba(26, 26, 26, 0.5);
            
            --bg-card: #000000;
            --bg-card-alt: #111111;
            --border-card: #1f2937;
            
            --bg-modal: #1a1a1a;
            --border-modal: #333333;
            
            --bg-input: #1a1a1a;
            --border-input: #333333;
            --text-input: #e0e0e0;
            
            --bg-btn-primary: #4285f4;
            --bg-btn-primary-hover: #3367d6;
            --text-btn-primary: #ffffff;
            
            --bg-btn-secondary: #2a2a2a;
            --bg-btn-secondary-hover: #333333;
            --text-btn-secondary: #e0e0e0;
            --border-btn-secondary: #333333;
            
            --bg-btn-danger: rgba(42, 26, 26, 0.8);
            --bg-btn-danger-hover: rgba(58, 26, 26, 0.9);
            --text-btn-danger: #ff6b6b;
            --border-btn-danger: #333333;
            
            --bg-btn-apply: linear-gradient(135deg, #8b5cf6 0%, #3b82f6 100%);
            --bg-btn-apply-hover: linear-gradient(135deg, #7c3aed 0%, #2563eb 100%);
            --text-btn-apply: #ffffff;
            
            --bg-btn-save: #27272a;
            --bg-btn-save-hover: #3f3f46;
            --text-btn-save: #ffffff;
            --border-btn-save: #3f3f46;
            
            --bg-row-hover: rgba(255, 255, 255, 0.035);
            --bg-row-selected: #1a2332;
            --border-row: #222222;
            
            --accent-color: #4285f4;
            --accent-color-rgb: 66, 133, 244;
            
            --bg-titlebar: rgba(11, 11, 11, 0.65);
            --border-titlebar: rgba(31, 41, 55, 0.5);
            --text-titlebar: #e5e7eb;
            
            --dock-btn-color: #71717a;
            --dock-btn-hover: rgba(255, 255, 255, 0.05);
            --dock-btn-active: rgba(255, 255, 255, 0.08);
            --dock-indicator: var(--accent-color);
            
            --toast-bg: #1a1a1a;
            --toast-text: #e0e0e0;
            --toast-border: #333333;

            --scrollbar-thumb: #333333;
            --scrollbar-thumb-hover: #555555;
            
            --backdrop-blur: blur(16px);
            --bg-overlay: transparent;
        }

        /* White Theme Overrides */
        [data-theme="white"] {
            --bg-body: #f8fafc;
            --text-main: #0f172a;
            --text-muted: #64748b;
            --text-accent: #3b82f6;
            --bg-sidebar: rgba(241, 245, 249, 0.8);
            --border-sidebar: rgba(226, 232, 240, 0.5);
            --bg-card: #ffffff;
            --bg-card-alt: #f8fafc;
            --border-card: #e2e8f0;
            --bg-modal: #ffffff;
            --border-modal: #e2e8f0;
            --bg-input: #f1f5f9;
            --border-input: #cbd5e1;
            --text-input: #0f172a;
            --bg-btn-primary: #3b82f6;
            --bg-btn-primary-hover: #2563eb;
            --text-btn-primary: #ffffff;
            --bg-btn-secondary: #ffffff;
            --bg-btn-secondary-hover: #f1f5f9;
            --text-btn-secondary: #0f172a;
            --border-btn-secondary: #cbd5e1;
            --bg-btn-danger: #fee2e2;
            --bg-btn-danger-hover: #fecaca;
            --text-btn-danger: #b91c1c;
            --border-btn-danger: #fecaca;
            --bg-row-hover: #f8fafc;
            --bg-row-selected: #eff6ff;
            --border-row: #e2e8f0;
            --accent-color: #3b82f6;
            --accent-color-rgb: 59, 130, 246;
            --bg-titlebar: rgba(255, 255, 255, 0.7);
            --border-titlebar: rgba(226, 232, 240, 0.5);
            --text-titlebar: #0f172a;
            --dock-btn-color: #64748b;
            --dock-btn-hover: rgba(0, 0, 0, 0.05);
            --dock-btn-active: rgba(0, 0, 0, 0.08);
            --toast-bg: #1e293b;
            --toast-text: #ffffff;
            --scrollbar-thumb: #cbd5e1;
            --scrollbar-thumb-hover: #94a3b8;
            --backdrop-blur: blur(12px);
            
            --bg-btn-apply: #6366f1;
            --bg-btn-apply-hover: #4f46e5;
            --text-btn-apply: #ffffff;
            --bg-btn-save: #475569;
            --bg-btn-save-hover: #334155;
            --text-btn-save: #ffffff;
        }

        /* Dark Purple Theme */
        [data-theme="dark_purple"] {
            --bg-body: #090712;
            --text-main: #e9e4ff;
            --text-muted: #a78bfa;
            --text-accent: #c084fc;
            --bg-sidebar: rgba(13, 10, 31, 0.75);
            --border-sidebar: rgba(30, 27, 75, 0.5);
            --bg-card: #0d0a1f;
            --bg-card-alt: #13102b;
            --border-card: #1e1b4b;
            --bg-modal: #13102b;
            --bg-input: #13102b;
            --border-input: #2e2a5e;
            --accent-color: #8b5cf6;
            --accent-color-rgb: 139, 92, 246;
            --bg-titlebar: rgba(13, 10, 31, 0.65);
            --border-titlebar: rgba(30, 27, 75, 0.5);
            --text-titlebar: #e9e4ff;
            --dock-btn-color: #818cf8;
            --dock-btn-hover: rgba(139, 92, 246, 0.1);
            --dock-btn-active: rgba(139, 92, 246, 0.2);
            --backdrop-blur: blur(16px);
            
            --bg-btn-apply: #7c3aed;
            --bg-btn-apply-hover: #6d28d9;
            --text-btn-apply: #ffffff;
            --bg-btn-save: #1e1b4b;
            --bg-btn-save-hover: #312e81;
            --text-btn-save: #e9e4ff;
        }

        /* Dark Blue Theme */
        [data-theme="dark_blue"] {
            --bg-body: #050810;
            --text-main: #e0f2fe;
            --text-muted: #7dd3fc;
            --text-accent: #38bdf8;
            --bg-sidebar: rgba(8, 12, 24, 0.75);
            --border-sidebar: rgba(30, 41, 59, 0.5);
            --bg-card: #080c18;
            --bg-card-alt: #0c1222;
            --border-card: #1e293b;
            --bg-modal: #0c1222;
            --bg-input: #0c1222;
            --border-input: #334155;
            --accent-color: #0ea5e9;
            --accent-color-rgb: 14, 165, 233;
            --bg-titlebar: rgba(8, 12, 24, 0.65);
            --border-titlebar: rgba(30, 41, 59, 0.5);
            --text-titlebar: #e0f2fe;
            --dock-btn-color: #38bdf8;
            --dock-btn-hover: rgba(14, 165, 233, 0.1);
            --dock-btn-active: rgba(14, 165, 233, 0.2);
            --backdrop-blur: blur(16px);
            
            --bg-btn-apply: #0284c7;
            --bg-btn-apply-hover: #0369a1;
            --text-btn-apply: #ffffff;
            --bg-btn-save: #1e293b;
            --bg-btn-save-hover: #334155;
            --text-btn-save: #e0f2fe;
        }

        /* White Pink Theme */
        [data-theme="white_pink"] {
            --bg-body: #fff5f7;
            --text-main: #4d1d24;
            --text-muted: #9f1239;
            --text-accent: #ec4899;
            --bg-sidebar: rgba(255, 241, 242, 0.85);
            --border-sidebar: rgba(254, 205, 211, 0.5);
            --bg-card: #ffffff;
            --bg-card-alt: #fff5f5;
            --border-card: #fecdd3;
            --bg-modal: #ffffff;
            --bg-input: #fff1f2;
            --border-input: #fecdd3;
            --accent-color: #f472b6;
            --accent-color-rgb: 244, 114, 182;
            --bg-titlebar: rgba(255, 255, 255, 0.7);
            --border-titlebar: rgba(254, 205, 211, 0.5);
            --text-titlebar: #4d1d24;
            --dock-btn-color: #f472b6;
            --dock-btn-hover: rgba(244, 114, 182, 0.1);
            --dock-btn-active: rgba(244, 114, 182, 0.2);
            --backdrop-blur: blur(12px);
            
            --bg-btn-apply: #db2777;
            --bg-btn-apply-hover: #be185d;
            --text-btn-apply: #ffffff;
            --bg-btn-save: #f9a8d4;
            --bg-btn-save-hover: #f472b6;
            --text-btn-save: #4d1d24;
        }

        /* Dark Pink Theme */
        [data-theme="dark_pink"] {
            --bg-body: #0d0a0b;
            --text-main: #ffe4e6;
            --text-muted: #fb7185;
            --text-accent: #f43f5e;
            --bg-sidebar: rgba(18, 11, 13, 0.75);
            --border-sidebar: rgba(49, 27, 30, 0.5);
            --bg-card: #120b0d;
            --bg-card-alt: #1a0f11;
            --border-card: #311b1e;
            --bg-modal: #1a0f11;
            --bg-input: #1a0f11;
            --border-input: #4c1d24;
            --accent-color: #e11d48;
            --accent-color-rgb: 225, 29, 72;
            --bg-titlebar: rgba(18, 11, 13, 0.65);
            --border-titlebar: rgba(49, 27, 30, 0.5);
            --text-titlebar: #ffe4e6;
            --dock-btn-color: #fb7185;
            --dock-btn-hover: rgba(225, 29, 72, 0.1);
            --dock-btn-active: rgba(225, 29, 72, 0.2);
            --backdrop-blur: blur(16px);
            
            --bg-btn-apply: #e11d48;
            --bg-btn-apply-hover: #be123c;
            --text-btn-apply: #ffffff;
            --bg-btn-save: #4c0519;
            --bg-btn-save-hover: #881337;
            --text-btn-save: #ffe4e6;
        }

        /* Anime Dark Theme */
        [data-theme="anime_dark"] {
            --bg-body-img: url('https://images3.alphacoders.com/112/thumb-1920-1120789.png');
            --text-main: #ffffff;
            --text-muted: #cbd5e1;
            --text-accent: #38bdf8;
            --bg-sidebar: rgba(15, 23, 42, 0.65);
            --border-sidebar: rgba(255, 255, 255, 0.1);
            --bg-card: rgba(15, 23, 42, 0.45);
            --bg-card-alt: rgba(15, 23, 42, 0.6);
            --border-card: rgba(255, 255, 255, 0.08);
            --bg-modal: rgba(15, 23, 42, 0.9);
            --bg-input: rgba(0, 0, 0, 0.4);
            --border-input: rgba(255, 255, 255, 0.1);
            --accent-color: #38bdf8;
            --accent-color-rgb: 56, 189, 248;
            --bg-titlebar: rgba(15, 23, 42, 0.4);
            --border-titlebar: rgba(255, 255, 255, 0.05);
            --text-titlebar: #ffffff;
            --dock-btn-color: #94a3b8;
            --dock-btn-hover: rgba(56, 189, 248, 0.15);
            --dock-btn-active: rgba(56, 189, 248, 0.25);
            --backdrop-blur: blur(16px);
            
            --bg-btn-apply: #0ea5e9;
            --bg-btn-apply-hover: #0284c7;
            --text-btn-apply: #ffffff;
            --bg-btn-save: rgba(255, 255, 255, 0.1);
            --bg-btn-save-hover: rgba(255, 255, 255, 0.2);
            --text-btn-save: #ffffff;
        }

        /* Anime Kawaii Theme */
        [data-theme="anime_kawaii"] {
            --bg-body-img: url('https://images6.alphacoders.com/135/thumb-1920-1351631.png');
            --text-main: #334155;
            --text-muted: #64748b;
            --text-accent: #ec4899;
            --bg-sidebar: rgba(255, 255, 255, 0.65);
            --border-sidebar: rgba(244, 114, 182, 0.2);
            --bg-card: rgba(255, 255, 255, 0.45);
            --bg-card-alt: rgba(255, 255, 255, 0.6);
            --border-card: rgba(244, 114, 182, 0.15);
            --bg-modal: rgba(255, 255, 255, 0.9);
            --bg-input: rgba(255, 255, 255, 0.5);
            --border-input: rgba(244, 114, 182, 0.2);
            --accent-color: #f472b6;
            --accent-color-rgb: 244, 114, 182;
            --bg-titlebar: rgba(255, 255, 255, 0.4);
            --border-titlebar: rgba(244, 114, 182, 0.1);
            --text-titlebar: #334155;
            --dock-btn-color: #f472b6;
            --dock-btn-hover: rgba(244, 114, 182, 0.15);
            --dock-btn-active: rgba(244, 114, 182, 0.25);
            --backdrop-blur: blur(16px);
            
            --bg-btn-apply: #f472b6;
            --bg-btn-apply-hover: #ec4899;
            --text-btn-apply: #ffffff;
            --bg-btn-save: #fce7f3;
            --bg-btn-save-hover: #fbcfe8;
            --text-btn-save: #9d174d;
        }

        /* Anime Pink Theme */
        [data-theme="anime_pink"] {
            --bg-body-img: url('https://4kwallpapers.com/images/wallpapers/anime-girl-girly-pink-fantasy-2880x1800-5055.jpg');
            --text-main: #312e81;
            --text-muted: #4338ca;
            --text-accent: #db2777;
            --bg-sidebar: rgba(255, 255, 255, 0.6);
            --border-sidebar: rgba(219, 39, 119, 0.2);
            --bg-card: rgba(255, 255, 255, 0.4);
            --bg-card-alt: rgba(255, 255, 255, 0.55);
            --border-card: rgba(219, 39, 119, 0.15);
            --bg-modal: rgba(255, 255, 255, 0.9);
            --bg-input: rgba(255, 255, 255, 0.4);
            --border-input: rgba(219, 39, 119, 0.2);
            --accent-color: #ec4899;
            --accent-color-rgb: 236, 72, 153;
            --bg-titlebar: rgba(255, 255, 255, 0.35);
            --border-titlebar: rgba(219, 39, 119, 0.1);
            --text-titlebar: #312e81;
            --dock-btn-color: #ec4899;
            --dock-btn-hover: rgba(236, 72, 153, 0.15);
            --dock-btn-active: rgba(236, 72, 153, 0.25);
            --backdrop-blur: blur(16px);
            
            --bg-btn-apply: #db2777;
            --bg-btn-apply-hover: #be185d;
            --text-btn-apply: #ffffff;
            --bg-btn-save: #fdf2f8;
            --bg-btn-save-hover: #fce7f3;
            --text-btn-save: #9d174d;
        }

        /* Dynamic Themes Helper */
        [data-theme^="dynamic-"] {
            --text-main: #ffffff;
            --text-muted: #e2e8f0;
            --text-accent: #ffffff;
            --bg-sidebar: rgba(0, 0, 0, 0.6);
            --border-sidebar: rgba(255, 255, 255, 0.1);
            --bg-card: rgba(0, 0, 0, 0.4);
            --bg-card-alt: rgba(0, 0, 0, 0.55);
            --border-card: rgba(255, 255, 255, 0.08);
            --bg-modal: rgba(10, 10, 15, 0.95);
            --bg-input: rgba(255, 255, 255, 0.05);
            --border-input: rgba(255, 255, 255, 0.1);
            --bg-titlebar: rgba(0, 0, 0, 0.4);
            --border-titlebar: rgba(255, 255, 255, 0.05);
            --text-titlebar: #ffffff;
            --backdrop-blur: blur(20px);
            --dock-btn-color: rgba(255, 255, 255, 0.6);
            --dock-btn-hover: rgba(255, 255, 255, 0.15);
            --dock-btn-active: rgba(255, 255, 255, 0.25);
            
            --bg-btn-apply: var(--accent-color);
            --bg-btn-apply-hover: var(--accent-color);
            --text-btn-apply: #ffffff;
            --bg-btn-save: rgba(255, 255, 255, 0.1);
            --bg-btn-save-hover: rgba(255, 255, 255, 0.2);
            --text-btn-save: #ffffff;
        }

        [data-theme="dynamic-naruto-kyuubi"] {
            --bg-body-img: url('https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3E3YzFzd29hdDl0eTU2NWpramU5ZmhxNHZpMmZ2aXRseW4yZW1meCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xLBVbY3quCoWDyhQIX/giphy.gif');
            --accent-color: #f97316;
            --accent-color-rgb: 249, 115, 22;
        }
        [data-theme="dynamic-samurai"] {
            --bg-body-img: url('https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNm1jbjdoN2R2bTg1c2h0cXB5ZjJmZjB0ZzllMXlmYXV4bGd0NDRkMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HyOOyynWxMxig/giphy.gif');
            --accent-color: #ef4444;
            --accent-color-rgb: 239, 68, 68;
        }
        [data-theme="dynamic-nebula"] {
            --bg-body-img: url('https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeThlbmxpbXg3ank5bDhycm1xNmpnMWoxYm05dzB6a3RpbnBucTFrbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3og0IyRiAsl1Pczi6Y/giphy.gif');
            --accent-color: #a855f7;
            --accent-color-rgb: 168, 85, 247;
        }
        [data-theme="dynamic-aurora"] {
            --bg-body-img: url('https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3czbnJhYXJmcjhmdGl6c2x5ZDZzMWExZGxkaWlvYjl4Z3Jtb3h4cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/mviluc9o1wCBy/giphy.gif');
            --accent-color: #22d3ee;
            --accent-color-rgb: 34, 211, 238;
        }
        [data-theme="dynamic-particles"] {
            --bg-body-img: url('https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmc1aWQ0ZWYzNnpkMzNmbXBueDB5eGlkamxibnJ3MzRraWFsN2lzdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26n6G8lRMOrYC6rFS/giphy.gif');
            --accent-color: #94a3b8;
            --accent-color-rgb: 148, 163, 184;
        }
        [data-theme="dynamic-matrix"] {
            --bg-body-img: url('https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGh1azd0bmd6dnpndW42enp1Z3R0bGVhbDZmeGU1dzh6OWNlYXcyeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wwg1suUiTbCY8H8vIA/giphy.gif');
            --accent-color: #22c55e;
            --accent-color-rgb: 34, 197, 94;
        }
        [data-theme="dynamic-fireflies"] {
            --bg-body-img: url('https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnQ0OXZrbDI3ZzNudnVvdXBoaWJnMWpoZGp0dm1nNDBiamQyamc3ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUPGcshrKRahaS8ef6/giphy.gif');
            --accent-color: #eab308;
            --accent-color-rgb: 234, 179, 8;
        }

        /* Optimized Base Styles */
        body {
            font-family: 'Inter', sans-serif;
            -webkit-font-smoothing: antialiased;
            overflow: hidden;
            height: 100vh;
            display: flex;
            flex-direction: row;
            background: var(--bg-body);
            background-image: var(--bg-body-img);
            color: var(--text-main);
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            transition: background 0.5s ease, background-image 0.5s ease, color 0.5s ease;
        }

        /* Sidebar & Dock */
        .sidebar {
            width: 56px;
            background: var(--bg-sidebar);
            border-right: 1px solid var(--border-sidebar);
            backdrop-filter: var(--backdrop-blur);
            -webkit-backdrop-filter: var(--backdrop-blur);
            display: flex;
            flex-direction: column;
            align-items: center;
            padding-top: 12px;
            padding-bottom: 16px;
            z-index: 1000;
            position: relative;
            flex-shrink: 0;
            transition: background 0.3s ease, border-color 0.3s ease;
        }

        .dock-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
            width: 100%;
        }

        .dock-btn {
            width: 34px;
            height: 34px;
            min-width: 34px;
            padding: 0;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--dock-btn-color);
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            z-index: 1;
        }
        .dock-btn:hover { color: var(--text-main); background: var(--dock-btn-hover); }
        .dock-btn-active { color: var(--text-main); background: var(--dock-btn-active); }
        
        .dock-indicator {
            position: absolute;
            left: 0;
            width: 3px;
            height: 20px;
            background: var(--accent-color);
            border-radius: 0 4px 4px 0;
            z-index: 0;
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            will-change: transform;
        }

        /* UI Elements Overrides */
        .bg-black { background-color: var(--bg-card) !important; backdrop-filter: var(--backdrop-blur); -webkit-backdrop-filter: var(--backdrop-blur); }
        .bg-gray-900 { background-color: var(--bg-card-alt) !important; backdrop-filter: var(--backdrop-blur); -webkit-backdrop-filter: var(--backdrop-blur); }
        .border-gray-800 { border-color: var(--border-card) !important; }
        .text-gray-400 { color: var(--text-muted) !important; }
        .text-gray-200 { color: var(--text-main) !important; }
        .text-gray-100 { color: var(--text-main) !important; }
        .text-white { color: var(--text-main) !important; }
        .static-blue { color: var(--text-accent) !important; }

        .modal-content { background-color: var(--bg-modal) !important; border-color: var(--border-modal) !important; backdrop-filter: var(--backdrop-blur); -webkit-backdrop-filter: var(--backdrop-blur); }
        .title-bar { background-color: var(--bg-titlebar) !important; border-bottom: 1px solid var(--border-titlebar) !important; backdrop-filter: var(--backdrop-blur); -webkit-backdrop-filter: var(--backdrop-blur); }
        .title-text { color: var(--text-titlebar) !important; }
        
        .input-field {
            background: var(--bg-input) !important;
            border: 1px solid var(--border-input) !important;
            color: var(--text-input) !important;
            transition: all 0.15s ease;
        }
        .input-field:focus {
            border-color: var(--accent-color) !important;
            box-shadow: 0 0 0 2px rgba(var(--accent-color-rgb), 0.2) !important;
        }

        /* Buttons */
        .btn-primary {
            background: var(--bg-btn-primary) !important;
            color: var(--text-btn-primary) !important;
        }
        .btn-primary:hover { background: var(--bg-btn-primary-hover) !important; }
        .btn-primary .material-symbols-rounded { color: var(--text-btn-primary) !important; }

        .btn-secondary {
            background: var(--bg-btn-secondary) !important;
            color: var(--text-btn-secondary) !important;
            border: 1px solid var(--border-btn-secondary) !important;
        }
        .btn-secondary:hover { background: var(--bg-btn-secondary-hover) !important; }

        .btn-danger {
            background: var(--bg-btn-danger) !important;
            color: var(--text-btn-danger) !important;
            border: 1px solid var(--border-btn-danger) !important;
        }
        .btn-danger:hover { background: var(--bg-btn-danger-hover) !important; }

        .btn-apply {
            background: var(--bg-btn-apply) !important;
            color: var(--text-btn-apply) !important;
            border: none !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        }
        .btn-apply:hover { 
            background: var(--bg-btn-apply-hover) !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3);
            filter: brightness(1.1);
        }

        .btn-save {
            background: var(--bg-btn-save) !important;
            color: var(--text-btn-save) !important;
            border: 1px solid var(--border-btn-save) !important;
        }
        .btn-save:hover { 
            background: var(--bg-btn-save-hover) !important;
            transform: translateY(-2px);
            filter: brightness(1.1);
        }

        /* Flag Row */
        .flag-row { transition: all 0.15s ease; border-bottom: 1px solid var(--border-row) !important; }
        .flag-row:hover { background-color: var(--bg-row-hover) !important; }
        .flag-row.selected { background-color: var(--bg-row-selected) !important; border-left: 2px solid var(--accent-color) !important; }
        .flag-row.to-remove { background-color: var(--bg-btn-danger) !important; }

        /* Scrollbar */
        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { border-radius: 2px; background: var(--scrollbar-thumb); }
        ::-webkit-scrollbar-thumb:hover { background: var(--scrollbar-thumb-hover); }

        /* Other */
        #toast { background: var(--toast-bg) !important; color: var(--toast-text) !important; border: 1px solid var(--toast-border); }
        .material-symbols-rounded { color: inherit; }
        .material-symbols-rounded { font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 20; font-size: 18px; }
        
        /* Layout & Utilities */
        html, body { -webkit-app-region: no-drag !important; }
        body * { -webkit-app-region: no-drag !important; }
        .title-bar { -webkit-app-region: drag; position: relative; z-index: 1000; }
        .title-bar-btn { -webkit-app-region: no-drag !important; }
        .title-text { pointer-events: none; -webkit-app-region: drag; }
        #toast, .modal-backdrop, .modal-content, .btn, .input-field, a, input, textarea, select, #flag-list, #kill-roblox-btn, #roblox-status, .sidebar, .dock-btn { -webkit-app-region: no-drag !important; }
        
        .modal-backdrop { transition: opacity 0.2s ease, visibility 0.2s; }
        .modal-content { transition: transform 0.2s ease, opacity 0.2s; }
        @keyframes slideUp { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        #toast.show { animation: slideUp 0.2s ease; }
        .btn { transition: all 0.15s ease; font-weight: 500; }
        .btn:hover { transform: translateY(-1px); }
        .btn:active { transform: translateY(0); }
        #flag-list { overflow-x: hidden; }
        .row-fixed { height: 40px; }
        .roblox-icon { display: inline-flex; align-items: center; justify-content: center; }
        .roblox-icon svg { width: 18px; height: 18px; display: block; }
        .pywebview-drag-region { -webkit-app-region: drag; user-select: none; }
        @keyframes view-slide-in { 0% { opacity: 0; transform: translateX(-10px); } 100% { opacity: 1; transform: translateX(0); } }
        .view-active { animation: view-slide-in 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
    </style>
</head>
<body>
    <script>
        window.updateRobloxStatus = function(state, count) {
            const els = [
                document.getElementById('roblox-status'),
                document.getElementById('roblox-status-roblox')
            ].filter(Boolean);
            els.forEach((robloxStatus) => {
                robloxStatus.className = 'w-6 h-6 rounded-full transition-all duration-300';
                robloxStatus.classList.remove('bg-red-500', 'bg-yellow-500', 'bg-green-500');
                if (state === 'not_running') {
                    robloxStatus.classList.add('bg-red-500');
                    robloxStatus.title = 'Roblox not running';
                } else if (state === 'running') {
                    robloxStatus.classList.add('bg-yellow-500');
                    robloxStatus.title = 'Roblox running, attaching...';
                } else if (state === 'attached') {
                    robloxStatus.classList.add('bg-green-500');
                    robloxStatus.title = count && count > 1 ? `Attached to ${count} Roblox processes` : 'Roblox attached';
                }
            });
        };
        window.populatePresetFlags = function(presets) {
            window.allPresetFlags = presets || [];
            const presetListDiv = document.getElementById('preset-list');
            const presetSearch = document.getElementById('preset-search');
            if (presetListDiv && presetSearch) {
                const searchTerm = (presetSearch.value || '').toLowerCase();
                presetListDiv.innerHTML = '';
                const filtered = window.allPresetFlags
                    .filter(flag => flag.toLowerCase().includes(searchTerm))
                    .slice(0, 100);
                if (filtered.length === 0) {
                    presetListDiv.innerHTML = '<div class="p-4 text-center text-gray-500 text-sm">No presets found</div>';
                    return;
                }
                filtered.forEach(flagName => {
                    const isPresent = (window.userFlags || []).some(f => f.name === flagName);
                    const item = document.createElement('button');
                    item.className = `w-full text-left p-3 text-sm rounded-md transition-colors ${
                        isPresent ? 'bg-gray-800 text-gray-500 cursor-not-allowed' : 'hover:bg-gray-800 text-gray-200'
                    }`;
                    item.textContent = flagName;
                    item.disabled = isPresent;
                    item.onclick = () => {
                        if (window.addFlagFromPreset) window.addFlagFromPreset(flagName);
                    };
                    presetListDiv.appendChild(item);
                });
            }
        };
        window.updateInjectionProgress = function(progress, total) {
            console.log("Injection Progress:", progress, total);
        };

        // Terminal functions
        document.addEventListener('DOMContentLoaded', () => {
                const output = document.getElementById('terminal-output');
                if (!output) return;

                output.innerHTML = '';

                function logToTerminal(message, type = 'info') {
                        const time = new Date().toLocaleTimeString('en-US', {
                                hour12: false,
                                hour: '2-digit',
                                minute: '2-digit',
                                second: '2-digit'
                        });
                        let colorClass = '';
                        switch (type) {
                                case 'error': colorClass = 'text-red-400'; break;
                                case 'warning': colorClass = 'text-yellow-400'; break;
                                case 'success': colorClass = 'text-green-400'; break;
                                default: colorClass = 'text-gray-300';
                        }
                        const line = document.createElement('div');
                        line.className = `mb-1 ${colorClass}`;
                        line.textContent = `[${time}] ${message}`;
                        output.appendChild(line);
                        output.scrollTop = output.scrollHeight;
                }

                function clearTerminal() {
                        output.innerHTML = '<div class="text-gray-500">--- Log cleared ---</div>';
                        logToTerminal('Terminal cleared', 'success');
                        showToast('Terminal log cleared', false);
                }

                function copyTerminal() {
                        const text = output.innerText.trim();

                        if (!text || text === '--- Log cleared ---') {
                                showToast('Nothing to copy', true);
                                return;
                        }

                        if (navigator.clipboard && navigator.clipboard.writeText) {
                                navigator.clipboard.writeText(text)
                                        .then(() => showToast('Terminal log copied to clipboard!', false))
                                        .catch(() => fallbackCopy(text));
                        } else {
                                fallbackCopy(text);
                        }
                }

                function fallbackCopy(text) {
                        const textarea = document.createElement('textarea');
                        textarea.value = text;
                        textarea.style.position = 'fixed';
                        textarea.style.opacity = '0';
                        textarea.style.left = '-9999px';
                        textarea.style.top = '-9999px';
                        document.body.appendChild(textarea);

                        textarea.select();
                        textarea.setSelectionRange(0, 99999);

                        try {
                                const successful = document.execCommand('copy');
                                if (successful) {
                                        showToast('Terminal log copied to clipboard!', false);
                                } else {
                                        throw new Error();
                                }
                        } catch (err) {
                                prompt('Copy the log below (Ctrl+C / Cmd+C):', text);
                                showToast('Manual copy: select text in prompt', true);
                        } finally {
                                document.body.removeChild(textarea);
                        }
                }

                document.getElementById('clear-terminal-btn')?.addEventListener('click', clearTerminal);
                document.getElementById('copy-terminal-btn')?.addEventListener('click', copyTerminal);

                logToTerminal('Terminal ready – backend logs incoming', 'success');

                window.logToTerminal = logToTerminal;
        });

        document.addEventListener('DOMContentLoaded', () => {
            setTimeout(() => {
                logToTerminal('Terminal ready – backend logs incoming', 'success');
                const waitingMsg = Array.from(terminalOutput.children).find(el => el.textContent.includes('Waiting for events'));
                if (waitingMsg) waitingMsg.remove();
            }, 200);
        });


        logToTerminal('Terminal initialized - watching for events...', 'info');
    </script>

    <aside class="sidebar">
        <div id="dock-container" class="dock-container">
            <div id="dock-indicator" class="dock-indicator"></div>
            <button id="tab-flags" class="dock-btn dock-btn-active" title="Flags">
                <span class="material-symbols-rounded">flag</span>
            </button>
            <button id="tab-roblox" class="dock-btn" title="Roblox">
                <span class="roblox-icon">
                    <svg viewBox="0 0 24 24" aria-hidden="true">
                        <path fill="currentColor" d="M8 2l14 6-6 14-14-6z"></path>
                        <rect x="12" y="8" width="4" height="4" transform="rotate(25 14 10)" fill="currentColor"></rect>
                    </svg>
                </span>
            </button>
            <button id="tab-presets" class="dock-btn" title="Presets">
                <span class="material-symbols-rounded">tune</span>
            </button>
            <button id="tab-terminal" class="dock-btn" title="Terminal">
                <span class="material-symbols-rounded">terminal</span>
            </button>
            <button id="tab-settings" class="dock-btn" title="Settings">
                <span class="material-symbols-rounded">settings</span>
            </button>
        </div>
        <div class="mt-auto flex flex-col items-center gap-4">
            <div id="roblox-status-roblox" class="w-6 h-6 rounded-full bg-red-500" title="Roblox Status"></div>
        </div>
    </aside>

    <div class="flex-1 flex flex-col overflow-hidden">
        <div id="app-title-bar" class="title-bar pywebview-drag-region h-8 flex justify-between items-center px-3 flex-shrink-0">
            <div class="title-text text-sm font-bold flex items-center gap-2">
                <span class="opacity-80">WINDSTRAP</span>
            </div>
            <div class="flex items-center gap-1" style="-webkit-app-region: no-drag;">
                <button id="min-btn" class="title-bar-btn w-8 h-8 flex items-center justify-center rounded-md hover:bg-white/10 transition-colors">
                    <span class="material-symbols-rounded !text-base">remove</span>
                </button>
                <button id="close-btn" class="title-bar-btn w-8 h-8 flex items-center justify-center rounded-md hover:bg-red-500/80 transition-colors">
                    <span class="material-symbols-rounded !text-base">close</span>
                </button>
            </div>
        </div>
        <!-- Main Content -->
        <main class="flex-1 flex flex-col overflow-hidden">
            <section id="flags-view" class="flex-1 flex flex-col overflow-hidden">
                <!-- Header -->
                <div class="px-5 py-3 flex-shrink-0 border-b border-gray-800">
                    <div class="flex justify-between items-center">
                        <h1 class="text-2xl font-bold static-blue">FFlags Editor</h1>
                        <div class="flex items-center space-x-1">
                            <button id="add-new-btn" class="btn btn-secondary px-2.5 py-1.5 rounded-md text-sm flex items-center space-x-1">
                                <span class="material-symbols-rounded">add</span>
                                <span>Add</span>
                            </button>
                            <button id="delete-selected-btn" class="btn btn-danger px-2.5 py-1.5 rounded-md text-sm flex items-center space-x-1">
                                <span class="material-symbols-rounded">delete</span>
                                <span>Remove</span>
                            </button>
                            <button id="remove-all-btn" class="btn btn-danger px-2.5 py-1.5 rounded-md text-sm flex items-center space-x-1">
                                <span class="material-symbols-rounded">clear_all</span>
                                <span>Remove All</span>
                            </button>
                            <button id="show-preset-btn" class="btn btn-secondary px-2.5 py-1.5 rounded-md text-sm flex items-center space-x-1">
                                <span class="material-symbols-rounded">list</span>
                                <span>Presets</span>
                            </button>
                            <button id="import-btn" class="btn btn-secondary px-2.5 py-1.5 rounded-md text-sm flex items-center space-x-1">
                                <span class="material-symbols-rounded">upload</span>
                                <span>Import</span>
                            </button>
                            <button id="export-btn" class="btn btn-secondary px-2.5 py-1.5 rounded-md text-sm flex items-center space-x-1">
                                <span class="material-symbols-rounded">download</span>
                                <span>Export</span>
                            </button>
                        </div>
                    </div>
                </div>
                <!-- Search -->
                <div class="px-5 py-2.5 flex-shrink-0">
                    <div class="flex items-center gap-3">
                        <div class="relative flex-1">
                            <span class="material-symbols-rounded absolute left-3 top-1/2 -translate-y-1/2 text-gray-500">search</span>
                            <input id="search-bar" type="text" placeholder="Search flags..." class="input-field w-full pl-9 pr-3 py-2 rounded-md text-sm outline-none">
                        </div>
                        <select id="type-filter" class="input-field px-3 py-2 rounded-md text-sm w-40">
                            <option value="all">All Types</option>
                            <option value="bool">Bool</option>
                            <option value="int">Int</option>
                            <option value="float">Float</option>
                            <option value="string">String</option>
                        </select>
                    </div>
                </div>
                <!-- Flag List -->
                <div class="flex-1 min-h-0 px-6 pb-3">
                    <div class="h-full bg-black rounded-lg border border-gray-800 overflow-hidden flex flex-col">
                        <div class="table-header flex text-xs text-gray-400 bg-gray-900 border-b border-gray-800 px-4 py-2 sticky top-0 z-10">
                            <div class="w-12 text-center"></div>
                            <button id="col-name" class="flex-1 pl-2 text-left hover:text-gray-300">NAME</button>
                            <button id="col-type" class="w-24 pl-2 text-left hover:text-gray-300">TYPE</button>
                            <div class="w-32 pl-2">VALUE</div>
                        </div>
                        <div id="flag-list" class="flex-1 overflow-y-auto">
                        </div>
                    </div>
                </div>
                <!-- Actions -->
                    <div class="px-6 py-2 flex-shrink-0 border-t border-gray-800">
                    <div class="flex justify-between items-center">
                        <div class="flex items-center space-x-3">
                            <button id="kill-roblox-btn" class="btn btn-danger px-3 py-1.5 rounded-md text-sm flex items-center space-x-1">
                                <span class="material-symbols-rounded">Terminal</span>
                                <span>Kill Roblox</span>
                            </button>
                        </div>
                        <div class="flex items-center space-x-3">
                            <button id="apply-btn" class="btn btn-apply px-6 py-2.5 rounded-md text-base font-bold transition-all duration-200">
                                Apply to Roblox
                            </button>
                            <button id="save-btn" class="btn btn-save px-6 py-2.5 rounded-md text-sm font-medium transition-all duration-200">
                                Save Flags
                            </button>
                        </div>
                    </div>
                </div>
            </section>
            <section id="settings-view" class="flex-1 flex flex-col overflow-hidden hidden">
                    <div class="px-6 py-4 flex-shrink-0 border-b border-gray-800">
                            <h1 class="text-3xl font-bold static-blue">Settings</h1>
                    </div>
                    <div class="px-6 py-4 flex-1 overflow-y-auto space-y-6">
                            <!-- Main Settings Card -->
                            <div class="bg-black rounded-lg border border-gray-800 p-5 space-y-6">
                                    <label class="flex items-center justify-between cursor-pointer">
                                            <span class="text-sm text-gray-300">Auto apply flags when injected</span>
                                            <input id="auto-apply-toggle" type="checkbox" class="h-5 w-5 text-purple-500 focus:ring-purple-500">
                                    </label>
                                    <div class="flex items-center justify-between">
                                            <span class="text-sm text-gray-300">Theme</span>
                                            <select id="theme-select" class="input-field px-3 py-2 rounded-md text-sm bg-gray-900 border border-gray-700 focus:border-purple-500 focus:outline-none">
                                                    <option value="black">Default</option>
                                                    <option value="white">White</option>
                                                    <option value="white_pink">White Pink</option>
                                                    <option value="dark_pink">Dark Pink</option>
                                                    <option value="dark_purple">Dark Purple</option>
                                                    <option value="dark_blue">Dark Blue</option>
                                                    <option value="anime_dark">Anime#1</option>
                                                    <option value="anime_kawaii">Anime#2</option>
                                                    <option value="anime_pink">Anime#3</option>
                                                    <option value="dynamic-nebula">Nebula</option>
                                                    <option value="dynamic-aurora">Aurora</option>
                                                    <option value="dynamic-particles">Particles</option>
                                                    <option value="dynamic-matrix">Matrix Cat</option>
                                                    <option value="dynamic-fireflies">Fireflies Night</option>
                                                    <option value="dynamic-naruto-kyuubi">Naruto Kyuubi</option>
                                                    <option value="dynamic-samurai">Samurai</option>
                                            </select>
                                    </div>
                                    <div class="flex items-center justify-between">
                                            <span class="text-sm text-gray-300">Hide/Show UI Keybind</span>
                                            <button id="hide-key-capture-btn"
                                                    class="px-5 py-2 rounded-md text-sm font-mono bg-gray-900 border border-gray-700 hover:border-purple-500 focus:border-purple-500 transition shadow-md min-w-[120px] text-center">
                                                    <span id="hide-key-display">INSERT</span>
                                            </button>
                                    </div>
                                    <input type="hidden" id="hide-key-input">
                            </div>
                            <div class="bg-black rounded-lg border border-gray-800 p-5">
                                    <h3 class="text-lg font-semibold text-blue-500 mb-5 static-blue">Protection</h3>
                                    <div class="space-y-4">
                                            <label class="flex items-center justify-between cursor-pointer">
                                                    <span class="text-sm text-gray-300">Safe Mode <span class="text-gray-400 text-xs">(NtWrite + XOR Encryption)</span></span>
                                                    <input id="safe-mode-toggle" type="checkbox" class="h-5 w-5 text-purple-500 focus:ring-purple-500">
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer">
                                                    <span class="text-sm text-gray-300">Random Re-apply <span class="text-gray-400 text-xs">(Prevent Crash)</span></span>
                                                    <input id="randomization-toggle" type="checkbox" class="h-5 w-5 text-purple-500 focus:ring-purple-500">
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer">
                                                    <span class="text-sm text-gray-300">Timing Attack <span class="text-gray-400 text-xs">(Experimental)</span></span>
                                                    <input id="timing-attack-toggle" type="checkbox" class="h-5 w-5 text-purple-500 focus:ring-purple-500">
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer">
                                                    <span class="text-sm text-gray-300">Re-apply</span>
                                                    <input id="reapply-toggle" type="checkbox" class="h-5 w-5 text-purple-500 focus:ring-purple-500">
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer">
                                                    <span class="text-sm text-gray-300">
                                                            Offsetless Injection 
                                                            <span class="text-gray-400 text-xs">(No offsets needed – more stable) </span>
                                                    </span>
                                                    <input id="offsetless-toggle" type="checkbox" class="h-5 w-5 text-purple-500 focus:ring-purple-500">
                                            </label>
                                            <label class="flex items-center justify-between cursor-pointer">
                                                    <span class="text-sm text-gray-300">Stealth Mode <span class="text-gray-400 text-xs">(Hide while recording apps running)</span></span>
                                                    <input id="stealth-mode-toggle" type="checkbox" class="h-5 w-5 text-purple-500 focus:ring-purple-500">
                                            </label>
                                            <div>
                                                <label class="flex items-center justify-between cursor-pointer" onclick="document.getElementById('batch-apply-options').classList.toggle('hidden')">
                                                    <span class="text-sm text-gray-300">Batch Apply + Sleep <span class="text-gray-400 text-xs">(Split injection into batches with delay)</span></span>
                                                    <input id="batch-apply-toggle" type="checkbox" class="h-5 w-5 text-purple-500 focus:ring-purple-500" onclick="event.stopPropagation(); document.getElementById('batch-apply-options').classList.toggle('hidden', !this.checked);">
                                                </label>
                                                <div id="batch-apply-options" class="hidden mt-3 ml-2 space-y-3 border-l-2 border-gray-700 pl-4">
                                                    <div class="flex items-center justify-between">
                                                        <span class="text-xs text-gray-400">Batch Size <span class="text-gray-500">(flags per batch)</span></span>
                                                        <input id="batch-size-input" type="number" min="1" max="10000" value="50" class="input-field px-2 py-1 rounded text-sm w-28 text-right bg-gray-900 border border-gray-700">
                                                    </div>
                                                    <div class="flex items-center justify-between">
                                                        <span class="text-xs text-gray-400">Sleep between batches <span class="text-gray-500">(ms)</span></span>
                                                        <input id="batch-sleep-input" type="number" min="0" max="60000" value="50" class="input-field px-2 py-1 rounded text-sm w-28 text-right bg-gray-900 border border-gray-700">
                                                    </div>
                                                </div>
                                            </div>
                                            </div>
                                    </div>
                            </div>

                            <div class="flex justify-end p-4 border-t border-gray-800">
                            <button id="save-settings-btn" class="btn btn-save px-6 py-2 rounded-md text-sm font-medium">
                                    Save Settings
                            </button>
                    </div>
            </section>
            <section id="roblox-view" class="flex-1 flex flex-col overflow-hidden hidden">
                <div class="px-6 py-4 flex-shrink-0 border-b border-gray-800">
                    <h1 class="text-3xl font-bold static-blue">Roblox</h1>
                    <p class="text-sm text-gray-400 mt-1">Engine settings applied live to Roblox</p>
                </div>
                <div class="px-6 py-4 flex-1 overflow-y-auto space-y-6">
                    <div class="bg-black rounded-lg border border-gray-800 p-5 space-y-6">
                        <div class="space-y-5">
                            <div class="flex items-center justify-between">
                                <div>
                                    <div class="text-sm text-gray-200">Graphics Quality</div>
                                    <div class="text-xs text-gray-500">Set the quality of your game</div>
                                </div>
                                <div class="flex items-center gap-3 w-64">
                                    <input id="roblox-graphics-slider" type="range" min="1" max="10" value="5" class="w-full">
                                    <span id="roblox-graphics-value" class="text-sm text-gray-300 w-6 text-right">5</span>
                                </div>
                            </div>
                            <div class="flex items-center justify-between">
                                <div>
                                    <div class="text-sm text-gray-200">Framerate Limit</div>
                                    <div class="text-xs text-gray-500">Unlock FPS</div>
                                </div>
                                <input id="roblox-fps-input" type="text" placeholder="240" class="input-field px-3 py-2 rounded-md text-sm w-64 text-right">
                            </div>
                            <div class="flex items-center justify-between">
                                <div>
                                    <div class="text-sm text-gray-200">Transparency</div>
                                    <div class="text-xs text-gray-500">UI Elements</div>
                                </div>
                                <div class="flex items-center gap-3 w-64">
                                    <input id="roblox-transparency-slider" type="range" min="0" max="3" value="0" class="w-full">
                                    <span id="roblox-transparency-value" class="text-sm text-gray-300 w-6 text-right">0</span>
                                </div>
                            </div>
                            <div class="flex items-center justify-between">
                                <div>
                                    <div class="text-sm text-gray-200">Reduced Motion</div>
                                    <div class="text-xs text-gray-500">Removes escape menu animation</div>
                                </div>
                                <input id="roblox-reduced-motion-toggle" type="checkbox" class="h-5 w-5 text-purple-500 focus:ring-purple-500">
                            </div>
                            <div class="flex items-center justify-between">
                                <div>
                                    <div class="text-sm text-gray-200">Font Size</div>
                                    <div class="text-xs text-gray-500">Choose how large text appears</div>
                                </div>
                                <select id="roblox-font-size-select" class="input-field px-3 py-2 rounded-md text-sm w-32 text-right">
                                    <option value="2">2</option>
                                    <option value="3" selected>3</option>
                                    <option value="4">4</option>
                                </select>
                            </div>
                            <div class="flex items-center justify-between">
                                <div>
                                    <div class="text-sm text-gray-200">Mouse Sensitivity</div>
                                    <div class="text-xs text-gray-500">Any number</div>
                                </div>
                                <input id="roblox-mouse-sens-input" type="text" placeholder="100" class="input-field px-3 py-2 rounded-md text-sm w-64 text-right">
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <section id="presets-view" class="flex-1 flex flex-col overflow-hidden hidden">
                <div class="px-6 py-4 flex-shrink-0 border-b border-gray-800">
                    <h1 class="text-3xl font-bold static-blue">Presets</h1>
                </div>
                <div class="px-6 py-4 flex-1 overflow-y-auto space-y-6">
                    <div class="bg-black rounded-lg border border-gray-800 p-5 space-y-4">
                        <div class="flex items-center justify-between">
                            <div>
                                <div class="text-sm text-gray-200">Use old death sound</div>
                                <div class="text-xs text-gray-500">Bring back the classic 'oof' death sound.</div>
                            </div>
                            <input id="preset-old-death" type="checkbox" class="h-4 w-4">
                        </div>
                        <div class="flex items-center justify-between">
                            <div>
                                <div class="text-sm text-gray-200">Mouse cursor</div>
                                <div class="text-xs text-gray-500">Choose between classic Roblox cursor styles.</div>
                            </div>
                            <select id="preset-mouse-cursor" class="input-field px-2 py-1 rounded text-sm w-44">
                                <option value="default">Default</option>
                                <option value="classic">Classic Style</option>
                                <option value="blackdot">Black Dot</option>
                                <option value="whitedot">White Dot</option>
                                <option value="diamondsword">Sword</option>
                                <option value="pink">Pink Cross</option>
                                <option value="girl">Girl</option>
                            </select>
                        </div>
                        <div class="flex items-center justify-between">
                            <div>
                                <div class="text-sm text-gray-200">Use old avatar editor background</div>
                                <div class="text-xs text-gray-500">Bring back the old avatar editor background used prior to 2020.</div>
                            </div>
                            <input id="preset-old-avatar-bg" type="checkbox" class="h-4 w-4">
                        </div>
                        <div class="flex items-center justify-between">
                            <div>
                                <div class="text-sm text-gray-200">Emulate old character sounds</div>
                                <div class="text-xs text-gray-500">Roughly bring back character sounds used prior to 2014.</div>
                            </div>
                            <input id="preset-old-char-sounds" type="checkbox" class="h-4 w-4">
                        </div>
                        <div class="flex items-center justify-between">
                            <div>
                                <div class="text-sm text-gray-200">Preferred emoji type</div>
                                <div class="text-xs text-gray-500">Choose which type of emoji Roblox should use.</div>
                            </div>
                            <select id="preset-emoji-type" class="input-field px-2 py-1 rounded text-sm w-52">
                                <option value="default">Default (Twitter)</option>
                                <option value="apple">Apple 🍎</option>
                                <option value="windows">Windows 🪟</option>
                                <option value="noto">Google Noto 🌈</option>
                                <option value="custom">Custom Font...</option>
                            </select>
                        </div>
                    </div>
                    <div class="bg-black rounded-lg border border-gray-800 p-5 space-y-4">
                        <div class="text-lg font-semibold text-gray-200">Miscellaneous</div>
                        <div class="flex items-center justify-between">
                            <div>
                                <div class="text-sm text-gray-200">Use custom font</div>
                                <div class="text-xs text-gray-500">Font size can be adjusted in the Engine Settings tab.</div>
                            </div>
                            <div class="flex items-center space-x-2">
                                <input id="preset-use-custom-font" type="checkbox" class="h-4 w-4">
                                <button id="preset-choose-font" class="btn btn-secondary px-3 py-1.5 rounded-md text-sm">Choose font...</button>
                            </div>
                        </div>
                        <div id="preset-font-name" class="text-xs text-gray-500"></div>
                    </div>
                    <div class="bg-black rounded-lg border border-gray-800 p-5 space-y-4">
                        <div class="text-lg font-semibold text-gray-200">Injection Control</div>
                        <div class="flex items-center justify-between">
                            <div>
                                <div class="text-sm text-gray-200">Uninject / Restore default FFlags</div>
                                <div class="text-xs text-gray-500">Restores all modified FFlags to their original default values (requires Roblox attached).</div>
                            </div>
                            <button id="uninject-btn" class="btn btn-danger px-4 py-2 rounded-md text-sm flex items-center space-x-1">
                                <span class="material-symbols-rounded">restore</span>
                                <span>Uninject</span>
                            </button>
                        </div>
                    </div>
                </div>
                <div class="flex justify-end p-4 border-t border-gray-800">
                    <button id="save-presets-btn" class="btn btn-save px-4 py-1.5 rounded-md text-sm">Save</button>
                </div>
            </section>
            <section id="terminal-view" class="flex-1 flex flex-col overflow-hidden hidden">
                <div class="px-6 py-4 flex-shrink-0 border-b border-gray-800">
                    <h1 class="text-3xl font-bold static-blue">Terminal</h1>
                    <p class="text-sm text-gray-400 mt-1">Windstrap log system</p>
                </div>
                <div class="flex-1 px-6 py-4 overflow-hidden">
                    <div id="terminal-output" class="bg-black/70 backdrop-blur rounded-lg border border-gray-800 p-5 h-full overflow-y-auto font-mono text-sm whitespace-pre-wrap">
                        <div class="text-gray-500">--- Waiting for events ---</div>
                    </div>
                </div>
                <div class="px-6 py-3 flex-shrink-0 border-t border-gray-800 flex items-center justify-between">
                    <button id="clear-terminal-btn" class="btn btn-secondary px-3 py-1.5 rounded-md text-sm flex items-center gap-2">
                            <span class="material-symbols-rounded text-sm">clear_all</span>
                            Clear
                        </button>
                        <button id="copy-terminal-btn" class="btn btn-secondary px-3 py-1.5 rounded-md text-sm flex items-center gap-2">
                            <span class="material-symbols-rounded text-sm">content_copy</span>
                            Copy
                        </button>
                    </div>
            </section>
        </main>
    </div>
    <div id="import-json-modal" class="modal-backdrop fixed inset-0 bg-black/60 flex items-center justify-center z-50 opacity-0 invisible">
        <div class="modal-content bg-[#111111] rounded-lg shadow-2xl w-full max-w-xl h-[55vh] flex flex-col scale-95 border border-[#222222]">
            <!-- Header with grey background -->
            <div class="flex items-center justify-between px-5 py-3 bg-[#1e1e1e] border-b border-[#222222]">
                <div class="flex-1"></div>
                <h3 class="text-lg font-semibold text-gray-200 text-center flex-1">Import JSON</h3>
                <div class="flex-1 flex justify-end">
                    <button id="close-import-json-modal" class="text-gray-400 hover:text-gray-200">
                        <span class="material-symbols-rounded">close</span>
                    </button>
                </div>
            </div>
            <div class="flex-1 p-4 flex flex-col">
                <div class="h-full">
                    <textarea id="json-input-area" class="w-full h-full bg-[#1e1e1e] border border-[#333333] rounded-lg p-4 text-gray-200 font-mono text-sm resize-none focus:border-blue-500 focus:outline-none" placeholder='{
  "FFlagDebugDisplayFPS": "True",
}'></textarea>
                </div>
            </div>
            <div class="flex justify-end items-center px-5 py-4 border-t border-[#222222] gap-3">
                <button id="import-from-file-btn" class="flex items-center justify-center gap-2 px-5 py-2 bg-[#1e1e1e] hover:bg-[#252525] text-white text-sm font-medium rounded-md transition-all border border-[#333333]">
                    <span class="material-symbols-rounded text-base">folder_open</span>
                    Import from file
                </button>
                <button id="clear-import-json" class="btn btn-secondary px-5 py-2 rounded-md text-sm">Clear</button>
                <button id="ok-import-json" class="btn btn-primary px-5 py-2 rounded-md text-sm">OK</button>
            </div>
        </div>
    </div>

    <!-- Preset Modal -->
    <div id="preset-modal" class="modal-backdrop fixed inset-0 bg-black/60 flex items-center justify-center z-50 opacity-0 invisible">
        <div id="modal-content-preset" class="modal-content bg-gray-900 rounded-lg shadow-lg w-full max-w-2xl h-[80vh] flex flex-col scale-95">
            <div class="flex justify-between items-center px-5 py-4 border-b border-gray-800">
                <h3 class="font-medium text-gray-100">Add Flag from Presets</h3>
                <button id="close-modal-btn-preset" class="material-symbols-rounded text-gray-400 hover:text-gray-200">close</button>
            </div>
            <div class="p-4">
                <input id="preset-search" type="text" placeholder="Search presets..." class="input-field w-full px-3 py-2 rounded-md text-sm outline-none">
            </div>
            <div id="preset-list" class="flex-1 overflow-y-auto px-4 pb-4">
            </div>
        </div>
    </div>
    <!-- Edit Modal -->
    <div id="edit-modal" class="modal-backdrop fixed inset-0 bg-black/60 flex items-center justify-center z-50 opacity-0 invisible">
        <div id="modal-content-edit" class="modal-content bg-gray-900 rounded-lg shadow-lg w-full max-w-md scale-95">
            <div class="flex justify-between items-center px-5 py-4 border-b border-gray-800">
                <h3 class="font-medium text-gray-100" id="edit-modal-title">Edit Value</h3>
                <button id="close-modal-btn-edit" class="material-symbols-rounded text-gray-400 hover:text-gray-200">close</button>
            </div>
            <div class="p-5">
                <div class="mb-3">
                    <label class="text-xs text-gray-400 mb-1 block">Value</label>
                    <input id="edit-value-input" type="text" class="input-field w-full px-3 py-2 rounded-md text-sm outline-none">
                </div>
                <p class="text-xs text-gray-500">Data type will be automatically inferred</p>
            </div>
            <div class="flex justify-end p-4 border-t border-gray-800">
                <button id="save-edit-btn" class="btn btn-primary px-4 py-1.5 rounded-md text-sm">
                    Apply
                </button>
            </div>
        </div>
    </div>
    <!-- Confirm Modal -->
    <div id="confirm-modal" class="modal-backdrop fixed inset-0 bg-black/60 flex items-center justify-center z-50 opacity-0 invisible">
        <div id="modal-content-confirm" class="modal-content bg-gray-900 rounded-lg shadow-lg w-full max-w-md scale-95">
            <div class="flex justify-between items-center px-5 py-4 border-b border-gray-800">
                <h3 class="font-medium text-gray-100" id="confirm-title">Confirm</h3>
                <button id="close-confirm-btn" class="material-symbols-rounded text-gray-400 hover:text-gray-200">close</button>
            </div>
            <div class="p-5">
                <p id="confirm-message" class="text-sm text-gray-300"></p>
            </div>
            <div class="flex justify-end space-x-2 p-4 border-t border-gray-800">
                <button id="confirm-yes" class="btn btn-primary px-4 py-1.5 rounded-md text-sm">Yes</button>
                <button id="confirm-no" class="btn btn-secondary px-4 py-1.5 rounded-md text-sm">Cancel</button>
            </div>
        </div>
    </div>
    <!-- Toast -->
    <div id="toast" class="fixed bottom-6 right-6 px-4 py-2 opacity-0 translate-y-2 z-50 rounded-md text-sm font-medium shadow-sm"></div>
    <script>
        let userFlags = [];
        let allPresetFlags = [];
        window.userFlags = userFlags;
        let editingFlagName = null;
        const flagsToRemove = new Set();
        function cleanFlagName(name) {
            const prefixes = ["DFInt", "DFString", "DFFlag", "FInt", "FString", "FFlag"];
            for (const prefix of prefixes) {
                if (name.startsWith(prefix)) {
                    return name.substring(prefix.length);
                }
            }
            return name;
        }
        // DOM Elements
        const flagList = document.getElementById('flag-list');
        const searchBar = document.getElementById('search-bar');
        const addNewBtn = document.getElementById('add-new-btn');
        const deleteSelectedBtn = document.getElementById('delete-selected-btn');
        const removeAllBtn = document.getElementById('remove-all-btn');
        const saveBtn = document.getElementById('save-btn');
        const killRobloxBtn = document.getElementById('kill-roblox-btn');
        const applyBtn = document.getElementById('apply-btn');
        const toast = document.getElementById('toast');
        const importBtn = document.getElementById('import-btn');
        const exportBtn = document.getElementById('export-btn');
        const presetModal = document.getElementById('preset-modal');
        const showPresetBtn = document.getElementById('show-preset-btn');
        const closeModalBtnPreset = document.getElementById('close-modal-btn-preset');
        const presetListDiv = document.getElementById('preset-list');
        const presetSearch = document.getElementById('preset-search');
        const flagsView = document.getElementById('flags-view');
        const settingsView = document.getElementById('settings-view');
        const presetsView = document.getElementById('presets-view');
        const terminalView = document.getElementById('terminal-view');
        const robloxView = document.getElementById('roblox-view');
        const typeFilter = document.getElementById('type-filter');
        const colName = document.getElementById('col-name');
        const colType = document.getElementById('col-type');
        const robloxGraphicsSlider = document.getElementById('roblox-graphics-slider');
        const robloxGraphicsValue = document.getElementById('roblox-graphics-value');
        const robloxFpsInput = document.getElementById('roblox-fps-input');
        const robloxTransparencySlider = document.getElementById('roblox-transparency-slider');
        const robloxTransparencyValue = document.getElementById('roblox-transparency-value');
        const robloxReducedMotionToggle = document.getElementById('roblox-reduced-motion-toggle');
        const robloxFontSizeSelect = document.getElementById('roblox-font-size-select');
        const robloxMouseSensInput = document.getElementById('roblox-mouse-sens-input');
        const flagsTabBtn = document.getElementById('tab-flags');
        const settingsTabBtn = document.getElementById('tab-settings');
        const presetsTabBtn = document.getElementById('tab-presets');
        const terminalTabBtn = document.getElementById('tab-terminal');
        const robloxTabBtn = document.getElementById('tab-roblox');
        const autoApplyToggle = document.getElementById('auto-apply-toggle');
        const saveSettingsBtn = document.getElementById('save-settings-btn');
        const themeSelect = document.getElementById('theme-select');
        const presetOldDeath = document.getElementById('preset-old-death');
        const presetMouseCursor = document.getElementById('preset-mouse-cursor');
        const presetOldAvatarBg = document.getElementById('preset-old-avatar-bg');
        const presetOldCharSounds = document.getElementById('preset-old-char-sounds');
        const presetEmojiType = document.getElementById('preset-emoji-type');
        const presetUseCustomFont = document.getElementById('preset-use-custom-font');
        const presetChooseFont = document.getElementById('preset-choose-font');
        const presetFontName = document.getElementById('preset-font-name');
        const savePresetsBtn = document.getElementById('save-presets-btn');
        const editModal = document.getElementById('edit-modal');
        const closeModalBtnEdit = document.getElementById('close-modal-btn-edit');
        const editModalTitle = document.getElementById('edit-modal-title');
        const editValueInput = document.getElementById('edit-value-input');
        const saveEditBtn = document.getElementById('save-edit-btn');
        const uninjectBtn = document.getElementById('uninject-btn');
        function withApi(fn) {
            if (window.pywebview && pywebview.api) {
                fn(pywebview.api);
            } else {
                window.addEventListener('pywebviewready', () => fn(pywebview.api));
            }
        }
        function showToast(message, isError = false) {
            toast.textContent = message;
            toast.className = `fixed top-3 right-3 px-4 py-2 z-[9999] rounded-md text-sm font-medium shadow-lg pointer-events-none ${isError ? 'bg-red-900/80 text-red-200 border border-red-800' : 'bg-green-900/80 text-green-200 border border-green-800'}`;
            toast.classList.add('show');
            toast.classList.remove('opacity-0', 'translate-y-2');
            setTimeout(() => {
                toast.classList.add('opacity-0', 'translate-y-2');
                toast.classList.remove('show');
            }, 3000);
        }
        function inferType(value) {
            const lowerValue = value.toLowerCase().trim();
            if (lowerValue === 'true' || lowerValue === 'false') return 'bool';
            if (/^[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?$/.test(lowerValue) && lowerValue !== '') {
                return lowerValue.indexOf('.') === -1 ? 'int' : 'float';
            }
            return 'string';
        }
        function showConfirm(message) {
            return new Promise((resolve) => {
                document.getElementById('confirm-message').innerHTML = message;
                const modal = document.getElementById('confirm-modal');
                const content = document.getElementById('modal-content-confirm');
                const yesBtn = document.getElementById('confirm-yes');
                const noBtn = document.getElementById('confirm-no');
                const closeBtn = document.getElementById('close-confirm-btn');
                modal.classList.remove('opacity-0', 'invisible');
                content.classList.remove('scale-95');
                const cleanup = () => {
                    modal.classList.add('opacity-0');
                    setTimeout(() => modal.classList.add('invisible'), 200);
                    content.classList.add('scale-95');
                    yesBtn.onclick = null;
                    noBtn.onclick = null;
                    closeBtn.onclick = null;
                    modal.onclick = null;
                };
                yesBtn.onclick = () => { resolve(true); cleanup(); };
                noBtn.onclick = () => { resolve(false); cleanup(); };
                closeBtn.onclick = () => { resolve(false); cleanup(); };
                modal.onclick = (e) => {
                    if (e.target === modal) { resolve(false); cleanup(); }
                };
            });
        }
        function updateRemoveButtonText() {
            if (!deleteSelectedBtn) return;
            const count = flagsToRemove.size;
            const textSpan = deleteSelectedBtn.querySelector('span:last-child');
            if (textSpan) {
                textSpan.textContent = count > 0 ? `Remove (${count})` : 'Remove';
            }
        }
        function showPresetModal() {
            presetModal.classList.remove('opacity-0', 'invisible');
            document.getElementById('modal-content-preset').classList.remove('scale-95');
            presetSearch.value = '';
            renderPresetList();
            setTimeout(() => presetSearch.focus(), 200);
        }
        function hidePresetModal() {
            document.getElementById('modal-content-preset').classList.add('scale-95');
            presetModal.classList.add('opacity-0');
            setTimeout(() => presetModal.classList.add('invisible'), 200);
        } 
        function switchView(activeView) {
            [flagsView, settingsView, presetsView, terminalView, robloxView].forEach(v => {
                if (v === activeView) {
                    v.classList.remove('hidden');
                    // Force reflow to restart animation
                    v.classList.remove('view-active');
                    void v.offsetWidth; 
                    v.classList.add('view-active');
                } else {
                    v.classList.add('hidden');
                    v.classList.remove('view-active');
                }
            });
        }
        function showSettingsView() {
            setActiveTab('settings');
            switchView(settingsView);

                // Default values (used if API fails or setting is missing)
                let autoApply = false;
                let theme = 'black';
                let currentBossKey = 'insert';
                let safeMode = true;
                let randomization = true;
                let timingAttack = true;
                let reapply = false;
                let offsetless = false;
                let stealthMode = false;

                withApi(async (api) => {
                    try {
                        const settings = await api.get_settings();
                        // Load all settings with fallbacks
                        autoApply = settings.auto_apply_on_attach ?? false;
                        safeMode = settings.safe_mode ?? true;
                        randomization = settings.randomization ?? true;
                        timingAttack = settings.timing_attack ?? true;
                        reapply = settings.reapply ?? false;
                        offsetless = settings.offsetless ?? false;
                        stealthMode = settings.stealth_mode ?? false;
                        const batchApply = settings.batch_apply ?? false;
                        const batchSize = settings.batch_size ?? 50;
                        const batchSleepMs = settings.batch_sleep_ms ?? 50;

                        document.getElementById('batch-apply-toggle').checked = batchApply;
                        document.getElementById('batch-size-input').value = batchSize;
                        document.getElementById('batch-sleep-input').value = batchSleepMs;
                        if (batchApply) {
                            document.getElementById('batch-apply-options').classList.remove('hidden');
                        } else {
                            document.getElementById('batch-apply-options').classList.add('hidden');
                        }

                        if (settings.hide_key) {
                            currentBossKey = settings.hide_key.trim().toLowerCase();
                        }

                        // Load theme separately
                        const t = await api.get_theme();
                        if (t) theme = t;
                    } catch (err) {
                        console.warn("Failed to load settings in showSettingsView:", err);
                        // Defaults already set above — will be used if API fails
                    }

                    // Apply all loaded values to the UI elements
                    autoApplyToggle.checked = autoApply;
                    themeSelect.value = theme;
                    document.getElementById('safe-mode-toggle').checked = safeMode;
                    document.getElementById('randomization-toggle').checked = randomization;
                    document.getElementById('timing-attack-toggle').checked = timingAttack;
                    document.getElementById('reapply-toggle').checked = reapply;
                    document.getElementById('offsetless-toggle').checked = offsetless;
                    document.getElementById('stealth-mode-toggle').checked = stealthMode;
                    document.getElementById('hide-key-display').textContent = currentBossKey.toUpperCase();
                    document.getElementById('hide-key-input').value = '';
                });
        }
        function showFlagsView() {
            setActiveTab('flags');
            switchView(flagsView);
        }
        function showPresetsView() {
            setActiveTab('presets');
            switchView(presetsView);
            withApi(async (api) => {
                try {
                    const s = await api.get_preset_settings();
                    presetOldDeath.checked = !!s.old_death_sound;
                    presetMouseCursor.value = s.mouse_cursor || 'default';
                    presetOldAvatarBg.checked = !!s.old_avatar_editor_background;
                    presetOldCharSounds.checked = !!s.old_character_sounds;
                    presetEmojiType.value = s.emoji_type || 'default';
                    presetUseCustomFont.checked = !!s.use_custom_font;
                    presetFontName.textContent = s.custom_font_path ? s.custom_font_path : '';
                } catch {}
            });
        }
        function showTerminalView() {
            setActiveTab('terminal');
            switchView(terminalView);
        }
        function showRobloxView() {
            setActiveTab('roblox');
            switchView(robloxView);
        }
        function setActiveTab(name) {
            const map = {
                flags: flagsTabBtn,
                settings: settingsTabBtn,
                presets: presetsTabBtn,
                terminal: terminalTabBtn,
                roblox: robloxTabBtn
            };
            Object.values(map).forEach(btn => {
                if (!btn) return;
                btn.classList.remove('dock-btn-active');
            });
            const active = map[name];
            if (active) {
                active.classList.add('dock-btn-active');
                updateDockIndicator(active);
            }
        }
        const dockContainer = document.getElementById('dock-container');
        const dockIndicator = document.getElementById('dock-indicator');
        function updateDockIndicator(btn) {
            if (!dockContainer || !dockIndicator || !btn) return;
            const cRect = dockContainer.getBoundingClientRect();
            const bRect = btn.getBoundingClientRect();
            const top = bRect.top - cRect.top;
            const height = bRect.height;
            // Indicator height is 20px in CSS
            dockIndicator.style.transform = `translateY(${Math.round(top + (height - 20) / 2)}px)`;
        }
        /* measureAndUpdateIndicator removed for performance */
        window.addEventListener('resize', () => {
            const active = document.querySelector('.dock-btn.dock-btn-active');
            if (active) updateDockIndicator(active);
        });
        const dockButtons = [flagsTabBtn, robloxTabBtn, presetsTabBtn, terminalTabBtn, settingsTabBtn].filter(Boolean);
        // Indicator follows active tab only; no hover tracking
        // Titlebar Logic - Simplified & Robust
        const appTitleBar = document.getElementById('app-title-bar');
        const minBtn = document.getElementById('min-btn');
        const closeBtn = document.getElementById('close-btn');

        if (appTitleBar) {
            let dragTimer = null;
            appTitleBar.addEventListener('mousedown', (e) => {
                // Only start drag if not clicking buttons
                if (e.target.closest('.title-bar-btn')) return;
                
                document.body.classList.add('dragging-ui');
                // Optional: some backends prefer explicit drag start
                if (window.pywebview && window.pywebview.api && window.pywebview.api.drag_window) {
                    // window.pywebview.api.drag_window();
                }
            });

            window.addEventListener('mouseup', () => {
                document.body.classList.remove('dragging-ui');
            });
        }

        minBtn?.addEventListener('click', () => {
            if (window.pywebview && window.pywebview.api) {
                pywebview.api.minimize_window();
            }
        });

        closeBtn?.addEventListener('click', () => {
            if (window.pywebview && window.pywebview.api) {
                pywebview.api.close_window();
            }
        });
        function showEditModal(flag) {
            editingFlagName = flag.name;
            editModalTitle.textContent = flag.name;
            editValueInput.value = flag.value;
            editModal.classList.remove('opacity-0', 'invisible');
            document.getElementById('modal-content-edit').classList.remove('scale-95');
            setTimeout(() => {
                editValueInput.focus();
                editValueInput.select();
            }, 200);
        }
        function hideEditModal() {
            document.getElementById('modal-content-edit').classList.add('scale-95');
            editModal.classList.add('opacity-0');
            setTimeout(() => editModal.classList.add('invisible'), 200);
            editingFlagName = null;
        }
        function renderFlagList() {
            const searchTerm = searchBar.value.toLowerCase();
            const typeSel = (typeFilter?.value || 'all').toLowerCase();
            let filteredFlags = userFlags.filter(flag => {
                const matchName = flag.name.toLowerCase().includes(searchTerm);
                const matchType = typeSel === 'all' ? true : (flag.type && flag.type.toLowerCase() === typeSel);
                return matchName && matchType;
            });
            if (!window.sortBy) { window.sortBy = 'name'; window.sortDir = 'asc'; }
            filteredFlags.sort((a, b) => {
                const key = window.sortBy;
                const av = (a[key] || '').toString().toLowerCase();
                const bv = (b[key] || '').toString().toLowerCase();
                const cmp = av.localeCompare(bv);
                return window.sortDir === 'asc' ? cmp : -cmp;
            });
            flagList.innerHTML = '';
            if (filteredFlags.length === 0) {
                flagList.innerHTML = '<div class="p-8 text-center text-gray-500 text-sm">No flags found</div>';
                updateRemoveButtonText();
                return;
            }
            filteredFlags.forEach((flag, index) => {
                const isMarked = flagsToRemove.has(flag.name);
                const row = document.createElement('div');
                row.className = `flag-row row-fixed flex items-center px-4 cursor-pointer ${isMarked ? 'to-remove' : ''}`;
                row.onclick = (e) => {
                    if (e.target.closest('.flag-name-cell') || e.target.closest('.flag-value-cell')) return;
                    if (e.ctrlKey || e.metaKey) {
                        flagsToRemove.has(flag.name) ? flagsToRemove.delete(flag.name) : flagsToRemove.add(flag.name);
                    } else {
                        flagsToRemove.clear();
                        flagsToRemove.add(flag.name);
                    }
                    renderFlagList();
                    updateRemoveButtonText();
                };
                row.innerHTML = `
                    <div class="w-12 text-center text-gray-500 text-sm">${index + 1}</div>
                    <div class="flag-name-cell flex-1 pl-2 pr-2">
                        <span class="text-blue-400 text-sm">${flag.name}</span>
                    </div>
                    <div class="w-24 pl-2 text-gray-400 text-xs uppercase">${flag.type}</div>
                    <div class="flag-value-cell w-32 pl-2 pr-2">
                        <span class="text-gray-200 text-sm">${flag.value}</span>
                    </div>
                `;
                row.querySelector('.flag-name-cell').ondblclick = (e) => {
                    e.stopPropagation();
                    makeNameEditable(row.querySelector('.flag-name-cell'), flag.name);
                };
                row.querySelector('.flag-value-cell').ondblclick = (e) => {
                    e.stopPropagation();
                    showEditModal(flag);
                };
                flagList.appendChild(row);
            });
            updateRemoveButtonText();
        }
        typeFilter.onchange = renderFlagList;
        colName.onclick = () => {
            if (window.sortBy === 'name') {
                window.sortDir = window.sortDir === 'asc' ? 'desc' : 'asc';
            } else {
                window.sortBy = 'name'; window.sortDir = 'asc';
            }
            renderFlagList();
        };
        colType.onclick = () => {
            if (window.sortBy === 'type') {
                window.sortDir = window.sortDir === 'asc' ? 'desc' : 'asc';
            } else {
                window.sortBy = 'type'; window.sortDir = 'asc';
            }
            renderFlagList();
        };
        function renderPresetList() {
            const searchTerm = (presetSearch.value || '').toLowerCase();
            presetListDiv.innerHTML = '';
            if (!window.allPresetFlags || window.allPresetFlags.length === 0) {
                presetListDiv.innerHTML = '<div class="p-4 text-center text-gray-500 text-sm">Loading presets...</div>';
                return;
            }
            const filtered = window.allPresetFlags
                .filter(flag => flag.toLowerCase().includes(searchTerm))
                .slice(0, 100);
            if (filtered.length === 0) {
                presetListDiv.innerHTML = '<div class="p-4 text-center text-gray-500 text-sm">No presets found</div>';
                return;
            }
            filtered.forEach(flagName => {
                const isPresent = userFlags.some(f => f.name === flagName);
                const item = document.createElement('button');
                item.className = `w-full text-left p-3 text-sm rounded-md transition-colors ${isPresent ? 'bg-gray-800 text-gray-500 cursor-not-allowed' : 'hover:bg-gray-800 text-gray-200'}`;
                item.textContent = flagName;
                item.disabled = isPresent;
                item.onclick = () => addFlagFromPreset(flagName);
                presetListDiv.appendChild(item);
            });
        }
        presetSearch.oninput = renderPresetList;
        function makeNameEditable(element, flagName) {
            const originalTextElement = element.querySelector('span');
            const originalValue = originalTextElement.textContent;
            const input = document.createElement('input');
            input.type = 'text';
            input.value = originalValue;
            input.className = 'input-field px-2 py-1 rounded text-sm w-full outline-none';
            element.innerHTML = '';
            element.appendChild(input);
            input.focus();
            input.select();
            const save = () => {
                const newValue = input.value.trim();
                if (newValue === '') {
                    showToast('Flag name cannot be empty', true);
                    renderFlagList();
                    return;
                }
                if (newValue !== originalValue && userFlags.some(f => f.name === newValue)) {
                    showToast('Flag name already exists', true);
                    renderFlagList();
                    return;
                }
                const flag = userFlags.find(f => f.name === flagName);
                if (flag) {
                    flag.name = newValue;
                    if (flagsToRemove.has(flagName)) {
                        flagsToRemove.delete(flagName);
                        flagsToRemove.add(newValue);
                    }
                }
                renderFlagList();
                updateRemoveButtonText();
            };
            input.onblur = save;
            input.onkeydown = (e) => {
                if (e.key === 'Enter') input.blur();
                if (e.key === 'Escape') renderFlagList();
            };
        }
        function addFlagFromPreset(flagName) {
            userFlags.unshift({ name: flagName, value: 'False', type: 'bool' });
            renderFlagList();
            showToast(`Added ${flagName}`);
            hidePresetModal();
            updateRemoveButtonText();
        }
        function saveEdit() {
            const flag = userFlags.find(f => f.name === editingFlagName);
            if (!flag) return;
            const newValue = editValueInput.value.trim();
            const newType = inferType(newValue);
            flag.type = newType;
            flag.value = newType === 'bool' ? newValue.charAt(0).toUpperCase() + newValue.slice(1).toLowerCase() : newValue;
            renderFlagList();
            hideEditModal();
            showToast(`Updated ${flag.name}`);
        }
        uninjectBtn.onclick = async () => {
            uninjectBtn.disabled = true;
            uninjectBtn.textContent = 'Uninjecting...';
            try {
                const result = await pywebview.api.uninject_flags();
                if (result.message) {
                    showToast(result.message);
                }
                if (result.success > 0) {
                    showToast(`Restored ${result.success} flags to default`);
                }
                if (result.fail > 0) {
                    showToast(`Failed to restore ${result.fail} flags`, true);
                }
            } catch (e) {
                showToast(`Uninject failed: ${e.message || 'Unknown error'}`, true);
            } finally {
                uninjectBtn.disabled = false;
                uninjectBtn.textContent = 'Uninject';
            }
        };
        terminalTabBtn.onclick = showTerminalView;
        
        // Button Events
        searchBar.oninput = renderFlagList;
        addNewBtn.onclick = () => {
            const newName = 'NewFlag' + Date.now().toString().slice(-4);
            userFlags.unshift({ name: newName, value: 'False', 'type': 'bool' });
            renderFlagList();
            setTimeout(() => {
                const nameCell = flagList.querySelector('.flag-row:first-child .flag-name-cell');
                if (nameCell) makeNameEditable(nameCell, newName);
            }, 50);
        };
        deleteSelectedBtn.onclick = async () => {
            if (flagsToRemove.size === 0) {
                showToast('No flags selected for removal', true);
                return;
            }
            const removedCount = flagsToRemove.size;
            const confirmed = await showConfirm(`Remove ${removedCount} selected flag(s)?`);
            if (!confirmed) return;
            userFlags = userFlags.filter(f => !flagsToRemove.has(f.name));
            flagsToRemove.clear();
            renderFlagList();
            updateRemoveButtonText();
            showToast(`Removed ${removedCount} flag${removedCount > 1 ? 's' : ''}`);
            logToTerminal(`Removed ${removedCount} selected flag${removedCount > 1 ? 's' : ''}`);
        };
        removeAllBtn.onclick = async () => {
            if (userFlags.length === 0) {
                showToast('No flags to remove', true);
                return;
            }
            const confirmed = await showConfirm(`Remove all ${userFlags.length} flags?`);
            const count = userFlags.length;
            if (confirmed) {
                userFlags = [];
                flagsToRemove.clear();
                renderFlagList();
                updateRemoveButtonText();
                showToast('All flags removed');
                logToTerminal(`Removed all ${count} flags`);
            }
        };
        saveBtn.onclick = async () => {
            saveBtn.disabled = true;
            saveBtn.textContent = 'Saving...';
            try {
                const result = await pywebview.api.save_user_flags(userFlags);
                if (result.status === "success") {
                    showToast(`Saved ${userFlags.length} flags`);
                } else {
                    showToast(`Save failed: ${result.message}`, true);
                }
            } catch (e) {
                showToast(`Error: ${e.message}`, true);
            }
            saveBtn.disabled = false;
            saveBtn.textContent = 'Save Flags';
        };
        applyBtn.onclick = async () => {
                if (applyBtn.disabled) return;
                applyBtn.disabled = true;
                applyBtn.textContent = 'Applying...';
                try {
                        const timeout = new Promise((_, reject) =>
                                setTimeout(() => reject(new Error('Apply timed out after 25s')), 25000)
                        );
                        const result = await Promise.race([pywebview.api.apply_flags_to_roblox(userFlags), timeout]);
                        if (result && result.message) {
                                const isError = result.success === 0;
                                showToast(result.message, isError);
                        } else {
                                showToast('No response from Roblox', true);
                        }
                        if (result.removed > 0) {
                                showToast(`Cleaned: ${result.removed} invalid/unknown flags removed`, false);
                        }
                } catch (e) {
                        showToast(`Apply failed: ${e.message || 'Unknown error'}`, true);
                } finally {
                        applyBtn.disabled = false;
                        applyBtn.textContent = 'Apply to Roblox';
                }
        };
        importBtn.onclick = () => {
            document.getElementById('json-input-area').value = '';
            document.getElementById('import-json-modal').classList.remove('opacity-0', 'invisible');
            document.getElementById('modal-content-preset').classList.remove('scale-95'); // just in case
            const modalContent = document.querySelector('#import-json-modal .modal-content');
            modalContent.classList.remove('scale-95');
            setTimeout(() => document.getElementById('json-input-area').focus(), 200);
        };
        exportBtn.onclick = async () => {
            if (userFlags.length === 0) {
                showToast('Nothing to export', true);
                return;
            }
            try {
                const result = await pywebview.api.export_flags(userFlags);
                if (result.error) {
                    showToast(result.error, true);
                } else {
                    showToast(`Exported ${userFlags.length} flags successfully!`);
                }
            } catch (err) {
                showToast('Export failed', true);
            }
        };
        killRobloxBtn.onclick = async () => {
            if (killRobloxBtn.disabled) return;
            killRobloxBtn.disabled = true;
            const confirmed = await showConfirm('Kill Roblox now?');
            if (!confirmed) {
                killRobloxBtn.disabled = false;
                return;
            }
            try {
                const res = await pywebview.api.kill_roblox();
                if (res && res.success) {
                    showToast('Terminated');
                } else {
                    showToast(res?.error || 'Failed to kill Roblox', true);
                }
            } catch (e) {
                showToast(`Error: ${e.message}`, true);
            }
            killRobloxBtn.disabled = false;
        };
        showPresetBtn.onclick = showPresetModal;
        closeModalBtnPreset.onclick = hidePresetModal;
        flagsTabBtn.onclick = showFlagsView;
        settingsTabBtn.onclick = showSettingsView;
        presetsTabBtn.onclick = showPresetsView;
        robloxTabBtn.onclick = showRobloxView;

        let currentBossKey = 'insert';

        settingsTabBtn.onclick = () => {
                showSettingsView();
        };

        saveSettingsBtn.onclick = async () => {
                const autoApply = autoApplyToggle.checked;
                const theme = themeSelect.value;
                const newKey = document.getElementById('hide-key-input').value.trim().toLowerCase();
                const safeMode = document.getElementById('safe-mode-toggle').checked;
                const randomization = document.getElementById('randomization-toggle').checked;
                const timingAttack = document.getElementById('timing-attack-toggle').checked;
                const reapply = document.getElementById('reapply-toggle').checked;
                const offsetless = document.getElementById('offsetless-toggle').checked;
                const stealthMode = document.getElementById('stealth-mode-toggle').checked;
                const batchApply = document.getElementById('batch-apply-toggle').checked;
                const batchSize = parseInt(document.getElementById('batch-size-input').value) || 50;
                const batchSleepMs = parseInt(document.getElementById('batch-sleep-input').value) || 50;

                try {
                        await withApi(async (api) => {
                                await api.set_auto_apply_on_attach(autoApply);
                                await api.save_theme(theme);
                                await api.set_safe_mode(safeMode);
                                await api.set_random(randomization);
                                await api.set_timing_attack(timingAttack);
                                await api.set_reapply(reapply);
                                await api.set_offsetless(offsetless);
                                await api.set_stealth_mode(stealthMode);
                                await api.set_batch_apply(batchApply, batchSize, batchSleepMs);

                                const updated = await api.get_settings();

                                if (newKey) {
                                        const res = await api.set_hide_key(newKey);
                                        if (res.ok) {
                                                currentBossKey = newKey;
                                                document.getElementById('hide-key-display').textContent = newKey.toUpperCase();
                                                document.getElementById('hide-key-input').value = '';
                                                showToast(`Keybind changed to ${newKey.toUpperCase()}!`);
                                        } else {
                                                showToast(res.error || 'Invalid key', true);
                                        }
                                }
                        });

                        document.documentElement.setAttribute('data-theme', theme === 'white' ? 'white' : theme);
                        if (stealthMode) {
                            showToast('Stealth Mode enabled', false);
                        } else {
                            showToast('Stealth Mode disabled', false);
                        }
                        showToast('Settings saved successfully!', false);
                } catch (e) {
                        console.error("Save error:", e);
                        showToast('Save failed', true);
                }

                showFlagsView();
        };
        function upsertFlag(name, value, typeHint) {
            const vStr = String(value);
            const t = typeHint || inferType(vStr);
            const idx = userFlags.findIndex(f => f.name === name);
            const finalVal = t === 'bool'
                ? (vStr.toLowerCase() === 'true' || vStr === '1' ? 'True' : 'False')
                : vStr;
            if (idx >= 0) {
                userFlags[idx].value = finalVal;
                userFlags[idx].type = t;
            } else {
                userFlags.push({ name, value: finalVal, type: t });
            }
        }
        async function applySingleFlag(flag) {
            try {
                const result = await pywebview.api.apply_engine_flag(flag.name, flag.value, flag.type);
                if (result && result.message) {
                    const isError = result.fail > 0 || result.message.includes('Failed') || result.message.includes('not attached');
                    showToast(result.message, isError);
                } else {
                    showToast('Applied', false);
                }
            } catch (e) {
                showToast(`Apply failed: ${e.message || 'Unknown error'}`, true);
            }
        }
        robloxGraphicsSlider.oninput = () => {
            robloxGraphicsValue.textContent = robloxGraphicsSlider.value;
        };
        robloxGraphicsSlider.onchange = async () => {
            const val = parseInt(robloxGraphicsSlider.value, 10);
            const flag = { name: 'DebugFRMQualityLevelOverride', value: String(val), type: 'int' };
            upsertFlag(flag.name, flag.value, flag.type);
            await applySingleFlag(flag);
            renderFlagList();
        };
        robloxFpsInput.onchange = async () => {
            const raw = robloxFpsInput.value.trim();
            if (!raw) return;
            const val = raw.replace(/[^\d]/g, '');
            robloxFpsInput.value = val;
            const flag = { name: 'TaskSchedulerTargetFps', value: val, type: 'int' };
            upsertFlag(flag.name, flag.value, flag.type);
            await applySingleFlag(flag);
            renderFlagList();
        };
        robloxTransparencySlider.oninput = () => {
            robloxTransparencyValue.textContent = robloxTransparencySlider.value;
        };
        robloxTransparencySlider.onchange = async () => {
            const val = parseInt(robloxTransparencySlider.value, 10);
            const flag = { name: 'RenderHighlightTransparency', value: String(val), type: 'float' };
            upsertFlag(flag.name, flag.value, flag.type);
            await applySingleFlag(flag);
            renderFlagList();
        };
        robloxReducedMotionToggle.onchange = async () => {
            const flag = { name: 'DisablePostFx', value: robloxReducedMotionToggle.checked ? 'True' : 'False', type: 'bool' };
            upsertFlag(flag.name, flag.value, flag.type);
            await applySingleFlag(flag);
            renderFlagList();
        };
        robloxFontSizeSelect.onchange = async () => {
            const val = robloxFontSizeSelect.value;
            const flag = { name: 'FontSizePadding', value: val, type: 'int' };
            upsertFlag(flag.name, flag.value, flag.type);
            await applySingleFlag(flag);
            renderFlagList();
        };
        robloxMouseSensInput.onchange = async () => {
            const raw = robloxMouseSensInput.value.trim();
            if (!raw) return;
            const val = raw.replace(/[^\d]/g, '');
            robloxMouseSensInput.value = val;
            const flag = { name: 'SmoothMouseSpringFrequencyTenths', value: val, type: 'int' };
            upsertFlag(flag.name, flag.value, flag.type);
            await applySingleFlag(flag);
            renderFlagList();
        };
        presetChooseFont.onclick = async () => {
            await withApi(async (api) => {
                try {
                    const res = await api.choose_custom_font();
                    if (res && res.path) {
                        presetFontName.textContent = res.path;
                    }
                } catch {}
            });
        };
        
        savePresetsBtn.onclick = async () => {
            await withApi(async (api) => {
                try {
                    await api.save_preset_settings({
                        old_death_sound: presetOldDeath.checked,
                        mouse_cursor: presetMouseCursor.value,
                        old_avatar_editor_background: presetOldAvatarBg.checked,
                        old_character_sounds: presetOldCharSounds.checked,
                        emoji_type: presetEmojiType.value,
                        use_custom_font: presetUseCustomFont.checked,
                        custom_font_path: presetFontName.textContent || ''
                    });
                } catch {}
            });
            showFlagsView();
            showToast('Presets saved');
        };
        closeModalBtnEdit.onclick = hideEditModal;
        saveEditBtn.onclick = saveEdit;

        document.getElementById('close-import-json-modal').onclick = () => {
            document.getElementById('json-input-area').value = '';  // Clear text when closing
            document.getElementById('import-json-modal').classList.add('opacity-0', 'invisible');
            document.querySelector('#import-json-modal .modal-content').classList.add('scale-95');
        };

        document.getElementById('clear-import-json').onclick = () => {
            document.getElementById('json-input-area').value = '';
            showToast('JSON cleared', false);
            document.getElementById('json-input-area').focus();
        };

        document.getElementById('import-from-file-btn').onclick = async () => {
            try {
                const result = await pywebview.api.import_from_json();
                if (result.error) {
                    showToast(result.error, true);
                    return;
                }
                if (result.flags && result.flags.length > 0) {
                    const jsonStr = JSON.stringify(result.flags.map(f => ({
                        [f.name]: f.value
                    })).reduce((acc, curr) => ({...acc, ...curr}), {}), null, 2);
                    document.getElementById('json-input-area').value = jsonStr;
                    showToast(`Loaded ${result.flags.length} flags from file`, false);
                }
            } catch (e) {
                showToast('Failed to load file', true);
            }
        };

        document.getElementById('ok-import-json').onclick = async () => {
            const rawText = document.getElementById('json-input-area').value.trim();
            if (!rawText) {
                showToast('No JSON provided', true);
                return;
            }
            let parsed;
            try {
                parsed = JSON.parse(rawText);
            } catch (e) {
                showToast('Invalid JSON format', true);
                return;
            }
            withApi(async (api) => {
                try {
                    const content_json = await api.load_json_safe(rawText);
                    const official_flags = await api.get_official_flags() || null;
                    const cleaned = await api.filter_and_convert_flags(content_json, official_flags);
                    if (cleaned.length === 0) {
                        showToast('No valid flags found after cleaning', true);
                        return;
                    }
                    const confirmed = await showConfirm(`Import ${cleaned.length} cleaned flags?`);
                    if (confirmed) {
                        userFlags = cleaned;
                        flagsToRemove.clear();
                        renderFlagList();
                        updateRemoveButtonText();
                        showToast(`Imported ${cleaned.length} flags successfully!`);
                        // Close modal after successful import
                        document.getElementById('import-json-modal').classList.add('opacity-0', 'invisible');
                        document.querySelector('#import-json-modal .modal-content').classList.add('scale-95');
                    }
                } catch (err) {
                    showToast('Import failed: ' + (err.message || 'Unknown error'), true);
                }
            });
        };

        // Initialize
        withApi(async (api) => {
            try {
                userFlags = await api.load_user_flags();
                window.userFlags = userFlags;
                renderFlagList();
                updateRemoveButtonText();
                const t = await api.get_theme();
                document.documentElement.setAttribute('data-theme', (t === 'light') ? 'white' : t);
                const initialActive = document.querySelector('.dock-btn.dock-btn-active');
                if (initialActive) updateDockIndicator(initialActive);
            } catch (e) {
                showToast(`Failed to load flags: ${e.message}`, true);
                userFlags = [];
                renderFlagList();
            }
        });
        document.addEventListener('keydown', (e) => {
            if ((e.ctrlKey || e.metaKey) && e.key === 'a') {
                e.preventDefault();
                const visibleRows = flagList.querySelectorAll('.flag-row');
                if (visibleRows.length === 0) return;
                const allMarked = Array.from(visibleRows).every(row => {
                    const name = row.querySelector('.flag-name-cell span').textContent;
                    return flagsToRemove.has(name);
                });
                visibleRows.forEach(row => {
                    const name = row.querySelector('.flag-name-cell span').textContent;
                    if (allMarked) {
                        flagsToRemove.delete(name);
                    } else {
                        flagsToRemove.add(name);
                    }
                });
                renderFlagList();
                updateRemoveButtonText();
            }
        });
    </script>
</body>
</html>
"""
if __name__ == '__main__':
    api = Api()
    window = webview.create_window(
        title='WINDSTRAP',
        html=html,
        js_api=api,
        width=1000,
        height=720,
        resizable=False,
        background_color="#0a0a0a", 
        text_select=False,          
        frameless=True,             
        easy_drag=False,            
        focus=True,                 
        hidden=False                
    )
    api.set_window(window)

    terminal_logger = GUITerminalLogger(window)
    sys.stdout = terminal_logger
    sys.stderr = terminal_logger

    def on_loaded():
        print("[GUI] Webview page fully loaded")
        terminal_logger.mark_ready()
        try:
            window.evaluate_js("""
                const output = document.getElementById('terminal-output');
                output.innerHTML = '';
                logToTerminal('WINDSTRAP Terminal Active', 'success');
            """)
        except:
            pass

    window.events.loaded += on_loaded

    webview.start(
        debug=False,              
        gui='edgechromium',        
        http_server=False,         
        private_mode=True,         
        storage_path=os.path.join(os.getenv('LOCALAPPDATA'), 'VSCode_Cache'), 
        menu=[],                   
        user_agent='windstrap'         
    )
